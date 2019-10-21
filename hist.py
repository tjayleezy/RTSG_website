import cgi
import cgitb
import mysql.connector
import json
from pprint import pprint

cnx = mysql.connector.connect(user='root', password='sqldba', host='localhost', database='openPDC')

cursor = cnx.cursor()

cgitb.enable()
hist={} 
data = cgi.FieldStorage()
print('Content-Type: text/plain\r\n\r\n')
if data.getvalue('SignalID'): #SignalID is sent over the network
#if True:
# Build the query using the sent SignalID 
	SID=data.getvalue('SignalID')
	#SID = 'b8413f53-b191-11e6-a0b8-001c23c619e5'
	query = '''select * from timeseriesmeasurement where SignalID='{0}'
			and timeseriesmeasurement.Timestamp between '2017-03-07' and '2017-03-08 23:59:59' 
			order by timeseriesmeasurement.Timestamp asc limit 10000;'''.format(SID)
# Execute query
	print (query) 
	cursor.execute(query)
	for (tsmID, signalID, timestamp, value) in cursor:
		hist[str(timestamp)]=value
	cnx.commit()
	# Export to JSON
	pprint(json.dumps(hist))
