import os

#Main path
root = "F:\PyCharm Workspace\website-static-backup\mtw\Page"

for dir, subdirs, files in os.walk(root):
    if dir != root:
        old_name = os.path.join(dir, files[0])
        new_name = os.path.join(dir, "index.html")
        os.rename(old_name, new_name)