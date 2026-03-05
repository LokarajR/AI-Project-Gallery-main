from difflib import SequenceMatcher

def calculate_similarity(ast1, ast2):

    return SequenceMatcher(None, ast1, ast2).ratio()