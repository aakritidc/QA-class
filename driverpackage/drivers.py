from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class Drive:
    def chrome(self):
        self.driver = webdriver.Chrome(service=Service("../Driver/chromedriver.exe"))
        return self.driver