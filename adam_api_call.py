
import base64
import urllib, urllib2, ssl

def make_api_request(username, password, url, arguments):
   request_url = url
   encoded_auth = 'Basic %s' % base64.b64encode('%s:%s' % (username, password))
   query_string = urllib.urlencode(arguments)

   if len(query_string) > 0:
       request_url = '%s?%s' % (url, query_string)
   
   request = urllib2.Request(request_url)
   request.add_header('Authorization', encoded_auth)

   return urllib2.urlopen(request, context=ssl._create_unverified_context()).read()

result = make_api_request('amitpatel741234567890gmailcom', 'D7A37396AB0C40CBA489D88316D727F3', 'http://apiqa.qa.colo1.nsslabs.com/Captures/List', {})
#result = make_api_request('patellabs', '2992A2D48ED942A2A3596D762A4415BC', 'http://data.nsslabs.com/Captures/List', {})
print(result)