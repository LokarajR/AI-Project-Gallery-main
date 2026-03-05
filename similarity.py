from difflib import SequenceMatcher

def similarity_score(ast1, ast2):
    return SequenceMatcher(None, ast1, ast2).ratio()