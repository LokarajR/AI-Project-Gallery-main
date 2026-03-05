import ast

def get_ast(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            tree = ast.parse(f.read())
            return ast.dump(tree)
    except:
        return ""