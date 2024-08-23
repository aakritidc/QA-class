import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../Driver/chromedriver.exe"))
driver.maximize_window()
driver.get("https://www.demoblaze.com/")

nav_login = driver.find_element(By.ID, "login2")
nav_login.click()
driver.implicitly_wait(10)
uname = driver.find_element(By.ID,"loginusername")
uname.send_keys("testmorning")
pwd = driver.find_element(By.ID, "loginpassword")
pwd.send_keys("test123")
button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
button.click()
time.sleep(10)