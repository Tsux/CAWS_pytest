


import os, base64, pickle, json, pprint,  yaml , requests, urllib, urllib2 , zipfile, subprocess, time 
#from robot.api.deco import keyword
#from datetime import date
import datetime

try:
    from urllib.request import Request, urlopen, HTTPError  # Python 3
except:
    from urllib2 import Request, urlopen, HTTPError  # Python 2
    
'''
Set : 
DUT = 1 for CAWS QA with user  amitpatel741234567890gmailcom
DUT = 2 for CAWS QA with user  amitpatel
DUT = 3 fopr CAWS PATCH QA with user  patellabs
DUT = 
'''

Dut = 0    
#Dut = 4
#start = datetime.date( year = 2017, month = 2, day = 7 )
#print "start is:" , start
#end = datetime.date( year = 2017, month = 2, day = 8 )
#print "end is:" , end

dnld_pcap = 0
dnld_saz = 0
dnld_payload = 0
dnld_exploit_payload = 0



    
if Dut == 1:
    #cawsqa -- user/password
    username = "amitpatel741234567890gmailcom"
    password = "D7A37396AB0C40CBA489D88316D727F3"
    url = "http://apiqa.qa.colo1.nsslabs.com"

if Dut == 2:
    #cawsqa -- user/password
    username = "amitpatel"
    password = "BB8FA646126D4C8991C6088E1E60E684"
    url = "http://apiqa.qa.colo1.nsslabs.com"

if Dut == 3:
    #caws qa patch
    username = "patellabs"
    password = "240DA1A652B44014993D59986156DE47"
    url = "http://apiqa-patch.qa.colo1.nsslabs.com"


if Dut == 4:
    #caws qa patch
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    url = "http://data.nsslabs.com"
    #url = "http://10.144.192.72:8081"
    
if Dut == 5:
    #caws Beta 
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    #url = "http://10.144.192.60:82"
    url = "https://apibeta.nsslabs.com"

 


'''
f = open("response_a.txt","w")
pickle.dump(a, f)
f.close()

f = open("response_data.txt","w")
pickle.dump(data, f)
f.close()


print(data)
print "now it will print dictionary \n"

for k,v in data.items():
    print k, 'corresponds to', v
    
for k in data['Captures']:
    print k
'''
DATE_FORMAT = '%Y%m%d'

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input
    
def get_capture_counts(url, username, password, day_str ):
    print "day string is:" , day_str
    #print datetime.date.today() - datetime.timedelta(days=i)
    base64string = base64.b64encode('%s:%s' % (username, password))

#q = Request('http://apiqa-patch.qa.colo1.nsslabs.com/Captures/List')
    #q = Request(url+'/Captures/List?DetectionDate=20161128')
    #===========================================================================
    # if len(q) > 0:
    #     q = '%s?%s' % (url, query_string)
    # else:
    #     print " Request length is zero."
    #===========================================================================
    q = Request(url+'/Captures/List?DetectionDate='+day_str)
    print "req is :",url,'/Captures/List?DetectionDate=',day_str,":"
    #q = Request(url+'/files/32CC69ECEDE54C689D5BCF755A48144C')    
    #q = Request('http://apiqa.qa.colo1.nsslabs.com/Captures/List')
    #q = Request('http://apiqa-patch.qa.colo1.nsslabs.com/statistics/global?startDate=2016-11-01&endDate=2016-1201')
    q.add_header("Authorization", "Basic %s" % base64string)
    q.add_header('Accept-encoding', 'gzip')
    q.add_header('Connection',"keep-alive")
    q.add_header('context','ssl._create_unverified_context()')
    #q.add_unredirected_header('User-Agent', 'Custom User-Agent') 
    q.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')#q.add_header('User-agent', 'Mozilla/5.0')
    q.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
    #q.add_headers = ('User-Agent', 'Mozilla/5.0')
    
    #a = {}
    #a = requests.get('http://apiqa.qa.colo1.nsslabs.com/Captures/List', auth=('amitpatel741234567890gmailcom', 'D7A37396AB0C40CBA489D88316D727F3'))
    try:
        a = urlopen(q).read()
        #cookie = a.getheader('Set-Cookie')
        #print "Cookie is :" , cookie
    #except IOError as ioerr:
    except HTTPError, err:
        try:
            if err.code == 404:
                #print('Error in opening url is -- for -- amit --: %s' % err)
                #a = urlopen(q).read()
                #a.close()
                request = urllib2.Request(url)
                sock=urllib2.urlopen(request)
                cookies=sock.info()['Set-Cookie']
                content=sock.read()
                sock.close()
                print (cookies, content)
                #FIXME - [Tsune] uncommented cookie value from Request header (my guess)
                cookie=request.getheader['Set-Cookie']
                print "Cookie is :" , cookie
                # top is for obtaining the cookie via the info get.
                #req = urllib2.Request(url)#send the new url with the cookie.
                #req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                q.add_header('Cookie',cookie)
                a = urlopen(q).read()
                #FIXME - [Tsune] changed ioerr to err available err object (my guess)
                print('Error in opening url is -- for -- amit --: %s' % err)
            else:
                raise
        except:
                raise    
        
    data  = {}
    data = json.loads(a)
    data = byteify(data)
    #json.dump(data, open('/Users/apatel/Documents/workspace/pcap_download/'+keys+'_capture_detail.txt','w'))
    
    #data = yaml.safe_load(json.loads(a))
    #pprint.pprint(data)
    Captureslist =  data['Captures']
    print "Date ;", day_str , " Total Number of Captures are ; " , len(Captureslist)
    return (Captureslist)
    #return len(Captureslist)

def get_day_capture_dict(url, username, password, day_str ):
    print "day string is:" , day_str
    #print datetime.date.today() - datetime.timedelta(days=i)
    base64string = base64.b64encode('%s:%s' % (username, password))

#q = Request('http://apiqa-patch.qa.colo1.nsslabs.com/Captures/List')
    #q = Request(url+'/Captures/List?DetectionDate=20161128')
    #===========================================================================
    # if len(q) > 0:
    #     q = '%s?%s' % (url, query_string)
    # else:
    #     print " Request length is zero."
    #===========================================================================
    q = Request(url+'/Captures/List?DetectionDate='+day_str)
    print "req is :",url,'/Captures/List?DetectionDate=',day_str,":"
    #q = Request(url+'/files/32CC69ECEDE54C689D5BCF755A48144C')    
    #q = Request('http://apiqa.qa.colo1.nsslabs.com/Captures/List')
    #q = Request('http://apiqa-patch.qa.colo1.nsslabs.com/statistics/global?startDate=2016-11-01&endDate=2016-1201')
    q.add_header("Authorization", "Basic %s" % base64string)
    q.add_header('Accept-encoding', 'gzip')
    q.add_header('Connection',"keep-alive")
    q.add_header('context','ssl._create_unverified_context()')
    #q.add_unredirected_header('User-Agent', 'Custom User-Agent') 
    q.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')#q.add_header('User-agent', 'Mozilla/5.0')
    q.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
    #q.add_headers = ('User-Agent', 'Mozilla/5.0')
    
    #a = {}
    #a = requests.get('http://apiqa.qa.colo1.nsslabs.com/Captures/List', auth=('amitpatel741234567890gmailcom', 'D7A37396AB0C40CBA489D88316D727F3'))
    try:
        a = urlopen(q).read()
        #cookie = a.getheader('Set-Cookie')
        #print "Cookie is :" , cookie
    #except IOError as ioerr:
    except HTTPError, err:
        try:
            if err.code == 404:
                #print('Error in opening url is -- for -- amit --: %s' % err)
                #a = urlopen(q).read()
                #a.close()
                request = urllib2.Request(url)
                sock=urllib2.urlopen(request)
                cookies=sock.info()['Set-Cookie']
                content=sock.read()
                sock.close()
                print (cookies, content)
                #FIXME - [Tsune] uncommented cookie value from Request header (my guess)
                cookie=request.getheader['Set-Cookie']
                print "Cookie is :" , cookie
                # top is for obtaining the cookie via the info get.
                #req = urllib2.Request(url)#send the new url with the cookie.
                #req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
                q.add_header('Cookie',cookie)
                a = urlopen(q).read()
                #FIXME - [Tsune] changed ioerr to err available err object (my guess)
                print('Error in opening url is -- for -- amit --: %s' % err)
            else:
                raise
        except:
                raise    
        
    capture_dict = {}
    capture_dict = json.loads(a)
    capture_dict = byteify(capture_dict)
    return (capture_dict)

#     #json.dump(data, open('/Users/apatel/Documents/workspace/pcap_download/'+keys+'_capture_detail.txt','w'))
#     
#     #data = yaml.safe_load(json.loads(a))
#     #pprint.pprint(data)
#     Captureslist =  data['Captures']
#     print "Date ;", day_str , " Total Number of Captures are ; " , len(Captureslist)
#     return (Captureslist)
#     #return len(Captureslist)



#def Get_Capture_List(Captureslist):
def Get_Capture_List_from_capture_dict(capture_dict, start_up_config_dict):
    s = start_up_config_dict
    capture_dict = capture_dict
    print "startup config file exploited_nssids location is :" , s["exploited_nssids"]
# #     for each_capture in Captureslist:
# #         #print "capture is : " , each_capture, "\n"
# #         #print "nssid is:" , each_capture['NSSId']
# #         name = each_capture['NSSId'] 
# #         capture_dict[name] = each_capture
#        pprint.pprint (capture_dict[name])
    #print "NSSId ; Platform ; Browser, InstalledApplication; TargetedApplication ; SourceUri ; network connection "
    target_nssids = open(s["exploited_nssids"], 'w') 
    for keys in capture_dict:
        #print keys, ";" ,capture_dict[keys]['NetworkConnections']
        
        #if (len(capture_dict[keys]['NetworkConnections']) != 0):
        #    print "nssid is :" , keys, ";" ,capture_dict[keys]['NetworkConnections']
        #   print keys, ";" , capture_dict[keys]['Platform'] , ";" , capture_dict[keys]['Browser'] , ";" , capture_dict[keys]['InstalledApplication'] , ";" , capture_dict[keys]['TargetedApplication'] , ";" , capture_dict[keys]['SourceUri'] , ";" , capture_dict[keys]['NetworkConnections']
        #print keys, ";" , capture_dict[keys]['Platform'] , ";" , capture_dict[keys]['Browser'] , ";" , capture_dict[keys]['InstalledApplication'] , ";" , capture_dict[keys]['TargetedApplication'] , ";" , capture_dict[keys]['SourceUri'] , ";" , capture_dict[keys]['NetworkConnections']
        #print keys, ";" , capture_dict[keys]['Platform'] , ";" , capture_dict[keys]['Browser'] , ";" , capture_dict[keys]['InstalledApplication'] , ";" , capture_dict[keys]['TargetedApplication'] , ";" , capture_dict[keys]['SourceUri'] , ";" , capture_dict[keys]['NetworkConnections']    
        #print capture_dict[keys]['SourceUri']
        #capture_text_file = open('/Users/apatel/Documents/workspace/pcap_download/'+keys+'_capture_detail.txt', 'w')
        json.dump(capture_dict[keys], open('/Users/apatel/Documents/workspace/pcap_download/'+keys+'_capture_detail.txt','w'))
        #capture_text_file.write(str(capture_dict[keys]))
        #capture_text_file.close()
        if (dnld_pcap == 1):
            download_pcap_file( url, username, password, keys )
        if (dnld_saz == 1):
            download_saz_file( url, username, password, keys )
        #if ((len(capture_dict[keys]['Files']) != 0) and (len(capture_dict[keys]['Files']) < 3 )):
        if (dnld_payload == 1):
            #download_saz_file( url, username, password, keys )
            if (len(capture_dict[keys]['Files']) != 0):
            #if (len(capture_dict[keys]['Files']) > 2):
                bad_nssids = ['NSS-2017-27ZRFD', 'NSS-2017-282NXB' , 'NSS-2017-27ZQ30' , 'NSS-2017-280DCG' ,'NSS-2017-2808W3' 
                              'NSS-2017-280F6K' , 'NSS-2017-27ZNR0', 'NSS-2017-2808W3', 'NSS-2017-280F6K', 'NSS-2017-27ZM5X',
                              'NSS-2017-27ZNR0', 'NSS-2017-27ZNR0' , 'NSS-2017-27ZSZ4', 'NSS-2017-27ZDXG', 'NSS-2017-27ZKKT' ,
                              'NSS-2017-280DGP', ]
                if (keys in bad_nssids):
                    print ">>>>>>>>>>>>>> this was a problem NSSiD in file list <<<<<<<<<<<<<<<<<<"
                #    continue 
                print "total files are : " , str(len(capture_dict[keys]['Files']))
                print "nssid is :" , keys, "files are ;" ,capture_dict[keys]['Files']
                #pprint.pprint (capture_dict[keys])
                for files in capture_dict[keys]['Files']:
                    print "File : "  , files , ": for nssid is :" , keys
                    print "file came back as :" , type(files)
                    print "file name came back as :" , files['Name']
                    print "file hash back as :" , files['Md5Hash'],":"
                    #download_payload_file( url, username, password, keys , files['Md5Hash'],files['Name']  )
                    
                #for filenamekeys in files['Md5Hash']:
                    #print "file name is :", files['Name'] , filenamekeys
#                 print "File name is :" , capture_dict[keys][files]['Name']
#                 print "and hash is :", capture_dict[keys][files]['Md5Hash']
                #/Captures/Files/DetectedFile/{hash}
        #pprint.pprint (capture_dict[keys])
        #if (len(capture_dict[keys]['IndicatorsOfAttack']['Processes']) == 0):
            #print "Nssid :" , keys ,"has no processes"
            #pprint.pprint (capture_dict[keys])
            #print "nssid is :" , keys, ";" ,capture_dict[keys]['NetworkConnections']
            #print "No processes for: " , keys, ";" , capture_dict[keys]['Platform'] , ";" , capture_dict[keys]['Browser'] , ";" , capture_dict[keys]['InstalledApplication'] , ";" , capture_dict[keys]['TargetedApplication'] , ";" , capture_dict[keys]['SourceUri'] , ";" , capture_dict[keys]['NetworkConnections']

                    
                    
        target_nssids.write(keys)
        target_nssids.write("\n")
        #=======================================================================
        # 
        # print "now it will work on the saz file."
        # process = subprocess.Popen("/usr/local/bin/python3 /Users/apatel/Documents/workspace/test.py " + keys, shell=True, stdout=subprocess.PIPE)
        # process.wait()
        # print "process return code is : " , process.returncode
        #=======================================================================
    

    
    
    target_nssids.close()
    return (capture_dict)

def Get_day_exploits_list_with_files_list(capture_dict):
    #pprint.pprint(capture_dict)
    dict_with_files = {}
    captureslist =  capture_dict['Captures']
    capture_count = len(captureslist)
    print "Capture count is :", capture_count
    for capture in captureslist:
        if (len(capture['Files']) != 0):
        #if (len(capture_dict[keys]['Files']) > 2):
            print "total files for :",capture['NSSId'] ,":are : " , str(len(capture['Files']))
            print "List of files for :",capture['NSSId'] ,":are :" ,capture['Files']
            #pprint.pprint (capture_dict[keys])
            for files in capture['Files']:
                print "File : "  , files , ": for nssid is :" , capture['NSSId']
                print "file came back as :" , type(files)
                print "file name came back as :" , files['Name']
                print "file hash back as :" , files['Md5Hash'],":"
            #FIXME - [Tsune] Getting '+' operand not applicable for dict & dict, so I took dict_with_files away, not affections seen since dict is empty until this point
            dict_with_files = {capture['NSSId'] : capture['Files']}
            print "nss id is :" , capture['NSSId'] , ": Total files for the NSSid is :" , len(capture['Files']) , "Files list is:" , capture['Files']
        
        else:
            print "nss id is :" ,capture['NSSId'], ": Total files for the NSSid is :" , len(capture['Files']) , "NO Files for NSS id"
                                                                                            
    return dict_with_files
    
    
# new_dict = Get_day_exploits_list_with_files_list(capture_dict)
# for keys in new_dict:
#             print "total files are : " , str(len(new_dict[keys]['Files']))




def download_pcap_file( url, username, password, nssid ):
    #print datetime.date.today() - datetime.timedelta(days=i)
    base64string = base64.b64encode('%s:%s' % (username, password))
    NSSid = nssid
    url_pcap_download = url +"/Captures/Files/Pcap/"+nssid
    url_saz_download = url +"/Captures/Files/Saz/"+nssid
    q = Request(url_pcap_download)
    q.add_header("Authorization", "Basic %s" % base64string)
    try:
        a = urlopen(q).read()
    #except IOError as ioerr:
    except HTTPError, err:
        try:
            if err.code == 404:
                request = urllib2.Request(url)
                sock=urllib2.urlopen(request)
                cookies=sock.info()['Set-Cookie']
                content=sock.read()
                sock.close()
                print (cookies, content)
                #FIXME - [Tsune] uncommented cookie value from Request header (my guess)
                cookie=request.getheader['Set-Cookie']
                print "Cookie is :" , cookie
                q.add_header('Cookie',cookie)
                a = urlopen(q).read()
                #FIXME - [Tsune] changed ioerr to err available err object (my guess)
                print('Error in opening url is -- for -- amit --: %s' % err)
            else:
                raise
        except:
                raise    
        
    data  = {}
    data = json.loads(a)
    data = byteify(data)
    zip_file_content = base64.decodestring(data['Binary'])
    f = open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.zip', 'wb')
    f.write(zip_file_content) #TypeError: a bytes-like object is required, not 'str' 
    f.close()
    zip_ref = zipfile.ZipFile('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.zip', 'r')
    zip_ref.extractall('/Users/apatel/Documents/workspace/pcap_download/'+nssid)
    zip_ref.close()
    os.rename('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'/PCAPTraffic.pcap', '/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.pcap')
    os.remove('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.zip') 
    os.rmdir('/Users/apatel/Documents/workspace/pcap_download/'+nssid)

    #data = yaml.safe_load(json.loads(a))
    #pprint.pprint(data)
    #Captureslist =  data['Captures']
    #print "Date ;", date, " Total Number of Captures are ; " , len(Captureslist)

    return ()

def download_saz_file( url, username, password, nssid ):
    #print datetime.date.today() - datetime.timedelta(days=i)
    base64string = base64.b64encode('%s:%s' % (username, password))
    NSSid = nssid
    url_pcap_download = url +"/Captures/Files/Saz/"+nssid
    q = Request(url_pcap_download)
    q.add_header("Authorization", "Basic %s" % base64string)
    try:
        a = urlopen(q).read()
    #except IOError as ioerr:
    except HTTPError, err:
        try:
            if err.code == 404:
                request = urllib2.Request(url)
                sock=urllib2.urlopen(request)
                cookies=sock.info()['Set-Cookie']
                content=sock.read()
                sock.close()
                print (cookies, content)
                #cookie=req.getheader['Set-Cookie']
                print "Cookie is :" , cookies
                q.add_header('Cookie',cookies)
                a = urlopen(q).read()
                #FIXME - [Tsune] changed ioerr to err available err object (my guess)
                print('Error in opening url is -- for -- amit --: %s' % err)
            else:
                raise
        except:
                raise    
        
    data  = {}
    data = json.loads(a)
    data = byteify(data)
    zip_file_content = base64.decodestring(data['Binary'])
    f = open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.saz', 'wb')
    f.write(zip_file_content) #TypeError: a bytes-like object is required, not 'str' 
    f.close()
    #zip_ref = zipfile.ZipFile('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.zip', 'r')
    #zip_ref.extractall('/Users/apatel/Documents/workspace/pcap_download/'+nssid)
    #zip_ref.close()
    #os.rename('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'/PCAPTraffic.pcap', '/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.pcap')
    #os.remove('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.zip') 
    #os.rmdir('/Users/apatel/Documents/workspace/pcap_download/'+nssid)
    

    #data = yaml.safe_load(json.loads(a))
    #pprint.pprint(data)
    #Captureslist =  data['Captures']
    #print "Date ;", date, " Total Number of Captures are ; " , len(Captureslist)
    return ()

#/Captures/Files/DetectedFile/
#download_payload_file( url, username, password, files['Md5Hash'],files['Name']  )
def download_payload_file( url, username, password, nssid, Md5Hash,filename   ):
    #print datetime.date.today() - datetime.timedelta(days=i)
    base64string = base64.b64encode('%s:%s' % (username, password))
    #NSSid = nssid
    #Md5Hash = Md5Hash
    #filename = filename
    url_payload_download = url +"/Captures/Files/DetectedFile/"+Md5Hash
    q = Request(url_payload_download)
    q.add_header("Authorization", "Basic %s" % base64string)
    try:
        a = urlopen(q).read()
    #except IOError as ioerr:
    except HTTPError, err:
        try:
            if err.code == 404:
                request = urllib2.Request(url)
                sock=urllib2.urlopen(request)
                cookies=sock.info()['Set-Cookie']
                content=sock.read()
                sock.close()
                print (cookies, content)
                #FIXME - [Tsune] uncommented cookie value from Request header (my guess)
                cookie=request.getheader['Set-Cookie']
                print "Cookie is :" , cookie
                q.add_header('Cookie',cookie)
                a = urlopen(q).read()
                #FIXME - [Tsune] changed ioerr to err available err object (my guess)
                print('Error in opening url is -- for -- amit --: %s' % err)
            else:
                raise
        except:
                raise    
        
    data  = {}
    data = json.loads(a)
    data = byteify(data)
    file_content = base64.decodestring(data['Binary'])
    f = open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+"_"+Md5Hash+"_"+filename, 'wb')
    f.write(file_content) #TypeError: a bytes-like object is required, not 'str' 
    f.close()
    #zip_ref = zipfile.ZipFile('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.zip', 'r')
    #zip_ref.extractall('/Users/apatel/Documents/workspace/pcap_download/'+nssid)
    #zip_ref.close()
    #os.rename('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'/PCAPTraffic.pcap', '/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.pcap')
    #os.remove('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.zip') 
    #os.rmdir('/Users/apatel/Documents/workspace/pcap_download/'+nssid)
    

    #data = yaml.safe_load(json.loads(a))
    #pprint.pprint(data)
    #Captureslist =  data['Captures']
    #print "Date ;", date, " Total Number of Captures are ; " , len(Captureslist)
    return ()




            



def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )
            
 


uri_elements = []

#start = datetime.date( year = 2017, month = 2, day = 6 )
#end = datetime.date( year = 2017, month = 2, day = 9 )

#start = datetime.strptime("2017/02/08", "%y-%m-%d" )
#end = datetime.strptime("2017/02/09", "%y-%m-%d" )


def Get_capture_payload(start, end):
    start = datetime.datetime.strptime(start, "%Y-%m-%d" ).date()
    end = datetime.datetime.strptime(end, "%Y-%m-%d" ).date()
    #start = time.strptime(start,'%Y-%m-%d')
    #print "start time is:", start
    print start , ":" , end
    for date in daterange( start, end ):
    #for date in daterange( 2017-02-07, 2017-02-08 ):
        #print date
        day_str = date.strftime("%Y%m%d")
        #print "now will get capture count of the day:" , day_str
        capture_list = get_capture_counts( url, username, password, day_str )
        #print "now will get capture list of the day:" , day_str
        capture_dict = Get_Capture_List(capture_list)
        #print "Got capture list of the day which are:" , day_str
        for keys in capture_dict:
            if capture_dict[keys]['SourceUri'] not in uri_elements:
                uri_elements.append(capture_dict[keys]['SourceUri'])
                #print "Total Number of unique URLs are ; " , len(uri_elements)
                target_url.write(capture_dict[keys]['SourceUri'])
                target_url.write("\n")


#return("Done")

    
  
 #print get_capture_counts( url, username, password, days=60 )
 
if __name__ == "__main__":
     #start = datetime.date( year = 2017, month = 2, day = 8 )
     #end = datetime.date( year = 2017, month = 2, day = 9 )
     url = "https://data.nsslabs.com"
     username = "patellabs"
     password = "2992A2D48ED942A2A3596D762A4415BC"
     Today_Date = "20170224"
     TestCase = "None"
     capture_list = get_capture_counts( url, username, password, Today_Date )

     #FIXME - Only matching reference to capture_dict is at get_day_capture_dict() line 239
     pprint (capture_dict)
     capture_count = len(capture_dict)
     if ( capture_count != 0):
        Result_capture_count = "Pass"
        Note = "Counts count is  :" + str(capture_count)
        print TestCase, " ; " , Result_capture_count , "; Counts found are :" , capture_count
        assert True
     target_url = open("/Users/apatel/Documents/workspace/exploited_url.txt", 'w')
     #Get_capture_payload( '2017-02-1', "2017-02-1" )
     #print "Hello!"
     print "Program is done."  
     #target_url.close()



          


'''
def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )
            
 
start = datetime.date( year = 2016, month = 5, day = 24 )
end = datetime.date( year = 2017, month = 1, day = 4 )
 
for date in daterange( start, end ):
    #print date
    day_str = date.strftime("%Y%m%d")
    capture_list = get_capture_counts( url, username, password, day_str )
    capture_dict = Get_Capture_List(capture_list)
    
    
print "Program is done."    
#print get_capture_counts( url, username, password, days=60 )
'''



