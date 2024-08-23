from selenium.webdriver.common.by import By

from locators.locator import Locate


class Contact:
    def __init__(self,driver):
        self.driver = driver
        self.lc = Locate()

    def contact(self,email,name,msg):
        driver = self.driver
        nav_contact = driver.find_element(By.XPATH, self.lc.nav_contact_xpath)
        nav_contact.click()
        driver.implicitly_wait(10)
        em = driver.find_element(By.ID, self.lc.contact_email_id)
        em.send_keys(email)
        nm = driver.find_element(By.ID, self.lc.contact_name_id)
        nm.send_keys(name)
        message = driver.find_element(By.XPATH, self.lc.contact_message_xpath)
        message.send_keys(msg)
        button = driver.find_element(By.XPATH, self.lc.contact_button_xpath)
        button.click()