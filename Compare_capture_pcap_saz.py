import pprint, json, yaml

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
    
def compare_capture_pcap_saz():
    print "Nssid ; Capture SourceURI ; SAZ includes SourceURI ; PCAP includes SourceURI ?? ; Platform ; Browser ; TargetedApplication "    
    nssid_list_file="/Users/apatel/Documents/workspace/pcap_download/exploited_nssid.txt"    
    with open(nssid_list_file, "r") as ins: 
        for nssid in ins:
    #                array.append(line)
            #===================================================================
            # if line_num <= 460:
            #     line_num = line_num + 1
            #     continue
            #===================================================================
            nssid=nssid.replace(" ", "")
            nssid=nssid.rstrip('\n')
            nssid=nssid.rstrip('\r')
            nssid=nssid.lstrip()    
            #with open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'_saz_detail.txt', 'r') as my_saz:
            capture_saz_dict = json.load(open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'_saz_detail.txt'))
                #print "Saz : ", capture_saz_dict
            capture_pcap_dict = json.load(open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'_pcap_detail.txt'))
                
                #print "Pcap : ", capture_pcap_dict
            capture_capture_dict = json.load(open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'_capture_detail.txt'))
                #print "Capture : ", capture_capture_dict
                
            is_part_of_saz = "no"
            is_part_of_pcap = "no"  
            
            if isinstance(capture_pcap_dict, dict):
                #print "Returned dictionary :"
                for keys in capture_pcap_dict:
                    #print  "list_element_pcap is :" , capture_pcap_dict[keys]['url']
                    if(capture_capture_dict['SourceUri'] in capture_pcap_dict[keys]['url']) :
                        #print "capture SourceUri is part of the saz"
                        is_part_of_pcap = "Yes"
                        break  
            
            if isinstance(capture_saz_dict, dict):
                #print "Returned dictionary :"
                for keys in capture_saz_dict:
                     #print  "list_element_saz is :" , capture_saz_dict[keys]['url']
                     if(capture_capture_dict['SourceUri'] in capture_saz_dict[keys]['url']) :
                         #print "capture SourceUri is part of the saz"
                         is_part_of_saz = "Yes"
                         break 
    
    #         if isinstance(capture_capture_dict, dict):
    # #             print "Returned capture_capture_dict dictionary :"
    # #             pprint.pprint(capture_capture_dict)
    # #             for keys in capture_capture_dict:
    #              print  "list_element_capture is :" , capture_capture_dict['SourceUri'] 
    
            #print "Nssid:", nssid , "Source URI :",capture_capture_dict['SourceUri'], " # of urls in saz :",  len(capture_saz_dict) , "# of urls in pcap :",  len(capture_pcap_dict)
            #print "Nssid ; Capture SourceURI ; SAZ includes SourceURI ; PCAP includes SourceURI ?? ; Platform ; Browser ; TargetedApplication "
            print nssid, " ; ", capture_capture_dict['SourceUri'], " ;", is_part_of_saz  , " ; ", is_part_of_pcap , " ; " , capture_capture_dict['Platform'] ," ; " , capture_capture_dict['Browser'] ," ; " , capture_capture_dict['TargetedApplication'] 

print "Program is done."             
            
