import os

class Config:
    '''
    General configuration parent class
    '''
    
    SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey=6e8935872b5c41d8b095146feb42ddee'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2022-02-27&sortBy=popularity&apiKey=6e8935872b5c41d8b095146feb42ddee'
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=6e8935872b5c41d8b095146feb42ddee'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')

class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    
    
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}    
