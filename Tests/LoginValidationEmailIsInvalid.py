"""
Check that validation message is thrown on login page when Email is invalid(not a@a.a)
"""
from selenium import webdriver

# SetUp
exec_path = "D:\\chromedriver.exe"
URL = "https://www.optibet.com/login"
driver = webdriver.Chrome(exec_path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

# Locate email and write invalid data(not a@a.a)
invalidData = "123"
emailInputElement = driver.find_element_by_name("email")
emailInputElement.send_keys(invalidData)

# click on Login button
login_css = ".cLMVUC"
login = driver.find_element_by_css_selector(login_css)
login.click()

# Validate error message
expected_email_ExceptionText = "Please enter a valid email"
email_Exception_css = ".Login__loginForm___2-7BA-scss > .Field__Wrapper-hr4dpn-0 > .Field__Info-hr4dpn-1"
actual_email_ExceptionText = driver.find_element_by_css_selector(email_Exception_css).text

if actual_email_ExceptionText == expected_email_ExceptionText:
    print("Email error message:" + actual_email_ExceptionText + " Is Correct")
else:
    print("Email error message:" + actual_email_ExceptionText + " Is Incorrect")
driver.quit()
