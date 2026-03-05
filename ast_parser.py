import ast

def get_ast(file_path):
    with open(file_path, "r", encoding="utf8") as f:
        tree = ast.parse(f.read())
    return ast.dump(tree)