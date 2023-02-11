import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse
import os
import platform
import sys

#file pointer
f = open('user_info.txt', 'r')

#input user_information to list 
USERDATALIST = f.readlines() 
c_url = input('Enter cource URL  : ')
name = input('Enter directory name : ')
#make directory to save the pdf files
c_directory = os.getcwd()
directory_name = c_directory + '/' + name
os.mkdir(directory_name)

# Optional settings of chrome driver
options = webdriver.ChromeOptions()
options.add_experimental_option('prefs', {
    'download.default_directory': directory_name
})
options.add_argument('--headless')
options.add_argument('--kiosk-printing')
os.chdir(directory_name)

# Boot chrome driver
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(15) # Time out 15 sec

# GET (HTML Page)
driver.get(USERDATALIST[2])
time.sleep(5)

# Find elements and POST (send keys to the input tag)
id_element = driver.find_element(By.NAME,"j_username")
id_element.send_keys(USERDATALIST[0])
pw_element = driver.find_element(By.NAME,"j_password")
pw_element.send_keys(USERDATALIST[1])


# Click login button
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
        driver.execute_script('window.print();')
        print("file downloading...")
        time.sleep(2)

print("Complete!")

time.sleep(3)

driver.quit()