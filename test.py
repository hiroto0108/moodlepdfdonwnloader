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



ID = input('Enter your ID : ') # Please fill in your e-mail address at keio.jp (yukichi.fukuzawa@keio.jp) 
PW = input('Enter your Password : ')# Please fill in your password in keio.jp

name = input('Enter directory name : ')
directory_name = '/Users/nakatahiroto/moodledownroader/{}'.format(name) 
os.mkdir(directory_name)
os.chdir(directory_name)
# Optional settings of chrome driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--kiosk-printing')

# Boot chrome driver
driver = webdriver.Chrome(options=options)
driver.set_page_load_timeout(15) # Time out 15 sec

# GET (HTML Page)
driver.get("https://moodle.cis.kit.ac.jp/login/index.php")
time.sleep(5)

# Find elements and POST (send keys to the input tag)
id_element = driver.find_element(By.NAME,"j_username")
id_element.send_keys(ID)
pw_element = driver.find_element(By.NAME,"j_password")
pw_element.send_keys(PW)


# Click login button
login_button = driver.find_element(By.NAME,"_eventId_proceed")
login_button.click()
time.sleep(5)
c_url = input('Enter cource URL  : ')
driver.get(c_url)

elements = driver.find_elements(By.XPATH,"//a[@href]")
links = [i.get_attribute('href') for i in elements]
for url in links:
    parse = urlparse(url)
    filepath = parse.path
    if filepath == "/mod/resource/view.php":
        driver.get(url)
        driver.execute_script('window.print();')
        print("file downloading...")
        time.sleep(2)

print("Complete!")
#driver.execute_script('window.print();')
time.sleep(3)



driver.quit()