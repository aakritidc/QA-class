from selenium.webdriver.common.by import By

from locators.locator import Locate


class LoginPage:
    def __init__(self,driver):
        self.driver = driver
        self.lc = Locate()

    def login(self,usname, pwwd):
        driver = self.driver
        nav_login = driver.find_element(By.ID, self.lc.nav_login_id)
        nav_login.click()
        driver.implicitly_wait(10)
        uname = driver.find_element(By.ID, self.lc.uname_id)
        uname.send_keys(usname)
        pwd = driver.find_element(By.ID, self.lc.pwd_id)
        pwd.send_keys(pwwd)
        button = driver.find_element(By.XPATH, self.lc.login_button_xpath)
        button.click()