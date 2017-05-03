#import requests, json, os, base64, pickle, json, pprint,  yaml , requests, urllib, urllib2 , zipfile, subprocess, time
from html import HTML
from datetime import datetime
import CAWS_API_2_2_4 as c, pytest
from _pytest.runner import fail
# 
# 
#import HTML
# table_data = [
#         ['Last name',   'First name',   'Age'],
#         ['Smith',       'John',         30],
#         ['Carpenter',   'Jack',         47],
#         ['Johnson',     'Paul',         62],
#     ]
# htmlcode = HTML.table(table_data)
# print htmlcode
# 
# 
# 

#h = HTML()
#t = h.Table(header_row=['TestCase', 'Results', 'Note'])

Today_Date = datetime.now().strftime("%Y-%m-%d")
print "Todays date is:" , Today_Date

'''
Set : 
DUT = 1 for CAWS QA with user  amitpatel741234567890gmailcom
DUT = 2 for CAWS QA with user  amitpatel
DUT = 3 fopr CAWS PATCH QA with user  patellabs
DUT = 
'''
    
#start = datetime.date( year = 2017, month = 2, day = 7 )
#print "start is:" , start
#end = datetime.date( year = 2017, month = 2, day = 8 )
#print "end is:" , end

dnld_pcap = 0
dnld_saz = 0
dnld_payload = 0
dnld_exploit_payload = 0

    
def test_Get_capture_count_from_Prod_CAWS_Server_10_144_192_71():
    # Testing all App server's API health.
    TestCase = "Get capture count from Prod CAWS Server 10.144.192.71"
    Result_capture_count = "Fail"
    Note ="None"
    url = "http://10.144.192.71:8081"
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    capture_count = c.get_capture_counts( url, username, password, Today_Date )
    if ( Result_capture_count!= 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(capture_count)
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert True
        #t.rows.append([TestCase, Result_capture_count, Note])
    else:
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert False
        #t.rows.append([TestCase, Result_capture_count, Note])

                     
def test_Get_capture_count_from_Prod_CAWS_Server_10_144_192_72():
    TestCase = "Get capture count from Prod CAWS Server 10.144.192.72"
    Result_capture_count = "Fail"
    Note ="None"
    url = "http://10.144.192.72:8081"
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    capture_count = c.get_capture_counts( url, username, password, Today_Date )
    if ( Result_capture_count!= 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(capture_count)
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert True
        #t.rows.append([TestCase, Result_capture_count, Note])
    else:
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert False
        #t.rows.append([TestCase, Result_capture_count, Note])
    

def test_Get_capture_count_from_Prod_CAWS_Server_10_144_192_73():
# Testing all App server's API health.                       
    TestCase = "Get capture count from Prod CAWS Server 10.144.192.73"
    Result_capture_count = "Fail"
    Note ="None"
    url = "http://10.144.192.73:8081"
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    capture_count = c.get_capture_counts( url, username, password, Today_Date )
    if ( Result_capture_count!= 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(capture_count)
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert True
        #t.rows.append([TestCase, Result_capture_count, Note])
    else:
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert False
        #t.rows.append([TestCase, Result_capture_count, Note])

def test_Get_capture_count_from_Prod_CAWS_Server_data_nsslabs_com():
# Testing all App server's API health.                       
    TestCase = "Get capture count from Prod CAWS Server https://data.nsslabs.com"
    Result_capture_count = "Fail"
    Note ="None"
    url = "https://data.nsslabs.com"
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    capture_count = c.get_capture_counts( url, username, password, Today_Date )
    if ( Result_capture_count!= 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(capture_count)
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert True
        #t.rows.append([TestCase, Result_capture_count, Note])
    else:
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert False
        #t.rows.append([TestCase, Result_capture_count, Note])
        
    #htmlcode = str(t)
    #print htmlcode    
    

# if __name__ == "__main__":
# #Testing all App server's API health.  
#     print "Test Name ; Test Result; Note"
#     test_Get_capture_count_from_Prod_CAWS_Server_10_144_192_71
#     test_Get_capture_count_from_Prod_CAWS_Server_10_144_192_72
#     test_Get_capture_count_from_Prod_CAWS_Server_10_144_192_73()
#     test_Get_capture_count_from_Prod_CAWS_Server_data_nsslabs_com()
    
# 
# # Testing all App server's API health.
#     TestCase = "Get capture count from Prod CAWS Server 10.144.192.71"
#     Result_capture_count = "Fail"
#     Note ="None"
#     url = "http://10.144.192.71:8081"
#     username = "patellabs"
#     password = "2992A2D48ED942A2A3596D762A4415BC"
#     capture_count = c.get_capture_counts( url, username, password, Today_Date )
#     if ( Result_capture_count!= 0):
#         Result_capture_count = "Pass"
#         Note = "Counts count is  :" + str(capture_count)
#         print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
#         #t.rows.append([TestCase, Result_capture_count, Note])
#     else:
#         print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
#         #t.rows.append([TestCase, Result_capture_count, Note])
#         
# 
    
    print "program is done." 
                       
                       


 