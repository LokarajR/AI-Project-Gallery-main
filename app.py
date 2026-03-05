from flask import Flask, render_template, request
from repo_handler import clone_repo

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])

def home():

    result=None

    if request.method=="POST":

        repo1=request.form["repo1"]
        repo2=request.form["repo2"]

        clone_repo(repo1,"repos/repo1")
        clone_repo(repo2,"repos/repo2")

        result="Repositories downloaded. AST comparison running..."

    return render_template("index.html",result=result)

if __name__=="__main__":
    app.run(debug=True)