#!/usr/bin/env python

import dpkt, pprint, json


url_list_file="/Users/apatel/Documents/workspace/pcap_download/exploited_nssid.txt"  
 

with open(url_list_file, "r") as ins:
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
        print "pcap file name is: /Users/apatel/Documents/workspace/pcap_download/",nssid,'.pcap'   
        #saz = Saz('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.saz')


#f = open('/Users/apatel/Documents/workspace/infinity.pcap')
        #capture_text_file = open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'_pcap_detail.txt', 'w') 
        f = open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'.pcap')
        pcap = dpkt.pcap.Reader(f)
        pkt = 0
        id = 1
        d = {}
        for ts, buf in pcap:
            pkt = pkt + 1
            eth = dpkt.ethernet.Ethernet(buf)
            if eth.type!=dpkt.ethernet.ETH_TYPE_IP:
                    #print "not a ip packet"
                continue
            ip=eth.data
            if ip.p==dpkt.ip.IP_PROTO_UDP: # Check for UDP packets
                UDP=ip.data
                continue            
            
            if ip.p==dpkt.ip.IP_PROTO_TCP: # Check for TCP packets
                tcp=ip.data
                #print "packet is tcp" , tcp
                if tcp.dport == 1212 and len(tcp.data) > 0:
                #if (tcp.dport == 80):
                    try:
                        http_req = dpkt.http.Request(tcp.data)
                    except (dpkt.dpkt.NeedData, dpkt.dpkt.UnpackError):
                        #print "pkt with error is :" , pkt
                        continue
                    #print "req Method is:", http_req.method

                    #print "req version is:", http_req.version
                    #print "req header is:", http_req.headers
                    #print "host is :", http_req.headers['host']
                    #url = http_req.headers['host'] + http_req.uri
                    print "req uri is:", http_req.uri, "for nssid : " , nssid 
                    #print "url is: ", url
                    d[id] = {}
                    d[id]['url'] = http_req.uri
                    #d[url]['method'] = http_req.method
                    d[id]['method'] = http_req.method

                if tcp.sport == 1212 and len(tcp.data) > 0:
                #if (tcp.sport == 80) :
                    try:
                        http_res = dpkt.http.Response(tcp.data)
                    except:
                        #print "Error: parsing pcap : %s %s :" %nssid %e
                        just_cnt = 1
                        #print "Error: parsing pcap : ", nssid 
                        
                        continue 
                    #print tcp.sport
                    #print "res status is:", http_res.status
                    #d[url]['status_code'] = http_res.status
                    if('status_code' in http_res.headers):
                        d[id]['status_code'] = http_res.status
                    #print "res reason is:", http_res.reason
                    #print "res version is:", http_res.version
                    #print "res headers is:", http_res.headers
                    #print "res date is:" , http_res.headers['date']
                    #d[url]['date'] = http_res.headers['date']
#                     if('date' in http_res.headers):
#                         print http_res.headers
#                         print "pkt with error is :", pkt
#                         if('date' not in d[id].keys()):
#                             d[id]['date'] = http_res.headers['date']
                        #Sprint http_res.headers['date']
                    #print "res body is:", http_res.body
                    #capture_text_file.write(str(d))
                    #capture_text_file.write("\n")
                    id = id+1
                    
                  
            else:
                continue  
                                 

            #pkt = pkt+1
            #print "pkt is :" , pkt

        #print "now id is:" , id
        f.close()
        json.dump(d, open('/Users/apatel/Documents/workspace/pcap_download/'+nssid+'_pcap_detail.txt','w'))
        #capture_text_file.write(str(d))
        #pprint.pprint(d)
        #capture_text_file.close()
        

print "program is done."
