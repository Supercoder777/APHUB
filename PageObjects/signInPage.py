from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By



class signInPage:
    def __init__(self, driver):
        self.driver = driver

        #driver.find_element(By.ID, "edit-name").send_keys("samuel4luve@yahoo.com")
        #driver.find_element(By.CSS_SELECTOR, "#edit-pass").send_keys("zAddi623_")
        #driver.find_element(By.CSS_SELECTOR, "#edit-submit").click()

        emailsection = (By.ID, "edit-name")
        passwordSection = (By.CSS_SELECTOR, "#edit-pass")
        submit = (By.CSS_SELECTOR, "#edit-submit")


        def emailSection(self):
            return self.driver.find_element(*signInPage.email)

        def passwordSection(self):
            return self.driver.find_element(*signInPage.password)

        def submit(self):
            return self.driver.find_element(*signInPage.submit)