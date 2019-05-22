import json
import bs4 as bs
from botocore.vendored import requests
import random
import re

def getQuote(keyword):
    try:
        list_quotes = []
        url = requests.get('https://www.brainyquote.com/search_results?q='+keyword).text
        soup = bs.BeautifulSoup(url, 'html.parser')
        for quote in soup.find_all('div', class_='clearfix'):
            quote_text = quote.a.text
            # only select quote shorter than 400 characters
            if len(quote_text) < 400:
                list_quotes.append(quote_text)
            else: pass
            random_quote = random.choice(list_quotes)
            # remove the brackets
            # random_quote = re.sub(r'^[\'\"]|[\'\"]$', '', random_quote)
            
        return random_quote
        
    except Exception as e:
        return 'Keyword not found.'

def lambda_handler(event, context):
    keyword = event['queryStringParameters']['k']
    quote = getQuote(keyword)
    
    return {
        "statusCode": 200,
        "body": json.dumps(quote)
    }