import cgi
import cgitb
import mysql.connector
import json
from pprint import pprint

cnx = mysql.connector.connect(user='root', password='sqldba', host='localhost', database='openPDC')

cursor = cnx.cursor()

cgitb.enable()
hist=[]
data = cgi.FieldStorage()
SID = ''
print('Content-Type: text/plain\r\n\r\n')
if data.getvalue('thing'):
	SID=data.getvalue('thing')
else:
	print('no data')
if SID:
	for x in range(2):
		d = {}
		d["name"] = "{}".format(x)
		d["age"] = 3
		hist.append(d)
	print(json.dumps(hist))
