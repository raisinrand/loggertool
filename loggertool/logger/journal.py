from utils import cmdline
import os

def execute(f,config):
    path = os.path.join(os.getcwd(),config["journal_path"])
    if not os.path.isfile(path):
        return
    with open(path, "r") as r:
        if r.mode != 'r':
            return
        lines = r.readlines()
        f.writelines(cmdline.indent_all(1,lines))
        f.write('\n\n')
    open(path, 'w').close()