import random

import requests
from bs4 import BeautifulSoup


INVALID_TAGS = ['b', 'i', 'u', 'a', 'sup']


def get_webpage(url):
    """
    Download a webpage and clean it up using beautiful soup. I'm only looking for factoids so I'm just looking for
    <p></p> tags. I also want all nested tags to be removed and just the internal content remaining.

    :param str url: The URL to fetch and parse.
    :return: A list of strings containing cleansed/parsed elements.
    """
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, features="html.parser")

    for tag in INVALID_TAGS:
        for match in soup.findAll(tag):
            match.replaceWithChildren()

    paragraphs = [str.join('', paragraph.children) for paragraph in soup.findAll('p')]
    return paragraphs


def get_random_fact(url):
    """
    Get a random fact from the specified webpage.

    :param str url: The URL to fetch the facts from.
    :return str: A string containing a factoid from the specified webpage.
    """
    facts = get_webpage(url)
    return facts[random.randint(0, len(facts))]
