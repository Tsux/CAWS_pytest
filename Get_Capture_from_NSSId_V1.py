import requests, json, base64

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
#target_url = open("/Users/apatel/Documents/workspace/URL_SUBMIT_TOKEN.txt", 'a+') 

    
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
    #url = "https://apibeta.nsslabs.com"
    url = "https://apibeta.nsslabs.com"
    #url = "http://apibeta.nsslabs.com/Scan/url/"
    
    base64string = base64.b64encode('%s:%s' % (username, password))
    
    headers = {
        #'authorization': "Basic cGF0ZWxsYWJzOjI5OTJBMkQ0OEVEOTQyQTJBMzU5NkQ3NjJBNDQxNUJD",
        'authorization': "Basic %s" % base64string , 
        'cache-control': "no-cache"
        #'postman-token': "ff327d11-ae3b-95aa-8a7d-41269711ed55"
        }    


target_url = open("/Users/apatel/Documents/workspace/capture_info.txt", 'a+') 
url_token_list_file = "/Users/apatel/Documents/workspace/URL_TOKEN_with_NSSId.txt"
line_num=0
with open(url_token_list_file, "r") as ins:
    for line in ins:
        #array.append(line)
        #===================================================================
        # if line_num <= 460:
        #     line_num = line_num + 1
        #     continue
        #===================================================================
        print "line number is : ", line_num

        line=line.replace(" ", "")
        line=line.rstrip('\n')
        line=line.rstrip('\r')
        line=line.lstrip()
        if "micro" in line:
            continue
        #print line
        url_to_scan = line.split(';')[0]
        token = line.split(';')[1]
        nssid_to_scan = line.split(';')[2]
        #url = "http://apibeta.nsslabs.com/Scan/Status/url/634DF6E7AC6742B187EC945871EBE4DC"
        url_users_capture = url +"/users/captures/"+str(nssid_to_scan)
        url_pcap_download = url +"/Captures/Files/Pcap/"+str(nssid_to_scan)
        print "url to get pcap is : ", url_pcap_download
        #url = "http://apibeta.nsslabs.com/users/captures/"+str(nssid_to_scan)
        #USERS/CAPTURES/{nssid}
        #print url_to_scan ,  token, nssid_to_scan, url
        response = {}
        response = requests.request("GET", url_users_capture, headers=headers)
        #string = response.text
        #=======================================================================
        # NSSId = string.split('\"')[3]
        # Status = string.split(':')[-1]
        # print url_to_scan , " ; " , token , " ; " , NSSId , " ; " , Status
        # capture_token_string = url_to_scan + " ; " + token + " ; " + NSSId 
        #target_url.write(str(capture_token_string))
        capture_list  = {}
        capture_list = json.loads(str(response.text))
        #capture_list = byteify(data)
        if type(capture_list) is dict:
            #token_list = capture_list['NSSId']
            #print "nssid is : " , len(token_list)
            #print "nssid is : " , capture_list['NSSId']
            print "IsMalicious is:" , capture_list['IsMalicious'],":"
            #===================================================================
            # capture_list['IsMalicious']=capture_list['IsMalicious'].replace(" ", "")
            # capture_list['IsMalicious']=capture_list['IsMalicious'].rstrip('\n')
            # capture_list['IsMalicious']=capture_list['IsMalicious'].rstrip('\r')
            # capture_list['IsMalicious']=capture_list['IsMalicious'].lstrip()
            #===================================================================
            if (capture_list['IsMalicious']):
                print "nss id is :" , capture_list['NSSId'] , "is Malicious."
                response_pcap_download = requests.request("GET", url_pcap_download, headers=headers)
                print "response_pcap_download is :" , response_pcap_download.text
                 
                #capture_token_string = str(line_num) + " ; " + str(post_submit_time)  + " ; "  + line + " ; " + token + " ; " + str(browserPackage_list[browserPackage]) + " ; " + str(template)
                #capture_token_string = str(now)  + " ; "   + token
                #capture_token_string = token
                #print capture_token_string 
                #target_url.write(capture_token_string)
                #target_url.write("\n")
                #tmp_cnt=tmp_cnt + 1
                            
        else:
            print "capture_list is not a dict." , capture_list
        target_url.write(str(response.text))
        target_url.write("\n")
        
        #=======================================================================
        line_num = line_num + 1
        #print "Response for the url scan status http://apibeta.nsslabs.com/Scan/Status/url/{token=634DF6E7AC6742B187EC945871EBE4DC} request which returns NSS ID and status."
        #print(response.text)
target_url.close()
#url_token_list_file.close()

