#!/usr/bin/env python
#coding:utf8

import os
import sys

file = open(sys.argv[1],"r")

for line in file:
	url = line[0:-1]
	print "*******************8"
	command = "sqlmap.py -u " + url + " --random-agent -f --batch --answer=\"extending=N,follow=N,keep=N,exploit=n\""
	print "Exec : " + command
	os.system(command)