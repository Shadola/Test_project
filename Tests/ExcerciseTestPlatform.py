# Ignore this file, that's for future changes
"""
import unittest
from selenium import webdriver

class LoginSuccess(unittest.TestCase):
    @classmethod
    def setUp(inst):
        # create a new Chrome session
        exec_path = "D:\\chromedriver.exe"
        self.driver = webdriver.Chrome(exec_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def LoginOnSite(self):
        #Go to Login URL
        URL = "https://www.optibet.com/login"
        driver.get(URL)
        #Enter Email and Password
        email = "xakellax@hotmail.com"
        password = "Kalamala5"
        inputElement = driver.find_element_by_name("email")
        inputElement.send_keys(email)
        inputElement = driver.find_element_by_name("password")
        inputElement.send_keys(password)
        # click on Login button
        login_css = ".cLMVUC"
        login = driver.find_element_by_css_selector(login_css)
        login.click()
        # Check that u are logged IN
        login_css = ".cLMVUC"
        welcome = driver.find_element_by_css_selector(login_css)
        assert (welcome.text,"test")
    def tearDown(self):
        #close the browser windows
        self.driver.quit()
"""

