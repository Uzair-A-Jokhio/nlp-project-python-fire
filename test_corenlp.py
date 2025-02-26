from nlplogic.corenlp import get_phrases, search_wikipedia

def test_get_phrases():
    assert 'islamabad' in get_phrases('pakistan')

def test_search_wikipedia():
    assert 'Chinese' in search_wikipedia('china')
