#%%
import requests
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

print(response.keys())