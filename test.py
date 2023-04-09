import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from urllib.parse import urlparse
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os
import platform
import sys



INITIATE_INFO_LIST = ["",""]
USERDATALIST = ["",""]
URLFOLDER = [""]

#definition Function

#show error message
def errorpopup(ERRORMESSAGE):
    root = Tk()
    root.title('Error')

    # Frame as widget container
    frame1 = ttk.Frame(root)
    frame1.grid()
    # Label 1
    label1 = ttk.Label(
        frame1,
        text=ERRORMESSAGE,
        padding=(20)) # (left, top, right, bottom)
    label1.grid(row=0, column=1)

    frame2 = ttk.Frame(frame1, padding=(0, 5))
    frame2.grid(row=2, column=1, sticky=W)

    button1 = ttk.Button(
        frame2, text='OK',
        command=lambda:[sys.exit(), root.quit()]
    )
    button1.pack(side=BOTTOM)
        
    root.mainloop()
    
    time.sleep(10000)

#MessageBox
def Messagebox(MESSAGE):
    root = Tk()
    root.title('Progress')

    # Frame as widget container
    frame1 = ttk.Frame(root)
    frame1.grid()
    # Label 1
    label1 = ttk.Label(
        frame1,
        text=MESSAGE,
        padding=(20)) # (left, top, right, bottom)
    label1.grid(row=0, column=1)

    frame2 = ttk.Frame(frame1, padding=(0, 5))
    frame2.grid(row=2, column=2, sticky=W)

    button1 = ttk.Button(
        frame2, text='OK',
        command=lambda:[sys.exit(),root.quit()]
    )
    button1.pack(side=BOTTOM)
        
    root.mainloop()


#make directory to save the pdf files
def makedirectory(FOLDERNAME):
    c_directory = sys.argv[0]
    
    directory_name = c_directory.replace("test",FOLDERNAME)
    #directory_name = c_directory + '/' + FOLDERNAME
    
    print(directory_name)
    if os.path.exists(directory_name):
        #errorpopup('This name folder has been existed.Please chage name!')
        directory_name = makedirectoryforce(1,directory_name)
        return directory_name
    else:
        os.mkdir(directory_name)
        return directory_name

#make directory there is same name
def makedirectoryforce(n,DIRECTORYNAME):
    if os.path.exists(DIRECTORYNAME + "(" + str(n) + ")"):
        n+=1
        DIRECTORYNAME = makedirectoryforce(n,DIRECTORYNAME)
        return DIRECTORYNAME
    else:
        os.mkdir(DIRECTORYNAME + "(" + str(n) + ")")
        return DIRECTORYNAME + "(" + str(n) + ")"

#get Information for Initiate Settings
def get_initiate_info():
    #input cource URL and directoryname
    root = Tk()
    root.title('Initiate Setting')
    root.resizable(False, False)
    frame1 = ttk.Frame(root, padding=(32))
    frame1.grid()

    label1 = ttk.Label(frame1, text='Cource URL', padding=(5, 2))
    label1.grid(row=0, column=0, sticky=E)

    label2 = ttk.Label(frame1, text='Folder name', padding=(5, 2))
    label2.grid(row=1, column=0, sticky=E)

    label3 = ttk.Label(frame1, text='ID', padding=(5, 2))
    label3.grid(row=2, column=0, sticky=E)

    label4 = ttk.Label(frame1, text='Password', padding=(5, 2))
    label4.grid(row=3, column=0, sticky=E)
    #make frame to input cource URL
    #c_url = input('Enter cource URL  : ')
    c_url = StringVar()
    c_url_entry = ttk.Entry(
        frame1,
        textvariable=c_url,
        width=20
    )
    c_url_entry.grid(row=0, column=1)

    #make frame to input cource URL
    #name = input('Enter directory name : ')
    name = StringVar()
    name_entry = ttk.Entry(
        frame1,
        textvariable=name,
        width=20
    )
    name_entry.grid(row=1, column=1)
    
    #make frame to input ID
    #c_url = input('Enter cource URL  : ')
    id = StringVar()
    id_entry = ttk.Entry(
        frame1,
        textvariable=id,
        width=20
    )
    id_entry.grid(row=2, column=1)

    #make frame to input Password
    #name = input('Enter directory name : ')
    password = StringVar()
    password_entry = ttk.Entry(
        frame1,
        textvariable=password,
        width=20,
        show="*"
    )
    password_entry.grid(row=3, column=1)
    

    frame2 = ttk.Frame(frame1, padding=(0, 5))
    frame2.grid(row=4, column=1, sticky=W)
        

    button1 = ttk.Button(
        frame2, text='OK',
        command=lambda:[root.quit(),makelist(1,name.get(),c_url.get()),makelist(2,id.get(),password.get()),downloadfile()]
    )
    button1.pack(side=LEFT)

    button2 = ttk.Button(frame2, text='Cancel', command=lambda:[sys.exit(), root.quit()])
    button2.pack(side=LEFT)
    
    #display mainwindow
    root.mainloop()

#make List od Informaton to have info in Function    
def makelist(type,first,second):
    if type == 1:
        INITIATE_INFO_LIST[0] = makedirectory(first)
        INITIATE_INFO_LIST[1] = second
    else:
        USERDATALIST[0]= first
        USERDATALIST[1]= second
 

    
def downloadfile():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('prefs', {
        'download.default_directory': INITIATE_INFO_LIST[0],
        'download.prompt_for_download': False,
        "plugins.always_open_pdf_externally": True,
    })
    options.add_argument('--headless')
    options.add_argument('--kiosk-printing')
    os.chdir(INITIATE_INFO_LIST[0])
    print("folder change done")
    # Boot chrome driver
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30) # Time out 30 sec
    # GET (HTML Page)
    driver.get(INITIATE_INFO_LIST[1])
    time.sleep(5)


    # Find elements and POST (send keys to the input tag)
    id_element = driver.find_element(By.NAME,"j_username")
    id_element.send_keys(USERDATALIST[0])
    pw_element = driver.find_element(By.NAME,"j_password")
    pw_element.send_keys(USERDATALIST[1])

    #get current URL for checking page_changed
    cur_url = driver.current_url
    
    # Click login button
    login_button = driver.find_element(By.NAME,"_eventId_proceed")
    login_button.click()
    time.sleep(5)
    
    #check URL
    now_url = driver.current_url
    if(now_url != cur_url):
        messagebox.showinfo("login", "Login Complete!")
        print("access done")
    else:
        errorpopup("Fail Access:Please check network access and try one more!")
    
    time.sleep(2)
    #get the links to class pdf files
    elements = driver.find_elements(By.XPATH,"//a[@href]")
    links = [i.get_attribute('href') for i in elements]
    print("page links get done")
    for url in links:
        parse = urlparse(url)
        filepath = parse.path
        if filepath == "/mod/resource/view.php":
            driver.get(url)
            #download a pdf
            driver.execute_script('window.print();')
            print("file downloading...")
            time.sleep(2)
    driver.quit()
    Messagebox("File download complete!")
        
        

    
#file pointer
#f = open('user_info.txt', 'r')

#input user_information to list 
#USERDATALIST = f.readlines() 

#GUI
#get initiate info and make directory
get_initiate_info()

# Optional settings of chrome driver


#get identify infomation
#getuserinfo()


#getcource()
#access to cource page

#messagebox.showinfo("download","File download Complete!")