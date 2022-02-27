import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test class to test the behaviour of the class
    '''
    
    def setUp(self):
        '''
        setUp method that will run before every test
        '''
        self.new_article = Articles("techcrunch","TechCrunch","Connie Loizos","Tesla should say something","http://techcrunch.com/2021/09/10/tesla-should-say-something/","http://techcrunch.com/2021/09/10/tesla-should-say-something/","2021-09-11T05:37:56Z","Last weekend, a reader wrote to this editor, politely asking")
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))
        
        
    def test_init(self):
        self.assertEqual(self.new_article.id,"techcrunch")
        self.assertEqual(self.new_article.name,"TechCrunch")
        self.assertEqual(self.new_article.author,"Natasha Mascarenhas")
        self.assertEqual(self.new_article.title,"Startups scramble in wake of Ukraine invasion")
        self.assertEqual(self.new_article.description,"Welcome to Startups Weekly, a fresh human-first take on this week’s startup")
        self.assertEqual(self.new_article.url,"http://techcrunch.com/2022/02/27/Startups scramble in wake of Ukraine invasion")
        self.assertEqual(self.new_article.urlToImage,"https://techcrunch.com/wp-content/uploads/2020/02/GettyImages-655825116.jpeg?w=730&crop=1")
        self.assertEqual(self.new_article.publishedAt,"2022-02-2610:00pm")
        self.assertEqual(self.new_article.content,"Welcome to Startups Weekly, a fresh human-first take on this week’s startup news and ")
if __name__ == '__main__':
    unittest.main()