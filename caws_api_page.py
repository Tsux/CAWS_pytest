
    

import base64, pickle, json, pprint
import urllib2
#from urllib2 import URLError
#from urllib2 import Request
try:
    from urllib.request import Request, urlopen  # Python 3
except:
    from urllib2 import Request, urlopen  # Python 2

username = "amitpatel741234567890gmailcom"
password = "D7A37396AB0C40CBA489D88316D727F3"
#username = "amitpatel"
#password = "BB8FA646126D4C8991C6088E1E60E684"
    
base64string = base64.b64encode('%s:%s' % (username, password))
#request.add_header("Authorization", "Basic %s" % base64string)  

q = Request('http://apiqa.qa.colo1.nsslabs.com/Captures/List')
q.add_header("Authorization", "Basic %s" % base64string) 
#q.add_header('User-agent', 'Mozilla/5.0')
a = {}
a = urllib2.urlopen(q, cadefault=True).read()
pprint.pprint(a)


data  = {}
data = json.loads(a)
pprint.pprint(data)
Captureslist =  data['Captures']

print "list elements are" , len(Captureslist)


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





for majorkey, subdict in data.iteritems():
  for one_majorkey in subdict:
    for subkey, value in one_majorkey.iteritems():
        for each_subkey, valu_U in value.iteritems():
            for each_sub_subkey, value_Q in valu_U.iteritems():
                for each_sub_sub_subkey, value_num in value_Q.iteritems():
                    print each_sub_sub_subkey, value_num
'''


'''

__author__ = 'jcollinge@nsslabs.com'
import requests, pickle, base64
# Define Variables
username = "amitpatel741234567890gmailcom"
password = "D7A37396AB0C40CBA489D88316D727F3"
caws_search_url = 'http://apiqa.qa.colo1.nsslabs.com/Captures/List'
#This needs to be part of each request to API V2, USERID:API_Key needs to be Base64encoded
base64string_uname = base64.b64encode('%s' % (username))
base64string_passwd = base64.b64encode('%s' % (password))
caws_req_headers = {"Authorization:Basic" + base64string_uname + ":" + base64string_passwd}
def main():
 while True:
 # Get user input for the query
    #input_parameter = raw_input("Please enter the API parameter for the request:")
    #input_value = raw_input("Please enter the parameter value for the request: ")
 # Print/Confirm what we're searching for
    #print ("Searching for parameter: " + input_parameter + " with value " + input_value)
 #Build the request payload
    #caws_req_payload = (input_parameter + '=' + input_value)
 #Submit the request to the CAWS API
    caws_response = requests.get(caws_search_url, headers=caws_req_headers,params=caws_req_payload);
 #Print the response
    print caws_response.text
 #Write the response to a file
 
    f = open("response.txt","w")
    pickle.dump(caws_response, f)
    f.close()
    ans = raw_input("Would you like to create another request (y/n)? ")
     
    if ans.strip() != 'y':
        break
     
main()


__author__ = 'jcollinge@nsslabs.com'

import requests, pickle

# Define Variables
caws_search_url = 'http://apiqa.qa.colo1.nsslabs.com/Captures/List?'

#This needs to be part of each request to API V2, USERID:API_Key needs to be Base64 encoded
caws_req_headers = {'Authorization':'Basic USERID:API_KEY'}

def main():

    while True:

        # Get user input for the query
        input_parameter = raw_input("Please enter the API parameter for the request: ")
        input_value = raw_input("Please enter the parameter value for the request: ")

        # Print/Confirm what we're searching for
        print ("Searching for parameter: " + input_parameter + " with value " + input_value)

        #Build the request payload
        caws_req_payload = (input_parameter + '=' + input_value)

        #Submit the request to the CAWS API
        caws_response = requests.get(caws_search_url, headers=caws_req_headers, params=caws_req_payload);

        #Print the response
        print caws_response.text

        #Write the response to a file
        f = open("response.txt","w")
        pickle.dump(caws_response, f)
        f.close()

        ans = raw_input("Would you like to create another request (y/n)? ")
        if ans.strip() != 'y':
            break

main()
'''
 