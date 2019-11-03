# Importing required external packages:
import os, fnmatch

# Setting File Upload Extension types:
ALLOWED_EXTENSIONS = set(["csv", "txt", "tsv", "xlsx"])


# Locates list of file in a directory as per matching pattern:
def find_local_file(pattern, path):
    """
    Use Case: find_local_file("acer18__amz__orders__*","amz_uploaded_files/") --> Returns either an empty List like [] or with all available item/file paths like ['amz_uploaded_files/acer18__amz__orders__orders.txt']
    """
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


# Checks file extension for dataset being uploaded:
def allowed_file(filename):
    """
    DOCSTRING: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
    """
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
