import os
import requests
import re

try:
    path="S2_API_KEY.txt"
    os.environ["S2_API_KEY"] = open(path, 'r').read()
except:
    print("txt file with key missing.")





def get_papers(query, result_limit=5):
    if not query:
        return None

    rsp = requests.get('https://api.semanticscholar.org/graph/v1/paper/search',
                        headers={'X-API-KEY': os.environ["S2_API_KEY"]},
                        params={'query': query, 'limit': result_limit, 'fields': 'title,url,authors,abstract'})
    #print(rsp.text)
    rsp.raise_for_status()
    results = rsp.json()
    total = results["total"]
    if not total:
        return None

        #print(f'Found {total} results. Showing up to {result_limit}.')
        #papers = results['data']
        #print_papers(papers)

    #selection = ''
    #while not re.fullmatch('\\d+', selection):
    #    selection = input('Select a paper # to base recommendations on: ')
    return results['data']#[int(selection)]