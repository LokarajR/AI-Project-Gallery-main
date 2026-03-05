import os
import shutil
import stat

def remove_readonly(func, path, excinfo):
    os.chmod(path, stat.S_IWRITE)
    func(path)

def clone_repo(url, folder):

    if os.path.exists(folder):
        shutil.rmtree(folder, onerror=remove_readonly)

    os.system(f"git clone {url} {folder}")