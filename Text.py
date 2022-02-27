#hey!
# this module uses things we haven't done in
# class. However, the only functions used at
# runtime are loadWikiWords() and getSnippet(),
# which don't have any of the fancy things.
# un-taught stuff is all in updateWikiWords(),
# which is for getting the data from wikipedia,
# parsing it, and saving it to csv.

import requests
from random import randint
import re
import pandas as pd


def updateWikiWords():
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

    text=response['query']['pages']['5134']['extract']

    while '\n\n' in text:
        text = re.sub('\n\n', '\n', text)
    text=text.split(' ')

    df=pd.DataFrame(text)
    df.to_csv('wikiWords.csv', index=False)

    return text

def loadWikiWords(file='wikiWords.csv'):
    with open(file, 'r') as f:
        return f.read().split('\n')[1:] #[1:] gets rid of leading zero from stupid pandas column labels
        #not using readLines() because that puts a bunch of \n chars in

def getSnippet(text, length=11963, snippetSize=43):
    r=randint(0, length-snippetSize)
    return ' '.join(text[r:r+snippetSize])


if __name__ == '__main__':
    updateWikiWords()

