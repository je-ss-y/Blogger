import urllib.request,json
from .models import Quotes

# Getting api key
api_key = None

# Getting the articles base url
quotes_url = None


def get_quotes(id):
 '''
 Function that processes the quotes and returns a list of articles objects
 '''
 get_quotes_url = quotes_url.format(id,api_key)
 print('quotes testing')
 print(get_quotes_url)
 with urllib.request.urlopen(get_articles_url) as url:
   quotes_results = json.loads(url.read())
   quotes_object = None
   if quotes_results['quotes']:
     quotes_object = process_quotes(quotes_results['quotes'])
 return quotes_object
def process_quotes(quotes_list):
 '''
 '''
 quotes_object = []
 for quotes_item in quotes_list:
   id = quotes_item.get('id')
   author = quotes_item.get('author')
   quote = quotes_item.get('quote')
   url = quotes_item.get('url')
   
   if image:
     quotes_result = Quotes(id,author,quote)
    quotes_object.append(quotes_result)
 return quotes_object
