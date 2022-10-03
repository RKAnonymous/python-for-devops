import wikipedia
from textblob import TextBlob


def wiki(name="Uzbekistan", length=1):
    """This is a wikipedia fetcher"""

    wiki_result = wikipedia.summary(name, length)
    return wiki_result


def search(name):
    """Search Wikipedia for Names"""

    results = wikipedia.search(name)
    return results


def phrase(name):
    """Returns phrases from wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
