import unittest
from app.models import Movie

class TestQuotes(unittest.TestCase):
    '''
    Test class to test the behavior of the quotes class
    '''
    def setUp(self):
        '''
        Test class to run before other tests
        '''
        self.new_quotes = Quotes('shhhh','ishhh','just testing','https://anylink.com')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))
    
    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_quotes.id,'21')
        self.assertEquals(self.new_quotes.quote,'just testing')
        self.assertEquals(self.new_quotes.url,'http://quotes.stormconsultancy.co.uk/quotes/21')