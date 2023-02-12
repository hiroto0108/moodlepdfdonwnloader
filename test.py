import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse
import chromedriver_binary
import os
import json 

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local",
            "account":"",
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}

#file pointer
f = open('user_info.txt', 'r')

#input user_information to list 
USERDATALIST = f.readlines() 
c_url = input('Enter cource URL  : ')
name = input('Enter directory name : ')
#make directory to save the pdf files
c_directory = os.getcwd()
directory_name = c_directory + '\\' + name
print(directory_name)
if os.path.exists(directory_name):
    print("This directory name has been exited.")
else:
    os.mkdir(directory_name)

# Optional settings of chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    "download.default_directory": directory_name,
    "printing.print_preview_sticky_settings.appState": json.dumps(appState),
    'download.prompt_for_download': False,
    "plugins.always_open_pdf_externally": True,
})
options.add_argument('--kiosk-printing')
options.add_argument('--headless')
# Boot chrome driver
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(15) # Time out 15 sec
driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
driver.execute("send_command", {
    'cmd': 'Page.setDownloadBehavior',
    'params': {
        'behavior': 'allow',
        'downloadPath': directory_name # ダウンロード先
    }
})
# GET (HTML Page)
driver.get(USERDATALIST[2])
time.sleep(5)

# Find elements and POST (send keys to the input tag)
id_element = driver.find_element(By.NAME,"j_username")
id_element.send_keys(USERDATALIST[0])
pw_element = driver.find_element(By.NAME,"j_password")
pw_element.send_keys(USERDATALIST[1])


# Click login button
print("Login Successed")
time.sleep(5)

#access to cource page
driver.get(c_url)

#get the links to class pdf files
elements = driver.find_elements(By.XPATH,"//a[@href]")
links = [i.get_attribute('href') for i in elements]
for url in links:
    parse = urlparse(url)
    filepath = parse.path
    if filepath == "/mod/resource/view.php":
        
        driver.get(url)
        
        #download a pdf
        
        print("file downloading...")
        time.sleep(3)

print("Complete!")

time.sleep(3)

driver.quit()