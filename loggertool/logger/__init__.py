import datetime
import os
from utils import cmdline
from . import journal
from . import metrics
from . import tasklist

# latest time in am hours to count as the previous day (for late night logging)
PREVDAY_TIME = datetime.time(4,30)

# get the appropriate subpath for a log file based on the given date
def get_logfile_subpath(date):
    if date.time() < PREVDAY_TIME:
        date = date - datetime.timedelta(days=1)
    return os.path.join(date.strftime("%Y"),str(date.month),"{}.txt".format(date.day))

# prompt the user for information about their day and produce a log file
def log(date, config):
    dir = config["dir"]

    path = os.path.normpath(os.path.join(dir,get_logfile_subpath(date)))
    subdir = os.path.dirname(path)
    if not os.path.exists(subdir):
        os.makedirs(subdir)

    with open(path, "w") as f:

        # journal section
        # heading(f,"")
        journal.execute(f,config)
        
        # metrics section
        heading(f,"metrics")
        metrics.execute(f)

        # tasklist section
        heading(f,"tasks")
        tasklist.execute(f,config)
        
        print("Wrote new log file at {}".format(path))

def heading(f,s):
    f.write(s + ":" + cmdline.paragraph)