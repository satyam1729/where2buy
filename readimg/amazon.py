import requests

def bing_search(query):
    try:
    	url = 'https://api.cognitive.microsoft.com/bing/v5.0/search'
    # query string parameters
    	payload = {'q': query}
    # custom headers
    # change key for use
    	headers = {'Ocp-Apim-Subscription-Key': '8a4c7e6ad5694d4f960334295d01c3e4'}
    # make GET request
    	r = requests.get(url, params=payload, headers=headers)
    # get JSON response
    	return r.json()['webPages']['value'][0]['url']
    except:
    	return "url not found"

#j = bing_search('art of war amazon')
#print j
