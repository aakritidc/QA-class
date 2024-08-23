import time
import unittest

from driverpackage.drivers import Drive
from pages.loginpage import LoginPage
from pages.contactpage import Contact


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        driver = Drive()
        self.driver = driver.chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.demoblaze.com/")

    def test_w_contact(self):
        self.lp = LoginPage(self.driver)
        self.lp.login("testmorning", "test123")
        time.sleep(5)
        self.cp = Contact(self.driver)
        self.cp.contact("test@test.com","test", "This is test")
        time.sleep(5)
        self.driver.switch_to.alert.accept()


    def test_wo_contact(self):
        self.cp = Contact(self.driver)
        self.cp.contact("test@test.com", "test", "This is test")
        time.sleep(5)
        self.driver.switch_to.alert.accept()


if __name__ == '__main__':
    unittest.main()
