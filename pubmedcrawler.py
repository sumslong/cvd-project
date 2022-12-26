import bs4
import requests 
import json
import urllib.request, urllib.parse, urllib.error
import searchterms
import nlpgradelevel
import re

'''

Code for crawling through PubMed to obtain articles related to the search terms that
are relevant to the user
Learned from this tutorial: https://github.com/PhilippeCodes/Web-Scraping-PubMed/blob/master/Scrape_PubMed.py

'''

def idlist(sys_bp, sex, BMI, smoke):
    search_terms, search_list = searchterms.constructing_search_terms(sys_bp, sex, BMI, smoke)
    search_terms = search_terms.replace(" ", "%20")
    starting_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=9&sort=relevance&term=search_terms"
    starting_url = starting_url.replace('search_terms', search_terms)
    webpage = urllib.request.urlopen(starting_url).read()
    dict_page = json.loads(webpage)
    idlist = dict_page["esearchresult"]["idlist"]

    return (idlist, search_list)


def get_articles_and_abstracts(sys_bp, sex, BMI, smoke, literacy_level):
    '''
    Crawls through PubMed with the appropriate search terms, sorts the list of nine article
    in order of relevancy, and outputs all the information for the top five most relevant
    articles in order based on both literacy level and number of times the key words appear
    '''
    article_list = [] 
    id_list, search_list = idlist(sys_bp, sex, BMI, smoke)
    keys = "|".join(search_list)
    
    for link in id_list:
        
        begin_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&retmode=xml&id=idlist"
        article_url = begin_url.replace('idlist', link)
        article_begin_link = "https://pubmed.ncbi.nlm.nih.gov/idlist"
        article_link = article_begin_link.replace('idlist', link)
    
        r = requests.get(article_url)
        soup = bs4.BeautifulSoup(r.content, "html.parser")
        
        article = soup.find('article')
        
        if article.find('articletitle').text:
            article_title = article.find('articletitle').text
            
        author_list = article.find('authorlist')
        authors = "" 
        if author_list:
            for i in range(len(author_list.find_all('lastname'))):
                last_name = author_list.find_all('lastname')[i].text
                authors+= last_name + ", "
        
        authors = authors[:len(authors) - 2]
        
        if article.find('abstracttext'):
            abstract = article.find('abstracttext').text

        key_word_count = nlpgradelevel.count_key_words(keys, abstract)
        literacy_level, lit_score = nlpgradelevel.get_literacy_level(abstract)

        #create a relevancy score integrating both natural language processing
        #and regular expressions for number of key words
        if literacy_level == "Basic" or literacy_level == "Intermediate":
            relevancy_score = lit_score + key_word_count
        else:
            relevancy_score = lit_score - key_word_count

        article_list.append((article_link, article_title, authors, abstract, literacy_level, lit_score, relevancy_score))

    #sort based on the relavency score for each category of literacy levels
    if literacy_level == "Basic" or literacy_level == "Intermediate":
        article_list = sorted(article_list, key=lambda i: i[-1], reverse=True)
        
    if literacy_level == "High":
        article_list = sorted(article_list, key=lambda i: i[-1]) 

    #returns the top 5 articles    
    return article_list[:5]

    
