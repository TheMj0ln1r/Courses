#!/usr/bin/env python3
import re
import csv
import operator
import sys
error = {}
per_user = {}

errorfile = "error_message.csv"
userfile = "user_statistics.csv"

with open("syslog.log","r") as file:
	for line in file:
        result = re.search(r"ticky: ([\w+]*):? ([\w' ]*) [\[[0-9#]*\]?]? ?\((.*)\)$", log)
		if result.group(2) not in error.keys():
			error[result.group(3)] = 0
		error[result.group(3)] += 1

		if result.group(3) not in per_user.keys():
			per_user[result.group(3)] = {}
			per_user[result.group(3)]["INFO"] = 0
			per_user[result.group(3)]["ERROR"] = 0
		if result.group(1) == "INFO":
			per_user[result.group(3)]["INFO"] +=1
		elif result.group(1) == "ERROR":
			per_user[result.group(3)]["ERROR"] +=1

error = sorted(error.items(), key = operator.itemgetter(1),reverse = True)
per_user = sorted(per_user.items())

error.insert(0,("Error","Count"))

f = open(errorfile,"w")
for e in error:
	a,b = e
	f.write(str(a)+","+str(b)+"\n")
f.close()

f = open(userfile,"w")

f.write("Username,INFO,ERROR\n")
for stats in per_user:
	a,b = stats
	f.write(str(a)+","+str(b["INFO"])+","+str(b["ERROR"])+"\n")