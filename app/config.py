import os

class Config:
    '''
    General configuration parent class
    '''
    
    SOURCES_URL = 'https://newsapi.org/v2/sources?category={}&language=en&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?q=Apple&from=2021-09-11&sortBy=popularity&apiKey={}'
    HEADLINES_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
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
    pass  