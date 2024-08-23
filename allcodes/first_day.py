from selenium import webdriver
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service("../Driver/chromedriver.exe"))
driver.maximize_window()
driver.get("https://bishalkarki.xyz")