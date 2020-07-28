import os

DEFAULT_CONFIG = {
    "dir": "log",
    "task_path": "log{}done.txt".format(os.sep),
    "journal_path": "journal.txt",
    "list_path": "habit-list.txt"
}

def get_config():
    # path = os.path.abspath(__file__)
    # dir_path = os.path.dirname(path)
    # if os.path.exists(os.path.join(dir_path,".config")):
    #     #do stuff
    return DEFAULT_CONFIG