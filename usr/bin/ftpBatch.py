#!/usr/bin/env python3

"""
A program for deleting a bunch of files over ftp.
The files must be specified in a file, line by line.
Use with caution and at your own risk.
"""

import getpass
import ftplib

### Functions ###

def listDirs():
    """
    List current directory and its contents.
    """
    print("The current directory is:")
    print(ftp.pwd())
    print("The contents of this directory is:")
    ftp.dir()

def useOrChangeDir():
    """
    Use or change the current directory.
    """

    while True:
        listDirs()

        USER_DIR = input("Use this directory? (Y|N) ")

        if USER_DIR not in ("Y", "y", "N", "n"):
            print("Invalid input, try again.")
            continue
        elif USER_DIR in ("Y", "y"):
            getListandDelete()
            break
        elif USER_DIR in ("N", "n"):
            CHDIR = input("Enter directory to go to: ")
            try:
                ftp.cwd(CHDIR)
            except ftplib.all_errors:
                print("Whoops! That didn't work. Try again.")

def getListandDelete():
    """
    Get the file in which the filenames are listed.
    Read the file, and delete all files on the server which are
    listed line by line in the file.
    """

    NO_OF_DELS = 0

    while True:
        DEL_LIST = input("Enter the filename, or drag & drop the file here: ")
    
        try:
            with open(DEL_LIST) as alist:
                for line in alist:
                    DEL_RESPONSE = ftp.delete(line)
                    print(DEL_RESPONSE)
                    NO_OF_DELS += 1

            print(str(NO_OF_DELS) + " files deleted. Goodbye!")
            break
        except IOError:
            print("Could not open " + DEL_LIST + ", try again.")
            continue


### End of functions ###

### Main script ###

SERVER = input("Enter server name or ip: ")
USER = input("Enter username: ")
PASSWD = getpass.getpass()

# Try to connect using the above
print("Trying to connect...")

try:
    ftp = ftplib.FTP(SERVER)
    ftp.login(USER, PASSWD)
except ftplib.all_errors:
    print("Could not connect to server.")
    print("Exiting.")
    exit(1)

useOrChangeDir()

ftp.quit()

exit(0)

### End ###

