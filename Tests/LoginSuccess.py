"""
Here im logging in and check that im on succeed log in page
I could take login token from cookies, but used element from login suceed page to verify

"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# SetUp
exec_path = "D:\\chromedriver.exe"
URL = "https://www.optibet.com/login"
driver = webdriver.Chrome(exec_path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

# Send text to Email
email_name = "email"
email = "xakellax@hotmail.com"
inputElement = driver.find_element_by_name(email_name)
inputElement.send_keys(email)

# Send text to password
password_name = "password"
password = "Kalamala5"
inputElement = driver.find_element_by_name(password_name)
inputElement.send_keys(password)

# click on Login button
login_css = ".cLMVUC"
login = driver.find_element_by_css_selector(login_css)
login.click()

# Check that u are logged IN by element Deposit on succeed login page
depositButton_css = ".fFeWgx"
try:
    deposit_button = driver.find_element_by_css_selector(depositButton_css)
    print("You are logged in and Deposit button is visible")
except NoSuchElementException:
    print("Deposit button not found")
finally:
    driver.quit()
