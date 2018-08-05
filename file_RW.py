#coding=utf-8
from datetime import datetime

log_file="file_RW.log"

def read_log(log):

    """
    Open a log file and print the contents
    """
    with open(log,"r") as f:
        print(f.read())


def write_log(log,name):

    """
    add log record with timestamp
    """
    log_time = datetime.now()
    with open(log,"a") as f:
        f.writelines("Entry logged at : {} by {}\n".format(log_time,name))

if __name__ == "__main__":

    name = input("What is your name: ")
    print("Adding new log entry..")

    write_log(log_file, name)
    print("")
    print("Log file contents")
    print("-----------------")
    read_log(log_file)
