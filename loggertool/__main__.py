import argparse
import datetime
import os
import logger
import config

def main():
    parser = argparse.ArgumentParser(description="A tool for automating creation of daily log files to track various metrics.")
    parser.add_argument("command", default="log", nargs="?", choices=["log","parse","list"], help="todo")#TODO:change this to use subcommands
    args = parser.parse_args()

    if(args.command == "log"):
        c = config.get_config()
        date = datetime.datetime.now()
        logger.log(date,c)
    elif(args.command == "parse"):
        pass
    # elif(args.command == "list"):
    #     config = settings.get_settings()
    #     habitlist.list(config["list_path"])

main()