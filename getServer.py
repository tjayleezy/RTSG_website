import cgi
import cgitb
import json
from pprint import pprint
from datetime import datetime

cgitb.enable()
data = cgi.FieldStorage()
out_list= []
d={} 
print('Content-Type: application/json\r\n\r\n')
try:
	print(data.getlist("anom"))

except:
	print('Except Clause')
	pass