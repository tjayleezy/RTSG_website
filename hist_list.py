import cgi
import cgitb
import mysql.connector
import json
from pprint import pprint
from datetime import datetime

lookup = {}
with open('SIDdict.csv', 'r') as f:
    for line in f:
        line = line.strip().split(',')
        lookup[line[0]] = line[1]

cnx = mysql.connector.connect(user='root', password='sqldba', host='localhost', database='openPDC')
cursor = cnx.cursor()
cgitb.enable()
data = cgi.FieldStorage()
out_list= []
d={} 
print('Content-Type: application/json\r\n\r\n')
try:
	SignalID = data.getvalue('SignalID')
	Start = data.getvalue('start')
	End = data.getvalue('end')
	startobj = datetime.strptime(Start, '%m/%d/%Y').strftime('%Y-%m-%d')
	endobj = datetime.strptime(End, '%m/%d/%Y').strftime('%Y-%m-%d')
	#print(SignalID)
	#print(lookup)
	if SignalID:
		query = '''select * from timeseriesmeasurement where SignalID='{0}'
			and timeseriesmeasurement.Timestamp between '{1}' and '{2} 23:59:59' 
			order by timeseriesmeasurement.Timestamp asc limit 1000;'''.format(SignalID, startobj, endobj)
# Execute query
		cursor.execute(query)
		d['name'] = lookup[str(SignalID)]
		d['data'] = []
		for (tsmID, signalID, timestamp, value) in cursor:	
			d['data'].append((str(timestamp),value))#(timestamp, value)
		out_list.append(d)
		cnx.commit()
		print(json.dumps(out_list))
except:
	print('Except Clause')
	pass