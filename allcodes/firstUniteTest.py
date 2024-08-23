import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class MyTestCase(unittest.TestCase):


    def setUp(self) -> None:
        print("I am a setup")
        self.driver = webdriver.Chrome(service=Service("../Driver/chromedriver.exe"))
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def test_something(self):
        print("i am a test")
        driver = self.driver
        nav_login = driver.find_element(By.ID, "login2")
        nav_login.click()
        driver.implicitly_wait(10)
        uname = driver.find_element(By.ID, "loginusername")
        uname.send_keys("testmorning")
        pwd = driver.find_element(By.ID, "loginpassword")
        pwd.send_keys("test123")
        button = driver.find_element(By.XPATH, '//*[@id="logInModal"]/div/div/div[3]/button[2]')
        button.click()
        time.sleep(10)
        actual_result = driver.find_element(By.XPATH,'//*[@id="nameofuser"]').text

        self.assertEqual("Welcom testmorning", actual_result, "There is some error")




    def tearDown(self) -> None:
        self.driver.close()
        print("We are done of testing")




if __name__ == '__main__':
    unittest.main()
