import os



def read_syslog_messages(file_name):
    with open(file_name) as f:
        for line in f:
            if 'USB' in line:
                print line


#read_syslog_messages("messages")

def check_file_or_directory(p):
    for items in os.listdir(p):
        if os.path.isfile(items):
            print items + "is a file"
        elif os.path.isdir(items):
            print items + "is a directory"
        else:
            print items + "unknown file or directory"


def hierarchical_listing(path):
    for path, dirs, files in os.walk(path):
        print path
        for f in files:
            print f

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))

list_files("/home/sandeep/Documents/git-repo/python-infosec/module1/")