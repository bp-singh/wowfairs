from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
#from selenium.webdriver.support.select import Select 



driver_chrome = webdriver.Chrome("C:\chromedriver_win32\chromedriver.exe")
driver_chrome.get("https://indiasoft.wowfairs.com/")
driver_chrome.maximize_window()
# it will maximize the window size, bydefault the window size is not maximize

for i in range(1,1000):
    for j in range(1,1000):
        try:

user_name = "visitor@example.com"
password = "asdf@1234"

element = driver_chrome.find_element_by_id("inputEmail")
element.send_keys(user_name)
# it will search for the element id inputPassword
element = driver_chrome.find_element_by_id("inputPassword")
element.send_keys(password) # it will pass the string value assigned to password variable
time.sleep(2)
    
#click on remember me check box
element = driver_chrome.find_element_by_xpath("/html/body/app-root/app-content-layout/div/div/div/app-landing-page/section/div/div[2]/div[2]/app-login/section/div/div/form/div[3]/label")
element.click()
element.send_keys(Keys.RETURN) # it will press the enter after values have been entered
time.sleep(4)   
    
# searching for element having option logout
element = driver_chrome.find_element_by_id("apps")
element.click()
time.sleep(3)

# search for drop down logout and then click logout
element = driver_chrome.find_element_by_xpath("/html/body/app-root/app-full-layout/div/app-navbar/section/nav/div/div[4]/div/div/div/div/a[2]")
element.click()
time.sleep(3)

driver_chrome.quit()




















 
