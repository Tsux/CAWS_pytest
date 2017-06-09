import os
import subprocess
import base64
import datetime
import json
import pprint
import pytest
import requests
import time

from CAWS_API_2_2_4 import byteify

Dut = 4

if Dut == 1:
    # cawsqa -- user/password
    username = "amitpatel741234567890gmailcom"
    password = "D7A37396AB0C40CBA489D88316D727F3"
    url = "http://apiqa.qa.colo1.nsslabs.com"

if Dut == 2:
    # cawsqa -- user/password
    username = "amitpatel"
    password = "BB8FA646126D4C8991C6088E1E60E684"
    url = "http://apiqa.qa.colo1.nsslabs.com"

if Dut == 3:
    # caws qa patch
    username = "patellabs"
    password = "240DA1A652B44014993D59986156DE47"
    url = "http://apiqa-patch.qa.colo1.nsslabs.com"

if Dut == 4:
    # caws qa patch
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    url = "http://data.nsslabs.com"

if Dut == 5:
    # caws Beta
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    url = "https://apibeta.nsslabs.com"


@pytest.fixture(scope="module")
def file_submit_log():
    username = "patellabs"
    password = "2992A2D48ED942A2A3596D762A4415BC"
    url = "https://data.nsslabs.com"
    utc_datetime = datetime.datetime.utcnow()
    Today_Date_time = utc_datetime.strftime("%Y-%m-%d-%H-%M-%S")
    Today_Date = utc_datetime.strftime("%Y-%m-%d")
    print "utc_datetime is:", utc_datetime, ":"
    tmp_data_directory = "/CAWS_pytest/files_for_summit_source/tmp/" + utc_datetime.strftime(
        "%Y-%m-%d-%H-%M-%S") + "/"
    if not os.path.exists(tmp_data_directory):
        os.makedirs(tmp_data_directory)
        print "new directory created . already exists"
    else:
        print "directory already exists"

    print "Todays date is:", Today_Date
    print "Todays date n time  is:", Today_Date_time

    file_list_dict = {}
    file_list_dict["submission_metadata"] = {
        "File_name": "None",
        "File_location": "/CAWS_pytest/files_for_summit_source/",
        "Submit_file_location": tmp_data_directory,
        "Token_file_location": tmp_data_directory,
        "Submit_name": "None",
        "Token": "None",
        "Submit_time": "None",
        "Status": "None",
        "NSSId": "None",
        "Platform": "None",
        "ApplicationPackage": "None",
        "Result_time": "None",
        "Md5hash": "None",
        "Time_delta": "None"
    }
    start_up_config_dict = {"url": url, "username": username, "password": password, "utc_datetime": utc_datetime,
                            "file_list_dict": file_list_dict, "tmp_data_directory": tmp_data_directory}
    return (start_up_config_dict)


def test_prepare_office_submit_files():
    office_path = "files_for_summit_source/"
    subprocess.call("java -jar msoffice-access.jar " + office_path, shell=True)


@pytest.mark.parametrize("file_name, platform, application",
                         [
                             # Microsoft Office with windows 7.
                             ("DOC_doc.doc", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_docx.docx", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_xls_save_as.xls", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_xlsx_saveas.xlsx", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_csv.csv", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_pps.pps.ppt", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_ppt_saveass.pptx", 'Windows7', 'Microsoft Office 2013'),

                             # Microsoft Office with windows 10
                             # ("DOC_doc.doc",'Windows10', 'Microsoft Office 2016'),
                             # ("DOC_docx.docx",'Windows10', 'Microsoft Office 2016'),
                             # ("1_mb_xls_save_as.xls",'Windows10', 'Microsoft Office 2016'),
                             # ("1_mb_xlsx_saveas.xlsx",'Windows10', 'Microsoft Office 2016'),
                             # ("DOC_csv.csv",'Windows10', 'Microsoft Office 2016'),
                             # ("DOC_pps2.pps.ppt", 'Windows10', 'Microsoft Office 2016'),
                             # ("1_mb_ppt_saveass.pptx", 'Windows10', 'Microsoft Office 2016'),

                             # pdf file
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.017.20050"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.007.20033"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader 9.4"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.020.20039"),

                             # Apple files with Win 7
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Quicktime 7.79'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Itunes 12.5.1'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Itunes 12.5.4'),

                             # VLC
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'VLC 2.2.3'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'VLC 2.2.4')
                             # ("Casio-MT-45-Elec-Piano-C4.wav",'Windows7', 'Quicktime 7.79'),
                             # ("DOC_docx.docx"),
                             # ("DOC_docx_LongFileName-12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901324567890123456789.docx"),
                             # ("DOC_dot.dot.doc"),
                             # ("DOC_htm.htm"),
                             # ("DOC_html.html"),
                             # ("DOC_ics.ics"),
                             # ("DOC_mpp.mpp"),
                             # ("DOC_odf.odf"),
                             # ("DOC_odp.odp"),
                             # ("DOC_ods.ods"),
                             # ("DOC_odt.odt"),
                             #
                             # ("DOC_ppsx.ppsx"),
                             # ("DOC_ppt.ppt"),
                             # ("DOC_ppt_TEST.ppt"),
                             # ("DOC_pptx.pptx"),
                             # ("DOC_pptx2.pptx"),
                             # ("DOC_rtf.rtf"),
                             # ("DOC_rtf2.rtf"),
                             # ("DOC_sxw.sxw"),
                             # ("DOC_test.txt"),
                             # ("DOC_test_3.txt"),
                             # ("DOC_txt_ANSI_.txt"),
                             # ("DOC_txt_UTF8_.txt"),
                             # ("DOC_txt_UnicodeBigEndian_.txt"),
                             # ("DOC_txt_Unicode_.txt"),
                             # ("DOC_txt_ms-dos_.txt"),
                             # ("DOC_vcf.vcf"),
                             # ("DOC_vsd_1.vsd"),
                             # ("DOC_vsd_2.vsd"),
                             # ("DOC_wpd.wpd"),
                             # ("DOC_wps.wps"),
                             # ("DOC_xls_TEST.xls"),
                             # ("DOC_xlsx.xlsx"),
                             # ("DOC_xlsx_long_file_name_123456789012345678901234567890123456789012345678901234567890134567890123456789012345678901234567890123456789012345678901234567989012345678901234567890.xlsx"),
                             # ("DOC_xml.xml"),
                             # ("Getting_Started.key"),
                             # ("Getting_Started.numbers"),
                             # ("Getting_Started.pages"),
                             # ("SampleAudio_0.4mb.mp3"),
                             # ("SampleAudio_0.5mb.mp3"),
                             # ("SampleDOCFiles_100kb.doc"),
                             # ("SampleVideo_1280x720_5mbxcxc_1_.mp4"),
                             # ("bird.avi"),
                             # ("cbw3.avi"),
                             # ("flame.avi"),
                             # ("pptupload.ppt")
                         ]
                         )
def test_submit_file(file_name, platform, application, file_submit_log):
    (fname, token, now, hash) = submit_file(file_name, platform, application, file_submit_log)
    assert fname != token
    assert fname != application
    assert fname != platform
    print "url is: ", url, "token is: ", token, "for file name: ", file_name, "submitted at: ", now, \
        "token length = ", len(token), hash, len(hash)


@pytest.mark.parametrize("file_name, platform, application",
                         [
                             # Microsoft Office with windows 7.
                             ("DOC_doc.doc", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_docx.docx", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_xls_save_as.xls", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_xlsx_saveas.xlsx", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_csv.csv", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_pps.pps.ppt", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_ppt_saveass.pptx", 'Windows7', 'Microsoft Office 2013'),

                             # pdf file
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.017.20050"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.007.20033"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader 9.4"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.020.20039"),

                             # Apple files with Win 7
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Quicktime 7.79'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Itunes 12.5.1'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Itunes 12.5.4'),

                             # VLC
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'VLC 2.2.3'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'VLC 2.2.4')
                         ]
                         )
def test_check_file_submit_status(file_name, platform, application, file_submit_log):
    (file_submit_log["file_list_dict"]["submission_metadata"])["File_name"] = file_name
    (file_submit_log["file_list_dict"]["submission_metadata"])["Platform"] = platform
    (file_submit_log["file_list_dict"]["submission_metadata"])["ApplicationPackage"] = application

    (Status, NSSId, delta, token) = check_file_submit_status(file_submit_log)
    __tracebackhide__ = True
    if (str(Status) != "2"):
        pytest.fail("Status is still not completed even after wait period is %d secs and status is still : %s" % (
        delta, Status,))
    file_list_dict = file_submit_log["file_list_dict"]["submission_metadata"]
    assert token != ""
    assert application != ""
    assert platform != ""
    assert Status != ""
    assert NSSId != ""
    assert delta != ""
    assert token != ""


@pytest.mark.parametrize("file_name, platform, application",
                         [
                             # Microsoft Office with windows 7.
                             ("DOC_doc.doc", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_docx.docx", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_xls_save_as.xls", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_xlsx_saveas.xlsx", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_csv.csv", 'Windows7', 'Microsoft Office 2013'),
                             ("DOC_pps.pps.ppt", 'Windows7', 'Microsoft Office 2013'),
                             ("1_mb_ppt_saveass.pptx", 'Windows7', 'Microsoft Office 2013'),

                             # pdf file
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.017.20050"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.007.20033"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader 9.4"),
                             ("DOC_pdf.pdf", "Windows7", "Adobe Reader DC 2015.020.20039"),

                             # Apple files with Win 7
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Quicktime 7.79'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Itunes 12.5.1'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'Itunes 12.5.4'),

                             # VLC
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'VLC 2.2.3'),
                             ("SampleAudio_0.5mb.mp3", 'Windows7', 'VLC 2.2.4')
                         ]
                         )
def test_check_file_nssid_details(file_name, platform, application, file_submit_log):
    (file_submit_log["file_list_dict"]["submission_metadata"])["File_name"] = file_name
    (file_submit_log["file_list_dict"]["submission_metadata"])["Platform"] = platform
    (file_submit_log["file_list_dict"]["submission_metadata"])["ApplicationPackage"] = application
    nssid_dict = {}
    nssid_dict = check_file_nssid_details(file_submit_log)
    for key in nssid_dict:
        assert nssid_dict[key] != ""
        print "key is :", key, " and values is:", nssid_dict[key]
        if (key == "ErrorMessage"):
            pytest.fail("Got Errormessage %s that %s at : %s" % (key, nssid_dict[key], nssid_dict["ErrorDate"]))
    file_list_dict = file_submit_log["file_list_dict"]["submission_metadata"]
    platform = file_list_dict["Platform"]
    application = file_list_dict["ApplicationPackage"]


def submit_file(file_name, platform, application, file_submit_log):
    """Submits a file - File Submission Test Phase 1
    :param file_name: File name for submitted
    :param platform: Submission platform name
    :param application: Submission applacation package
    :param file_submit_log: Submission submit log
    :return:
    """
    url = file_submit_log["url"] + '/Scan/file/'
    username = file_submit_log["username"]
    password = file_submit_log["password"]
    Today_Date_time = str(file_submit_log["utc_datetime"].strftime("%Y-%m-%d-%H-%M-%S"))
    print "Today_Date_time is : ", Today_Date_time

    file_list_dict = file_submit_log["file_list_dict"]["submission_metadata"]
    file_list_dict["File_name"] = file_name
    file_list_dict["Platform"] = platform
    file_list_dict["ApplicationPackage"] = application
    subFile = file_list_dict["File_location"] + file_name
    token = "None"
    hash = "None"
    message = "None"
    print "file name is :", subFile

    base64string = base64.b64encode('%s:%s' % (username, password))
    headers = {
        'authorization': "Basic %s" % base64string,
        'cache-control': "no-cache"
    }
    files = {'file': open(subFile, 'rb')}
    response = requests.post(url, files=files, headers=headers,
                             data={"platform": platform, "applicationPackage": application})
    now = str(datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S"))
    file_list_dict["Submit_time"] = now
    print "Response for the ", url, "Scan/file/ request which returns the token : "
    print (str(now) + " ; " + subFile + " ; " + (response.text))
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
        print "token before is: ", file_list_dict["Token"]
        token = capture_msg_dict["Token"]
        message = "File Submit Token"
        file_list_dict["Token"] = token
        # print "this file was already submitted and its  token is:" , token

    if (token != "None"):
        capture_token_string = str(now) + " ; " + subFile + " ; " + str(token) + " ; " + message + " ; " + str(hash)
    else:
        capture_token_string = str(now) + " ; " + subFile + " ; " + str(token) + " ; " + message + " ; " + str(hash)

    FILE_SUBMIT_TOKEN_FILE = open("/CAWS_pytest/File_Submit_Token_" + Today_Date_time + ".txt",
                                  'a+')
    FILE_SUBMIT_TOKEN_FILE.write(capture_token_string)
    FILE_SUBMIT_TOKEN_FILE.write("\n")
    print "dictionary for file is:", file_list_dict
    json.dump(file_list_dict, open(file_submit_log['tmp_data_directory'] + file_list_dict["File_name"] + '.txt', 'w'))

    FILE_SUBMIT_TOKEN_FILE.close()
    return (file, token, now, hash)


def check_file_submit_status(file_submit_log):
    """Verifies file has been successfully submitted - File Submission Test Phase 2
    :param file_submit_log: Submission submit log
    """
    pprint.pprint(file_submit_log)
    time.sleep(500)
    username = file_submit_log["username"]
    password = file_submit_log["password"]
    file_list_dict = file_submit_log["file_list_dict"]["submission_metadata"]

    file_submit_result_dict = json.load(
        open(file_submit_log['tmp_data_directory'] + file_list_dict["File_name"] + '.txt'))
    print file_submit_result_dict
    token = file_submit_result_dict["Token"]
    Submit_time = file_submit_result_dict["Submit_time"]
    file_list_dict["Submit_time"] = file_submit_result_dict["Submit_time"]
    print "submit time is :", Submit_time
    url = file_submit_log["url"] + '/Scan/Status/file/' + str(token)
    print "url and token for the query is :", url, ";", token
    base64string = base64.b64encode('%s:%s' % (username, password))
    headers = {
        'authorization': "Basic %s" % base64string,
        'cache-control': "no-cache"
    }
    my_datetime = datetime.datetime.strptime(Submit_time, '%Y-%m-%d-%H-%M-%S')
    delta = (datetime.datetime.utcnow() - my_datetime).seconds
    response_dict = {}

    while ("NSSId" not in response_dict):
        del response_dict
        print "even after ", delta, "seconds, status is not 2. Will wait for 5 mins now"
        delta = (datetime.datetime.utcnow() - my_datetime).seconds
        time.sleep(5)

        response = requests.request("GET", url, headers=headers)
        response_dict = json.loads(response.text)
        response_dict = byteify(response_dict)

    print "response to status check is: ", response.text
    if "NSSId" in response_dict:
        file_list_dict["NSSId"] = response_dict["NSSId"]
        file_list_dict["Status"] = response_dict['Status']
    else:
        file_list_dict["Status"] = response_dict['Status']

    json.dump(file_list_dict, open(file_submit_log['tmp_data_directory'] +
                                   file_list_dict["File_name"] + '.txt', 'w'))
    print "file_list_dict is :"
    pprint.pprint(file_list_dict)
    capture_token_string = url + " ; " + token + " ; " + str(file_list_dict["NSSId"])
    target_url = open("/CAWS_pytest/URL_TOKEN_with_NSSId.txt", 'a+')
    target_url.write(str(capture_token_string))
    target_url.write("\n")
    target_url.close()
    return (file_list_dict["Status"], file_list_dict["NSSId"],
            (datetime.datetime.utcnow() - my_datetime).seconds, token)


def check_file_nssid_details(file_submit_log):
    """Verifies submitted file NSSId details - File Submission Test Phase 3
    :param file_submit_log: Submission submit log
    """
    username = file_submit_log["username"]
    password = file_submit_log["password"]
    file_list_dict = file_submit_log["file_list_dict"]["submission_metadata"]
    file_submit_result_dict = json.load(
        open(file_submit_log['tmp_data_directory'] + file_list_dict["File_name"] + '.txt'))
    nssId = file_submit_result_dict["NSSId"]
    submit_time = file_submit_result_dict["Submit_time"]
    url = file_submit_log["url"] + '/Users/Files/' + str(nssId)
    print "url and token for the query is :", url, ";", nssId
    base64string = base64.b64encode('%s:%s' % (username, password))
    headers = {
        'authorization': "Basic %s" % base64string,
        'cache-control': "no-cache"
    }
    response_dict = {}
    my_datetime = datetime.datetime.strptime(submit_time, '%Y-%m-%d-%H-%M-%S')
    delta = (datetime.datetime.utcnow() - my_datetime).seconds

    while ("captureModel" not in response_dict):
        print "even after ", delta, "seconds, NSSId details are not available. Will wait for 5 secs now"
        delta = (datetime.datetime.utcnow() - my_datetime).seconds
        time.sleep(5)
        response = requests.request("GET", url, headers=headers)
        print "response code is:", response, "and text is:", response.text
        response_dict = json.loads(response.text)
        response_dict = byteify(response_dict)

    response_dict = byteify(response_dict["captureModel"])
    pprint.pprint(response_dict)
    file_list_dict["IsMalicious"] = response_dict["IsMalicious"]
    file_list_dict["DetectionDate"] = response_dict["DetectionDate"]
    file_list_dict["Result_time"] = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H-%M-%S")
    file_list_dict['Time_delta'] = delta
    file_list_dict["NSSId"] = file_submit_result_dict["NSSId"]
    json.dump(file_list_dict, open(file_submit_log['tmp_data_directory'] + file_list_dict["File_name"] + '.txt', 'w'))
    return response_dict


print "program is done."