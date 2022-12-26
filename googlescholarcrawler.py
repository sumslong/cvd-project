import bs4
import requests 
import lxml
import searchterms


'''

Code for crawling through Google Scholar
Learned from this tutorial: https://dev.to/dmitryzub/scrape-google-scholar-with-python-32oh

'''


def search_parameters(search_terms): 
    params = {
        "q": search_terms,
        "hl": "en" 
    }
    
    return params


def google_scholar_links(sys_bp, sex, BMI, smoke):
    '''
    Obtains the Google Scholar links from the first page of results
    given a set of search terms
    
    Input: params: a dictionary with keys ("q", "hl") where "hl"'s value 
        is the language, and "q"'s value is the search terms
    
    Output: a list of links, authors, and snippets
    '''
    
    search_terms, _ = searchterms.constructing_search_terms(sys_bp, sex, BMI, smoke)
    params = search_parameters(search_terms)

    headers = {
    'User-agent':
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582"
    }
    
    google_scholar_articles = [] 
    
    html = requests.get('https://scholar.google.com/scholar', headers=headers, params=params).text
    soup = bs4.BeautifulSoup(html, 'lxml')
    
    for result in soup.select('.gs_ri'):
        link = result.select_one('.gs_rt a')['href']
        title = result.select_one('.gs_rt').text
        publication_info = result.select_one('.gs_a').text.replace(u'\xa0', u' ')
        snippet = result.select_one('.gs_rs').text
        google_scholar_articles.append(link)
        
    return google_scholar_articles



