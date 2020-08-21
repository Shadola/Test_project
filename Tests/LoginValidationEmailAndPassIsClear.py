"""
Check that validation messages is thrown on login page when Password and Email value is cleared
"""
from selenium import webdriver

# SetUp
exec_path = "D:\\chromedriver.exe"
URL = "https://www.optibet.com/login"
driver = webdriver.Chrome(exec_path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

# Locate and clear email
emailInputElement = driver.find_element_by_name("email")
emailInputElement.clear()

# Locate and clear password
passwordInputElement = driver.find_element_by_name("password")
passwordInputElement.clear()

# click on Login button
login_css = ".cLMVUC"
login = driver.find_element_by_css_selector(login_css)
login.click()

# Validate email error message
expected_email_ExceptionText = "Email is required"
email_Exception_css = ".Login__loginForm___2-7BA-scss > .Field__Wrapper-hr4dpn-0 > .Field__Info-hr4dpn-1"
actual_email_ExceptionText = driver.find_element_by_css_selector(email_Exception_css).text

if actual_email_ExceptionText == expected_email_ExceptionText:
    print("Email error message:" + actual_email_ExceptionText + " Is Correct")
else:
    print("Email error message:" + actual_email_ExceptionText + " Is Incorrect")

# Validate password error message
expected_password_ExceptionText = "Password is required"
password_Exception_css = ".PasswordField__container___iXaqk-scss .Field__Info-hr4dpn-1"
actual_password_ExceptionText = driver.find_element_by_css_selector(password_Exception_css).text

if actual_password_ExceptionText == expected_password_ExceptionText:
    print("password error message:" + actual_password_ExceptionText + " Is Correct")
else:
    print("password error message:" + actual_password_ExceptionText + " Is Incorrect")
driver.quit()
