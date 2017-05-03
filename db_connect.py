server = "10.144.194.82"
user = "baitnetuser"
password = "CAWSW3b"
'''
from os import getenv
import pymssql



conn = pymssql.connect(server, user, password, "BaitNETWeb2015")
cursor = conn.cursor()
'''

from sqlalchemy import create_engine
import datetime, time
#engine = create_engine('mssql+pymssql://baitnetuser:CAWSW3b@10.144.194.80:1433')

# query = "SELECT TOP (250) [Id] \
#       ,[ResponseId] \
#       ,[SourceUrl] \
#       ,[UTCSubmissionDate] \
#       ,[State] \
#       ,[NSSId] \
#       ,[UTCResultDate] \
#       FROM [BaitNETWebBETA].[dbo].[UserSourceUrl] \
#       order by id desc" 
query1 = "select count(*) as count from [ExploitCapture].[dbo].[ReversingLabsAnalysis]"
query2 = "select count(*) as count from [ExploitCapture].[dbo].[ReversingLabsQueue]"

 # --where state like '%2%' 
 # --where responseid like '%8411DFB97D9B4443BE20C8AA0DDBED7E%'
    
#rows = conn.execute("select name FROM sys.databases;")

for i in range(100):
    engine = create_engine('mssql+pymssql://baitnettester:baitnet@10.144.194.79:1433')
    conn = engine.connect()
    rows1 = conn.execute(query1)
    for row in rows1:
        #print(row["ResponseId"] , )
        count_processed = row[0]
        #print row[0]
        
    rows2 = conn.execute(query2)
    for row in rows2:
        #print(row["ResponseId"] , )
        count_in_queue = row[0]
        #print row[0]
    
    query_time = datetime.datetime.now()
        
    print query_time , ";", count_processed, ";" , count_in_queue
    file_str = str(query_time) + ";" + str(count_processed) + ";" + str(count_in_queue)
    target_url = open("/Users/apatel/Documents/workspace/reversinglab_results.txt", 'a')
    target_url.write(file_str)
    target_url.write("\n")
    target_url.close()
    conn.close()
    time.sleep (1800)


#441
#9268   