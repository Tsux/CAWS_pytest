import pytest, datetime, time

def test_sum(var1, var2):
    assert 4 == (var1 + var2)
    return ()

def test_take_sum(var2):
    assert 2 == var2
    my_sum = 3
    print "my_sum is:" , my_sum
    return (3 + my_sum)

    
# @pytest.fixture(scope="session")
# def file_submit_log():
#     utc_datetime = datetime.datetime.utcnow()
#     #utc_datetime.strftime("%Y-%m-%d %H:%M:%S")
#     #Today_Date_time = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
#     Today_Date_time = utc_datetime.strftime("%Y-%m-%d-%H-%M-%S")
#     #Today_Date = datetime.datetime.now().strftime("%Y-%m-%d")
#     Today_Date = utc_datetime.strftime("%Y-%m-%d")
#     print "Todays date is:" , Today_Date
#     print "Todays date n time  is:" , Today_Date_time
#     FILE_SUBMIT_TOKEN_FILE = open("/Users/apatel/Documents/workspace/File_Submit_Token_" + Today_Date + ".txt", 'w')
#     yield (Today_Date , Today_Date_time, FILE_SUBMIT_TOKEN_FILE)
#     #yield Today_Date_time
#     #yield FILE_SUBMIT_TOKEN_FILE   
#     FILE_SUBMIT_TOKEN_FILE.close()
#     

@pytest.fixture(scope="module")
def start_up_config(request):
    utc_datetime = datetime.datetime.utcnow()
    exploited_nssids = "/Users/apatel/Documents/workspace/pcap_download/exploited_nssid_"+str(utc_datetime.strftime("%Y-%m-%d-%H-%M-%S"))+".txt"
    start_up_config_dict = {"utc_datetime" : utc_datetime , "exploited_nssids" : exploited_nssids}
    return start_up_config_dict

def test_write_file_submit_token(file_submit_log):
    time.sleep(10)
    print "file_submit_log is :" , file_submit_log
    print file_submit_log[0]
    print file_submit_log[1]
    print file_submit_log[2]

    file_submit_log[2].write(str(file_submit_log[0]) + "hi" + str(file_submit_log[1]))
    assert True
    

@pytest.fixture(scope="module")
def var1():
    return 2

@pytest.fixture(scope="module")
def var2():
    return 2


#pytest --html=$(date +"%Y%m%d%H%M")_html_report.html   --capture=no