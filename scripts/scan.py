#currently must reside in same location as scan.txt and will write parsedHosts.txt to same location
#nmap does not need to reside in same directory as scan.py (as long as nmap is added to path, and should be by default)
#will prompt for sudo password

import subprocess

file1 = open("scan.txt","w") #open file to write to, clear contents
file2 = open("parsedHosts.txt","w") #open file to write unique host ip's and macs

#create subprocess to run nmap. return unique active hosts
test = subprocess.Popen(["sudo","nmap","-sP","192.168.171.*"], stdout=subprocess.PIPE)
output = test.communicate()[0]

file1.write(output) #write results of nmap scan to file scan.txt
file1.close() #close file scan.txt

#parse for unique ip's
output = "Separation = \"\\t\\t\"\nIP ADDRESS"+'\t\t'+"MAC Address"+'\n'

#populate output
need_mac = False	#nmap doesn't always find MAC's
with open("scan.txt") as f:	#cycle through each line of the file containing the nmap scan results
	for line in f:
	current_line = line.split()	#split current line by white space
	if len(current_line) > 1:	#first line of scan results is empty, so skip it
		if line.split()[-1] == "seconds":	#ignore last line of scan results
			break
				elif current_line[0] == "Nmap":		#any line starting with nmap (except last) has an IP address
			if need_mac == False:		#don't need a mac address, get IP
				output += line.split()[-1] + "\t\t"
				need_mac = True
			else:				#didn't find mac for last IP; \n then get IP
				output += "\n" + line.split()[-1] + "\t\t"
				need_mac = True
		elif current_line[0] == "MAC":		#get MAC for last IP
			output += line.split()[-2] + "\n"
			need_mac = False

file2.write(output) #write unique hosts to parsedHosts.txt
file2.close() #close parsedHosts.txt