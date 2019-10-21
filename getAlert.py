import cgi
import cgitb
import mysql.connector
import json
from pprint import pprint
from datetime import datetime

cgitb.enable()
d = {}
count = 0
with open("C:\Users\Administrator\alerts.txt") as alertFile:
	for line in alertFile:
		d[count] = line
		count += 1

print('Content-Type: application/json\r\n\r\n')
try:
	print(json.dump(d))
	#print("IS THIS WORKING")
except:
	print('Except Clause')
	pass