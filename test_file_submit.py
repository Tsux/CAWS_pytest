import pytest, requests, datetime, time, base64, json 
from CAWS_API_2_2_4 import byteify 
#sheet_ranges = wb['range names']
#print(sheet_ranges['D18'].value)

#from openpyxl import Workbook
#from openpyxl.compat import range
#from openpyxl.utils import get_column_letter



Dut = 4 
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
    
@pytest.fixture(scope="module")
def file_submit_log():
    Today_Date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    Today_Date = datetime.datetime.now().strftime("%Y-%m-%d")
    print "Todays date is:" , Today_Date
    print "Todays date n time  is:" , Today_Date_time
    #FILE_SUBMIT_TOKEN_FILE = open("/Users/apatel/Documents/workspace/File_Submit_Token_" + Today_Date + ".txt", 'w')
    #yield (Today_Date , Today_Date_time)
    yield (Today_Date , Today_Date_time)
    #yield Today_Date_time
    #yield FILE_SUBMIT_TOKEN_FILE   
    #FILE_SUBMIT_TOKEN_FILE.close()
       
#@pytest.mark.parametrize("test_input, expected_output",
@pytest.mark.parametrize("file_name, platform, application",
                         [
                            # Microsoft Office with windows 7. 
                            ("DOC_doc.doc",'Windows7', 'Microsoft Office 2013'),
                            ("DOC_docx.docx",'Windows7', 'Microsoft Office 2013'),
                            ("1_mb_xls_save_as.xls",'Windows7', 'Microsoft Office 2013'),
                            ("1_mb_xlsx_saveas.xlsx",'Windows7', 'Microsoft Office 2013'),                            
                            ("DOC_csv.csv",'Windows7', 'Microsoft Office 2013'),
                            ("DOC_pps.pps.ppt", 'Windows7', 'Microsoft Office 2013'),
                            ("1_mb_ppt_saveass.pptx", 'Windows7', 'Microsoft Office 2013'),

                            
#                             # Microsoft Office with windows 10  
#                             ("DOC_doc.doc",'Windows10', 'Microsoft Office 2016'),
#                             ("DOC_docx.docx",'Windows10', 'Microsoft Office 2016'),
#                             ("1_mb_xls_save_as.xls",'Windows10', 'Microsoft Office 2016'),
#                             ("1_mb_xlsx_saveas.xlsx",'Windows10', 'Microsoft Office 2016'),
#                             ("DOC_csv.csv",'Windows10', 'Microsoft Office 2016'),  
#                             ("DOC_pps2.pps.ppt", 'Windows10', 'Microsoft Office 2016'),
#                             ("1_mb_ppt_saveass.pptx", 'Windows10', 'Microsoft Office 2016'),                        
                            
                            #pdf file
                            ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.017.20050"),
                            ("DOC_pdf.pdf","Windows7" , "Adobe Reader DC 2015.007.20033"),
                            ("DOC_pdf.pdf","Windows7" , "Adobe Reader 9.4"),
                            ("DOC_pdf.pdf","Windows7" , "Adobe Reader DC 2015.020.20039"),
                            
                            #Apple files with Win 7
                            ("SampleAudio_0.5mb.mp3",'Windows7', 'Quicktime 7.79' ),
                            ("SampleAudio_0.5mb.mp3",'Windows7', 'Itunes 12.5.1' ),
                            ("SampleAudio_0.5mb.mp3",'Windows7', 'Itunes 12.5.4' ),
                            
                            #VLC
                            ("SampleAudio_0.5mb.mp3",'Windows7', 'VLC 2.2.3' ),
                            ("SampleAudio_0.5mb.mp3",'Windows7', 'VLC 2.2.4' )
                            #("Casio-MT-45-Elec-Piano-C4.wav",'Windows7', 'Quicktime 7.79'),
                            #("DOC_docx.docx"),
                            #("DOC_docx_LongFileName-12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901324567890123456789.docx"),
                            #("DOC_dot.dot.doc"),
                            #("DOC_htm.htm"),
                            #("DOC_html.html"),
                            #("DOC_ics.ics"),
                            #("DOC_mpp.mpp"),
                            #("DOC_odf.odf"),
                            #("DOC_odp.odp"),
                            #("DOC_ods.ods"),
                            #("DOC_odt.odt"),
# 
#                             ("DOC_ppsx.ppsx"),
#                             ("DOC_ppt.ppt"),
#                             ("DOC_ppt_TEST.ppt"),
#                             ("DOC_pptx.pptx"),
#                             ("DOC_pptx2.pptx"),
#                             ("DOC_rtf.rtf"),
#                             ("DOC_rtf2.rtf"),
#                             ("DOC_sxw.sxw"),
#                             ("DOC_test.txt"),
#                             ("DOC_test_3.txt"),
#                             ("DOC_txt_ANSI_.txt"),
#                             ("DOC_txt_UTF8_.txt"),
#                             ("DOC_txt_UnicodeBigEndian_.txt"),
#                             ("DOC_txt_Unicode_.txt"),
#                             ("DOC_txt_ms-dos_.txt"),
#                             ("DOC_vcf.vcf"),
#                             ("DOC_vsd_1.vsd"),
#                             ("DOC_vsd_2.vsd"),
#                             ("DOC_wpd.wpd"),
#                             ("DOC_wps.wps"),
#                             ("DOC_xls_TEST.xls"),
#                             ("DOC_xlsx.xlsx"),
#                             ("DOC_xlsx_long_file_name_123456789012345678901234567890123456789012345678901234567890134567890123456789012345678901234567890123456789012345678901234567989012345678901234567890.xlsx"),
#                             ("DOC_xml.xml"),
#                             ("Getting_Started.key"),
#                             ("Getting_Started.numbers"),
#                             ("Getting_Started.pages"),
#                             ("SampleAudio_0.4mb.mp3"),
#                             ("SampleAudio_0.5mb.mp3"),
#                             ("SampleDOCFiles_100kb.doc"),
#                             ("SampleVideo_1280x720_5mbxcxc_1_.mp4"),
#                             ("bird.avi"),
#                             ("cbw3.avi"),
#                             ("flame.avi"),
#                             ("pptupload.ppt")
                         ]
                         )

#sample token = 5008F26FECE31FFCA09D44CEF2CE28B9
#def test_submit_pdf(test_input, expected_output):
def test_submit_file(file_name, platform, application,file_submit_log):
    #FILE_SUBMIT_TOKEN_FILE = file_submit_log[2]
    #(fname,token, now) = submit_pdf(url, username, password, "/Users/apatel/Documents/CAWS/CAWS 2.2/CAWS_2.2_Release_Notes.pdf")
    (fname,token, now, hash) = submit_file(url, username, password, "/Users/design/GitHub/CAWS_API_2.2_V1/files_for_summit_source/"+file_name, platform, application,file_submit_log )
    assert file_name != token
    assert file_name != application
    #assert (file_name + ";" + token) != (platform + ";" + application)
      
    print "url is : ", url, "token is :" , token ,"for file name : ", file_name , "submitted at :" , now , "token length = " , len(token), hash , len(hash)
    #return (token, filename)

    
#def submit_file(server_api_url, username, password,file, platform, application, ):
def submit_file(server_api_url, username, password,file, platform, application,file_submit_log ):
    Today_Date_time = file_submit_log[1]
    file = file
    platform = platform
    application = application
    token = "None"
    hash = "None"
    message = "None"

    base64string = base64.b64encode('%s:%s' % (username, password))
    base_api_url = server_api_url + '/Scan/file/'
    #print "file is :" , file
    #wb = load_workbook(filename = '/Users/apatel/Documents/workspace/Workbook1.xlsm')
    headers = {
        'authorization': "Basic cGF0ZWxsYWJzOjI5OTJBMkQ0OEVEOTQyQTJBMzU5NkQ3NjJBNDQxNUJD",
        'cache-control': "no-cache"
        }
    files = {'file': open(file, 'rb')}
    #response = requests.post(base_api_url, files=files,  headers=headers, data = {"platform" : "1", "applicationPackage" : "Adobe Reader DC 2015.017.20050"})
    response = requests.post(base_api_url, files=files,  headers=headers, data = {"platform" : platform, "applicationPackage" : application})
    now = datetime.datetime.now()
    print "Response for the http://apibeta.nsslabs.com/Scan/file/ request which returns the token : "
    print (str(now) + " ; " + file + " ; " + (response.text))
    line = response.text
    capture_msg_dict = json.loads(response.text)
    capture_msg_dict = byteify(capture_msg_dict)
    if "This file was already submitted" in line:
        hash = capture_msg_dict['Message'].split(" ")[-1:][0]
        message = capture_msg_dict['Message']
    elif "platform" in line:
        token = "None"
        message = capture_msg_dict['Message']
    elif "application" in line:
        token = "None"
        message = capture_msg_dict['Message']
    else:
        token = capture_msg_dict['Token']
        message = "None"
        #print "this file was already submitted and its  token is:" , token
    #print "response dictionary message is : " , capture_msg_dict['Message']
    line=line.replace("Token", "")
    line=line.replace("{\"\":", "")
    line=line.replace("\"}", "")
    line=line.replace("\"", "")
    line=line.rstrip('\n')
    line=line.rstrip('\r')
    line=line.lstrip()
    #print "line is :", line
    if(token != "None"):
        capture_token_string =  str(now)  + " ; "  + file + " ; " + str(token) + " ; " + message + " ; " + str(hash)
    else:
        capture_token_string =  str(now)  + " ; "  + file + " ; " + str(token) + " ; " + message + " ; " + str(hash)
    #capture_token_string =  str(now)  + " ; "  + file + " ; " + str(line)
    #target_url = open("/Users/apatel/Documents/workspace/File_Submit_Token.txt", 'a+')
    #FIXME - [Tsune] /Users/design/GitHub/CAWS_API_2.2_V1/
    FILE_SUBMIT_TOKEN_FILE = open("/Users/design/GitHub/CAWS_API_2.2_V1/File_Submit_Token_"+Today_Date_time+".txt", 'a+')
    FILE_SUBMIT_TOKEN_FILE.write(capture_token_string)
    FILE_SUBMIT_TOKEN_FILE.write("\n")
    
    FILE_SUBMIT_TOKEN_FILE.close()
#    token_file.write(capture_token_string)
    return (file, token, now, hash)

    
# def test_disabling_capturing(capsys):
#     print('this output is captured')
#     with capsys.disabled():
#         print('output not captured, going directly to sys.stdout')
#     print('this output is also captured')
    

# if __name__ == '__main__':
#     #(token, filename) = test_submit_pdf(server_api_url = url, username=username, password=password, file='/Users/apatel/Documents/CAWS/CAWS 2.2/CAWS_2.2_Release_Notes.pdf')
#     (token, filename) = test_submit_pdf()
#     print ("program is done. Token and file are:" , token , file)
#     #test_disabling_capturing()



# AA
# Response for the http://apibeta.nsslabs.com/Scan/file/ request which returns the token : 
# 2017-02-16 11:39:53.240196  ;  empty_book_1.xls  ;  {"Token":"DBBAE6783EBA46428C9C9AD2BB165BE7"}
# line is : DBBAE6783EBA46428C9C9AD2BB165BE7
# program is done

