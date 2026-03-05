from ast_parser import parse_code
from similarity import calculate_similarity

file1 = "dataset/file1.py"
file2 = "dataset/file2.py"

ast1 = parse_code(file1)
ast2 = parse_code(file2)

score = calculate_similarity(ast1, ast2)

print("Similarity Score:", score)

if score > 0.8:
    print("Possible GPL Code Reuse Detected")
else:
    print("Code appears different")