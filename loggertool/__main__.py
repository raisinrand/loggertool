import argparse
import datetime
import os
import logger
import config
import dateutil.parser

def main():
    parser = argparse.ArgumentParser(description="A tool for automating creation of daily log files to track various metrics.")
    parser.add_argument("command", default="log", nargs="?", choices=["log","parse","list"], help="todo")
    parser.add_argument("date", help="date to generate log for")
    args = parser.parse_args()

    if(args.command == "log"):
        c = config.get_config()
        date = dateutil.parser.parse(args.date)
        logger.log(date,c)
    elif(args.command == "parse"):
        pass
    # elif(args.command == "list"):
    #     config = settings.get_settings()
    #     habitlist.list(config["list_path"])

main()
