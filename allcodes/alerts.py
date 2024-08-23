import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("../Driver/chromedriver.exe"))
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Alerts.html")

simple_alert_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[1]/a')
simple_alert_nav.click()
button1 = driver.find_element(By.XPATH, '//*[@id="OKTab"]/button')
button1.click()
ALert = driver.switch_to.alert
ALert.accept()

confirmation_alert_nav = driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div/div[1]/ul/li[2]/a')
confirmation_alert_nav.click()
button2 = driver.find_element(By.XPATH, '//*[@id="CancelTab"]/button')
button2.click()
ALert.dismiss()

text_alert_nav = driver.find_element(By.XPATH,'/html/body/div[1]/div/div/div/div[1]/ul/li[3]/a')
text_alert_nav.click()
button3 = driver.find_element(By.XPATH,'//*[@id="Textbox"]/button')
button3.click()
Alert.send_keys('QA1100')
Alert.accept()

time.sleep(5)