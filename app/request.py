import urllib.request,json
from .models import Articles,Sources


sources_url = None
articles_url = None

def configure_request(app):
    global api_key,sources_url,articles_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCES_URL']
    articles_url = app.config['ARTICLES_URL']

def get_sources(sources):
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey='.format(sources)
    with urllib.request.urlopen(get_sources_url) as url:
        sources_data = url.read()
        sources_response = json.loads(sources_data)
        
        sources_results = None
        
        if sources_response['sources']:
            sources_list = sources_response['sources']
            
            sources_results = process_sources(sources_list)
            
        return sources_results
    
def process_sources(sources_list):
    '''
    Function that processesses the source results and turns them to a list of objects
    '''
    
    sources_results = []
    
    for source in sources_list:
        id = source.get('id')
        name = source.get("name")
        description = source.get('description')
        url = source.get('url')
        category = source.get('category')
        language = source.get('language')
        
        if language == 'en':
            
            source_object =Sources(id,name,description,url,category,language)
            sources_results.append(source_object)
            
    return sources_results


def get_articles(articles):
    '''
    function to get json response
    '''
    
    get_articles_url = 'https://newsapi.org/v2/everything?q=Apple&from=2021-09-11&sortBy=popularity&apiKey='.format(articles)
    
    with urllib.request.urlopen(get_articles_url) as url:
        
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        
        articles_results = None
        
        if articles_response['articles']:
            articles_list =  articles_response['articles']
            articles_results = process_articles(articles_list)
            
        return articles_results
    
def process_articles(articles_list):
    
    articles_results = []
    
    for article in articles_list:
        id = article['source']['id']
        name = article.get('name')
        author = article.get('author')
        content = article.get('content')
        title = article.get('title')
        description = article.get('description')
        url = article.get('url')
        urlToImage = article.get('urlToImage')
        publishedAt = article.get('publishedAt')
        
        if urlToImage:
            articles_object = Articles(id,name,author,title,description,url,urlToImage,publishedAt,content)
            
            articles_results.append(articles_object)
            
    return articles_results
        