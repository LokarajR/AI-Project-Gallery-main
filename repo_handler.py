import os

def clone_repo(url, folder):
    os.system(f"git clone {url} {folder}")