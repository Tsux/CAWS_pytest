


import base64, pickle, json, pprint, datetime, yaml , requests  

try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2
    
'''
Set : 
DUT = 1 for CAWS QA with user  amitpatel741234567890gmailcom
DUT = 2 for CAWS QA with user  amitpatel
DUT = 3 fopr CAWS PATCH QA with user  patellabs
DUT = 
'''
    
Dut = 2 

    
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
    
def get_capture_counts( url, username, password, date ):
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
    
    a = {}
    #a = requests.get('http://apiqa.qa.colo1.nsslabs.com/Captures/List', auth=('amitpatel741234567890gmailcom', 'D7A37396AB0C40CBA489D88316D727F3'))
    try:
        a = urlopen(q).read()
    except IOError as ioerr:
        page = urlopen(q);response=page.read();page.close()
        cookie=page.info()['Set-Cookie']
        print "Cookie is :" , cookie
        # top is for obtaining the cookie via the info get.
        #req = urllib2.Request(url)#send the new url with the cookie.
        #req.add_header('User-Agent', 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-GB; rv:1.8.1.14) Gecko/20080404 Firefox/2.0.0.14')
        q.add_header('Cookie',cookie)
        a = urlopen(q).read()
        print('Error in opening url is -- for -- amit --: %s' % ioerr)
    
    data  = {}
    data = json.loads(a)
    data = byteify(data)
    #data = yaml.safe_load(json.loads(a))
    pprint.pprint(data)
    Captureslist =  data['Captures']
    print "Date ;", date, " Total Number of Captures are ; " , len(Captureslist)
    return (Captureslist)

def Get_Capture_List(Captureslist):
    capture_dict = {}
    for each_capture in Captureslist:
        #print "capture is : " , each_capture, "\n"
        #print "nssid is:" , each_capture['NSSId']
        name = each_capture['NSSId'] 
        capture_dict[name] = each_capture
    print "NSSId ; Platform ; Browser, InstalledApplication; TargetedApplication ; SourceUri "
    for keys in capture_dict:
        print keys, ";" , capture_dict[keys]['Platform'] , ";" , capture_dict[keys]['Browser'] , ";" , capture_dict[keys]['InstalledApplication'] , ";" , capture_dict[keys]['TargetedApplication'] , ";" , capture_dict[keys]['SourceUri'] , ";" , capture_dict[keys]['NetworkConnections']
        
    return (capture_dict)

            



def daterange( start_date, end_date ):
    if start_date <= end_date:
        for n in range( ( end_date - start_date ).days + 1 ):
            yield start_date + datetime.timedelta( n )
    else:
        for n in range( ( start_date - end_date ).days + 1 ):
            yield start_date - datetime.timedelta( n )
            
 
start = datetime.date( year = 2016, month = 12, day = 11 )
end = datetime.date( year = 2016, month = 12, day = 10 )
 
for date in daterange( start, end ):
    #print date
    day_str = date.strftime("%Y%m%d")
    capture_list = get_capture_counts( url, username, password, day_str )
    capture_dict = Get_Capture_List(capture_list)
    
    
    
#print get_capture_counts( url, username, password, days=60 )


