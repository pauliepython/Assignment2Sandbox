#R00005740 | Paul Cronin
#Scripting for System Adminsitration | Semester 1 | Assignment2

#################################################################
# time machine python tool to allow for the checking of a       #
# selection of files. If modified within the previous 60seconds #
# the file is to be backed up to a specific location            #
#
#################################################################

import yaml
import datetime
import os


#def read_config - THIS IS THE NEXT STEP TO BE COMPLETED: DEFINE A FUNCTION TO SEARCH THE FILE LIST

#def read_records

#def was_timestamp_updated
##ifelse to be used here, if not exit

#def backup_file
##to be called from was_timestamp_updated to location possibly from config file or else define the variable/function

with open("config.dat", "r") as f:
        backup_triggers = yaml.load(f)


#Now that backup_triggers is successfully pointing towards our directory, get the timestamps for files within that directory

timestamp=os.path.getmtime ('config.dat')


print (datetime.datetime.fromtimestamp(timestamp))

#print(triggers)

##Return here to look for timestamp rather than patterns for files in keys outlined in config.dat file


#for filename in triggers.keys():
#    with open(filename, "r") as f:
#        for line in f:
#            trigger_info = triggers[filename]
#
#            if re.search(trigger_info["pattern"],line):
#                print("Match found in line {0} for pattern{1})".
#                format(line, trigger_info["pattern"]))