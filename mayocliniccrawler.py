import bs4
import requests 
import json
import urllib.request, urllib.parse, urllib.error
import searchterms

'''

Web crawler for MayoClinic

'''

def link_to_search(search_terms):
    
    search_terms = search_terms.replace(" ", "%20")
    starting_url = "https://www.mayoclinic.org/search/search-results?q=search_terms"
    starting_url = starting_url.replace('search_terms', search_terms)

    return starting_url


def links_from_search(sys_bp, sex, BMI, smoke):
    
    search_terms, _ = searchterms.constructing_search_terms(sys_bp, sex, BMI, smoke)
    starting_url = link_to_search(search_terms)
    mayoclinic_articles = []
    
    headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }

    r = requests.get(starting_url, headers=headers)
    soup = bs4.BeautifulSoup(r.content, "html.parser")
    
    for link in soup.findAll('a'):
        if link.get('href'):
            if "www.mayoclinic.org" in link.get('href'):
                mayoclinic_articles.append(link.get('href'))
            
    return mayoclinic_articles[3:] 
