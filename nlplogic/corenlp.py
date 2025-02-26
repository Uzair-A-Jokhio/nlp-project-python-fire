from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    """Search in wikipedia
    Argument:
        str: Name

    Return:
        str: Details about name"""
    print(f"Searching for name {name}")
    return wikipedia.search(name)


def summarize_wiki(name):
    """Summarizes the wikipedia search"""
    print(f"Finding wikipedia summary name: {name}")
    return wikipedia.summary(name)


def get_text_blob(name):
    """Gets Text blob object and returns"""
    blob = TextBlob(name)
    return blob


def get_phrases(name):
    """finds wikipedia name and returns back phraese"""
    text = summarize_wiki(name)
    blob = TextBlob(text)
    phrases = blob.noun_phrases
    return phrases
