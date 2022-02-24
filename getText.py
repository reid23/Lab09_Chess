#%%
import requests
from random import randint
#%%
response = requests.get(
    'https://en.wikipedia.org/w/api.php',
    params={
        'action': 'query',
        'format': 'json',
        'titles': 'Chess',
        'prop': 'extracts',
        'explaintext': True,
    }
).json()

text=response['query']['pages']['5134']['extract'].split(' ')

print(len(text))

# %%
def getSnippet(text, length=11963, snippetSize=43):
    r=randint(0, length-snippetSize)
    return ' '.join(text[r:r+snippetSize]).remove('\n')

# %%
