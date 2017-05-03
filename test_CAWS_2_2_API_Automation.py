#import requests, json, os, base64, pickle, json, pprint,  yaml , requests, urllib, urllib2 , zipfile, subprocess, time
#from html import HTML
from datetime import datetime
import CAWS_API_2_2_4 as c, pytest
from _pytest.runner import fail
import test_exp

#Today_Date = datetime.now().strftime("%Y-%m-%d")
Today_Date = datetime.now().strftime("%Y%m%d")

'''
Set : 
DUT = 1 for CAWS QA with user  amitpatel741234567890gmailcom
DUT = 2 for CAWS QA with user  amitpatel
DUT = 3 fopr CAWS PATCH QA with user  patellabs
DUT = 
'''

dnld_pcap = 0
dnld_saz = 0
dnld_payload = 0
dnld_exploit_payload = 0


@pytest.fixture(scope="module")
def start_up_config(request):
    utc_datetime = datetime.utcnow()
    exploited_nssids = "/Users/apatel/Documents/workspace/pcap_download/exploited_nssid_"+str(utc_datetime.strftime("%Y-%m-%d-%H-%M-%S"))+".txt"
    
    url = "https://data.nsslabs.com"
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    capture_dict = c.get_day_capture_dict(url, username, password, Today_Date )
    
    start_up_config_dict = {"utc_datetime" : utc_datetime , "exploited_nssids" : exploited_nssids, "capture_dict" : capture_dict}
    return start_up_config_dict

    
def test_Get_capture_count_from_Prod_CAWS_Server_10_144_192_71():
    # Testing all App server's API health.
    print "Today_Date in the unit test is :", Today_Date
    TestCase = "Get capture count from Prod CAWS Server 10.144.192.71"
    Result_capture_count = "Fail"
    Note ="None"
    url = "http://10.144.192.71:8081"
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    capture_dict = c.get_day_capture_dict(url, username, password, Today_Date )
    captureslist =  capture_dict['Captures']
    capture_count = len(captureslist)
    #capture_count = len(c.get_capture_counts( url, username, password, Today_Date ))
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
    capture_dict = c.get_day_capture_dict(url, username, password, Today_Date )
    captureslist =  capture_dict['Captures']
    capture_count = len(captureslist)
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
    capture_dict = c.get_day_capture_dict(url, username, password, Today_Date )
    captureslist =  capture_dict['Captures']
    capture_count = len(captureslist)
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
    capture_dict = c.get_day_capture_dict(url, username, password, Today_Date )
    captureslist =  capture_dict['Captures']
    capture_count = len(captureslist)
    if ( capture_count != 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(capture_count)
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert True
        #t.rows.append([TestCase, Result_capture_count, Note])
    else:
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert False
      
def test_Get_day_exploit_list_from_Prod_CAWS_Server_data_nsslabs_com(start_up_config):
# Testing all App server's API health.
    s =  start_up_config                      
    TestCase = "Get capture count from Prod CAWS Server https://data.nsslabs.com"
    Result_capture_count = "Fail"
    Note ="None"
    url = "https://data.nsslabs.com"
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    ##capture_dict = c.get_day_capture_dict(url, username, password, Today_Date )
    capture_dict = start_up_config["capture_dict"]  
    ##another_dict = c.Get_Capture_List_from_capture_dict(capture_dict, s)
    captureslist =  capture_dict['Captures']
    capture_count = len(captureslist)
    for capture in captureslist:
        print capture['NSSId']
    if ( capture_count != 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(capture_count)
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert True
        #t.rows.append([TestCase, Result_capture_count, Note])
    else:
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert False
        #t.rows.append([TestCase, Result_capture_count, Note])
        
def test_Get_day_exploits_list_with_files_list(start_up_config):
    TestCase = "Get_day_exploits_list_with_files_list from Prod CAWS Server https://data.nsslabs.com"
    Result_capture_count = "False"
    Note ="None"
    #new_dict = start_up_config["capture_dict"]
    capture_dict = start_up_config["capture_dict"]
    captureslist =  capture_dict['Captures']
    new_dict = c.Get_day_exploits_list_with_files_list(capture_dict)
#         captureslist =  capture_dict['Captures']
#         capture_count = len(captureslist)
#     for capture in captureslist:
#         print capture['NSSId']
    if ( len(new_dict) != 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(len(new_dict))
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , len(new_dict)
        assert Result_capture_count == "Pass"
    else:
        Result_capture_count = "Warning"
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , len(new_dict)
        assert Result_capture_count != "Pass"

                
               
    
        
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
