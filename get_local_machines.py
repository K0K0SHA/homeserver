#!/usr/bin/python3
# filename: get_local_machines.py
# purpose: uses nmap to scan for devices on the LAN
# written by K0K0$H@
# github page: https://github.com/K0K0SHA/homeserver/
# version 0.1
# v0.1 notes: unstable; no guard rails or dependency checks. Function incomplete. May be blocked through firewalls and IDS.
# use NMap Cookbook and notes from it
# Nmap downloaded from: nmap.org
# from miscX.py in boilerplates repo
######################################################
import os	# for terminal execution and file ops
import platform # for OS identification
import shutil   # for checking installation

# class variable declaration area
verbosity = True # verbose output for verbosity() and verbose_echo()
# executes a command verbosely (shows command)
def verbosity(cmd):
    if(self.verbosity):
        print("Executing verbose:\n")
        print(cmd)
        returncode = safe_execute(commandstr)
	return returncode
    else:
	return -1 # verbosity disabled, stay mute 

# combines os.system() with Python's exception
# emulates a terminal command
def safe_execute(commandstr):
    try:
        cmd = commandstr
	exitcode = os.system(cmd)
	return exitcode
    except Exception as E:
	print("ERROR IN safe_execute(commandstr)\n")
	print(E)
	return 1

# function name: get_input()
# safe(r) way to get input from user
# allows no input
def get_input(prompt):
    try:
        if prompt == None:
            prompt = "AWAITING USER INPUT, INPUT A STRING!\n"
	    inp = input(prompt)
	return inp
    except Exception as E:
        print(E)
        return None

# asks user to confirm with y/n, case insensitive using casefold()
def user_confirm(prompt):
    try:
        i = get_input("PLEASE CONFIRM (Y/N)\n")
        run = True # classic n00b infinite runLoop
        while (run):
            if (i.casefold()=='y'):
                verbose_echo("CONFIRMED!")
                return True
            elif (i.casefold()=='n'):
                verbose_echo("DENIED!")
                return False
    except Exception as E:
        print("ERROR in user_confirm(), returning False!\n")
        print(E)
        return False

# function name: check_install()
# Boolean that checks if a program is installed
# To return the directory of the Python exe, run get_install_dir()
def check_install(program):
    try:
        if (program==None):
            print("Internal ERROR, no argument supplied to check_install. Returning False\n")
            return False
        else:
            if (shutil.which(program)!=None):
                print("Program Found:")
                print(program)
                return True
            else:
                print("Dependency not found:\n")
                print(program)				      
                return False
        return False
    except Exception as E:
        print("ERROR")
  print(E)
			  return False

# FILE OPERATION FUNCTIONS
#####
# function name: file_exists()
# returns True if file exists in current directory, false if not
def file_exists(filepath):
    try:
    fp = filepath
    if (os.exists(filepath)):
        verbose("File exists!")
        return True
    else:
        return False
    except Exception as E:
        print("Error")
        print(E)
        return False

# takes a list file, returns list object
def read_file_lines_as_list(filepath):
    try:
        fp = filepath
        if (file_exists(fp) == False):
            print("error, file does not exist:")
            print(fp)
            return None # error condition
        myfile = open(filepath, 'rw')
        Lines = myfile.readlines()
        return Lines
    except Exception as E:
        print(E)
        return None # error condition
