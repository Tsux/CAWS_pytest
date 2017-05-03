


import base64, pickle, json, pprint, datetime, yaml , requests, urllib, urllib2  

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
    
Dut = 5 

    
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
    
if Dut == 5:
    #caws Beta 
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    #url = "http://10.144.192.60:82"
    url = "https://apibeta.nsslabs.com"
    
def submit_url( url, username, password, urls_to_submit):
    #print datetime.date.today() - datetime.timedelta(days=i)
    base64string = base64.b64encode('%s:%s' % (username, password))
    new_url = url + '/Scan/url/'
    print "new url is :  ", new_url, "urls_to_submit is : " ,  urls_to_submit
    #values = {'uri' : '/Scan/url/' , 'url' : 'http://www.gujaratsamachara.com/'}
    #values1 = {'url' : 'http://www.gujaratsamachara.com/'}
    #values2 = {'url' : 'http://www.gujaratsamacharb.com/'}

              
              #'url' : 'http://www.gujaratsamachar11.com/'
    #data1 = urllib.urlencode(values1)
    #data2 = urllib.urlencode(values2)
    #urls_to_submit = urls_to_submit
    data = urllib.urlencode(urls_to_submit)
    print "data portion is :" , data
    q = Request(new_url, data)
    #q = Request(url+'/files/32CC69ECEDE54C689D5BCF755A48144C')    
    #q = Request('http://apiqa.qa.colo1.nsslabs.com/Captures/List')
    #q = Request('http://apiqa-patch.qa.colo1.nsslabs.com/statistics/global?startDate=2016-11-01&endDate=2016-1201')
    q.add_header("Authorization", "Basic %s" % base64string)
    q.add_header('Accept-encoding', 'gzip, deflate')
    q.add_header('Connection',"keep-alive")
    q.add_header('context','ssl._create_unverified_context()')
    #q.add_unredirected_header('User-Agent', 'Custom User-Agent') 
    q.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')#q.add_header('User-agent', 'Mozilla/5.0')
    q.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
    #q.add_headers = ('User-Agent', 'Mozilla/5.0')
    
    #a = {}
    #a = requests.get('http://apiqa.qa.colo1.nsslabs.com/Captures/List', auth=('amitpatel741234567890gmailcom', 'D7A37396AB0C40CBA489D88316D727F3'))
    try:
        a = urllib2.urlopen(q).read()
        #cookie = a.getheader('Set-Cookie')
    except urllib2.HTTPError, e:
        error_message = e.read()
        print  error_message
        return error_message   
    
    return (a)

def get_file_submit_status( url, username, password, token):
    #print datetime.date.today() - datetime.timedelta(days=i)
    base64string = base64.b64encode('%s:%s' % (username, password))
    new_url = url + '/Scan/Status/url/' + token
    print "new url is : " , new_url
    q = Request(new_url)
    #q = Request(url+'/files/32CC69ECEDE54C689D5BCF755A48144C')    
    #q = Request('http://apiqa.qa.colo1.nsslabs.com/Captures/List')
    #q = Request('http://apiqa-patch.qa.colo1.nsslabs.com/statistics/global?startDate=2016-11-01&endDate=2016-1201')
    q.add_header("Authorization", "Basic %s" % base64string)
    q.add_header('Accept-encoding', 'gzip, deflate')
    q.add_header('Connection',"keep-alive")
    q.add_header('context','ssl._create_unverified_context()')
    #q.add_unredirected_header('User-Agent', 'Custom User-Agent') 
    q.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')#q.add_header('User-agent', 'Mozilla/5.0')
    q.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
    #q.add_headers = ('User-Agent', 'Mozilla/5.0')
    
    #a = {}
    #a = requests.get('http://apiqa.qa.colo1.nsslabs.com/Captures/List', auth=('amitpatel741234567890gmailcom', 'D7A37396AB0C40CBA489D88316D727F3'))
    try:
        a = urllib2.urlopen(q).read()
        #cookie = a.getheader('Set-Cookie')
    except urllib2.HTTPError, e:
        error_message = e.read()
        print  error_message
        return error_message   
    
    data  = {}
    data = json.loads(a)
    data = byteify(data)
    print "printing status for the token :" , token
    pprint.pprint(data)
    return (a)





values1 = (('url' , 'http://empowernetworkpackage.com/test2/test.php/'),
            ('url', 'http://www.akilaindia.com/'),
          ('url' , 'http://www.sandesh.com/'),
          ("url" , 'http://www.timeofindia.com/'),
          ("url" , 'http://www.divyabhaskar.com/'))

values2 = (('url' , 'http://amit-patel-test1.com/test1.apk/'),
            ('url', 'http://amit-patel-test2.com/test2.bat/'),
          ('url' , 'http://amit-patel-test3.com/test3.bin/'),
          ("url" , 'http://amit-patel-test4.com/test4.cab/'),
          ("url" , 'http://amit-patel-test5.com/test5.cmd/'))

'''
invalid_url_ext_list = [".apk", ".bat", ".bin", ".cab", ".cmd", ".css", ".dat", ".dll", ".doc", ".enc", ".exe", ".flv", ".gif",
".gzip", ".ico", ".inf", ".jpeg", ".js", ".mp3", ".msi", ".nub", ".pdf", ".pif", ".png", ".rar",
".scr", ".txt", ".vbs", ".wix", ".wmv", ".xls", ".zip", ".jpg"]


for invalid_url_ext in invalid_url_ext_list:
    print "A fruit of type: %s" % invalid_url_ext
    request_url = '%s?%s' % (url, query_string)
    urls_to_submit = ((('url' , 'http://amit-patel-test1.com/test1' + invalid_url_ext + '/' )))
#    print "urls_to_submit is : %s" % urls_to_submit
    capture_list = submit_url( url, username, password, urls_to_submit)
    
    if type(capture_list) is dict:
        data  = {}
        data = json.loads(capture_list)
        data = byteify(data)
        # #data = yaml.safe_load(json.loads(a))
        pprint.pprint(data)
        token_list = data['Token']
        for token in token_list:
            print "Token is : " , token 
            token_submit_status = get_file_submit_status( url, username, password, token)
    else:
        print "Return is a string : ", capture_list
    
'''
capture_list = submit_url( url, username, password, values1)
print "capture_list in row form is : ", capture_list  
if type(capture_list) is dict:
        data  = {}
        data = json.loads(capture_list)
        data = byteify(data)
        # #data = yaml.safe_load(json.loads(a))
        pprint.pprint(data)
        token_list = data['Token']
        for token in token_list:
            print "Token is : " , token 
            token_submit_status = get_file_submit_status( url, username, password, token)
else:
    print "Return is a string : ", capture_list  

    


    

'''
if isinstance(capture_list, dict):
    print "Returned dictionary :" 
    data  = {}
    data = json.loads(capture_list)
    # #data = byteify(data)
    # #data = yaml.safe_load(json.loads(a))
    pprint.pprint(data)
        
if isinstance(capture_list, str): 
    print "Returned string :", capture_list
    
if isinstance( capture_list, list):
    print "Returned as list :" , capture_list        
''' 


