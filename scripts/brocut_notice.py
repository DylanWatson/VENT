#there is currently an issue with trying to run this script for real-time
#information gathering. bro keeps logs in a folder called current for x amount
#of time, then zips them with gunzip into a logs folder and clears current.
#next step is to check for presence of notice.log in current before running bro-cut.
#afterwards, determining when current logs are zipped will allow for
#some more automation with this script.
#for the time being, this script assumes notice.log exists.
#on line 16, change "SET_YOUR_PATH_HERE" to the preferred location of
#the newly cut notice.log (now called cut_notice.log)
#on line 26, change "SET_YOUR_PATH_HERE" to the location of the desired
#notice.log file.

import subprocess

#create and open file to store pertinent info from notice.log
file_cut_notice = open("/SET_YOUR_PATH_HERE/cut_notice.txt","w")

#setting up labels for info in cut_notice.txt
output = "Time\t\t\t\tSource IP\tPort\tDestination IP\tPort\tProto\tNote\t\t\t\tMessage\n"

#for remaining code before writing file, terminal command would look as follows:
#cat notice.log | bro-cut -d ts src id.orig_p dest p proto note
#using subprocess, this must be done in two statements, as seen below

#as long as cat is in your path, full path below is not necessary
cat = subprocess.Popen(["/bin/cat","/SET_YOUR_PATH_HERE/notice.log"], stdout=subprocess.PIPE)
#next line was just for testing automatically generated logs
#cat = subprocess.Popen(["sudo","/bin/cat","/nsm/bro/logs/current/notice.log"], stdout=subprocess.PIPE)

#running the output from cat as input for bro-cut then appending that result to output
brocut = subprocess.Popen(["bro-cut","-d","ts","src","id.orig_p","dst","p","proto","note","msg"], stdin=cat.stdout, stdout=subprocess.PIPE)
output += brocut.communicate()[0]

#write and close file_cut_notice
file_cut_notice.write(output)
file_cut_notice.close()