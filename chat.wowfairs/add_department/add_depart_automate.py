from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
#from selenium.webdriver.support.select import Select
import openpyxl 

wb_obj = openpyxl.load_workbook("C:\\Users\\BP\\Desktop\\chat.wowfairs\\add_department\\department.xlsx")
sheet_obj = wb_obj.active

user_name = "gaurav.raheja@outlook.com"
password = "asdf@1234"

driver_chrome = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
driver_chrome.get("https://chat.wowfairs.com/login")
driver_chrome.maximize_window()
# it will maximize the window size, bydefault the window size is not maximize

element = driver_chrome.find_element_by_xpath("/html/body/div/main/div/div/div/div/div[2]/form/div[1]/div/input")
element.send_keys(user_name)
# it will search for the element id inputPassword
element = driver_chrome.find_element_by_xpath("/html/body/div/main/div/div/div/div/div[2]/form/div[2]/div/input")
element.send_keys(password) # it will pass the string value assigned to password variable
time.sleep(2)
    
#click on remember me check box
element = driver_chrome.find_element_by_xpath("/html/body/div/main/div/div/div/div/div[2]/form/div[3]/div/label")
element.click()
# it will press the enter after values have been entered
element = driver_chrome.find_element_by_xpath("/html/body/div/main/div/div/div/div/div[2]/form/div[4]/div/button") 
element.click()
time.sleep(4)

# click on department
element = driver_chrome.find_element_by_xpath("/html/body/div[4]/section/aside/nav/ul/li[3]/a")
element.click()
time.sleep(2)

# click on add new
element = driver_chrome.find_element_by_xpath("/html/body/div[4]/section/aside/nav/ul/li[3]/ul/li[1]/a")
element.click()
time.sleep(2)

for i in range(5,131):
    
        alpha = sheet_obj.cell(row = i, column = 1)
        a = alpha.value
        print(a)
  

        #enter the value in department
        element = driver_chrome.find_element_by_xpath("/html/body/div[3]/section/section/div[2]/div/div/div/div[2]/div/form/div[1]/div/input")
        element.send_keys(a) 

        #enter the value in description
        element = driver_chrome.find_element_by_xpath("/html/body/div[3]/section/section/div[2]/div/div/div/div[2]/div/form/div[2]/div/textarea")
        element.send_keys(a) # it will pass the string value assigned 

        #click on save
        element = driver_chrome.find_element_by_xpath("/html/body/div[3]/section/section/div[2]/div/div/div/div[2]/div/form/div[3]/div/button[2]")
        element.click()
        time.sleep(3)
    
        
        























