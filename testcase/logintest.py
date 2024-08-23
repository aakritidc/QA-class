import time
import unittest

from selenium.webdriver.common.by import By

from driverpackage.drivers import Drive
from pages.loginpage import LoginPage

class MyTestCase(unittest.TestCase):

    def setUp(self):
        driver = Drive()
        self.driver = driver.chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")


    def test_positive_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("testmorning","test123")
        time.sleep(10)
        actual_result = self.driver.find_element(By.XPATH, '//*[@id="nameofuser"]').text

        self.assertEqual("Welcome testmorning", actual_result, "There is some error")

    def test_negative_login(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("testmorning", "test12")
        time.sleep(10)
        self.driver.switch_to.alert.accept()
        time.sleep(10)

    def tearDown(self) -> None:
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
