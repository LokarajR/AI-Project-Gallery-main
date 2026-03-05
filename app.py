from flask import Flask, render_template, request
from repo_handler import clone_repo
from file_scanner import get_python_files
from ast_parser import get_ast
from similarity import calculate_similarity

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def home():

    result = None

    if request.method == "POST":

        repo1 = request.form["repo1"]
        repo2 = request.form["repo2"]

        clone_repo(repo1, "repos/repo1")
        clone_repo(repo2, "repos/repo2")

        files1 = get_python_files("repos/repo1")
        files2 = get_python_files("repos/repo2")

        scores = []

        for f1 in files1:
            for f2 in files2:

                ast1 = get_ast(f1)
                ast2 = get_ast(f2)

                score = calculate_similarity(ast1, ast2)

                scores.append(score)

        if scores:
            similarity = round(max(scores) * 100, 2)
        else:
            similarity = 0

        if similarity > 70:
            result = f"Similarity Score: {similarity}% ⚠ Possible GPL Code Reuse Detected"
        else:
            result = f"Similarity Score: {similarity}% Code appears different"

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)