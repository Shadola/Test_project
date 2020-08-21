"""
Check that account is blocked with message
"Your account has been blocked, please contact support for more info" after 6 attempts in a row
"""
from selenium import webdriver

# SetUp
exec_path = "D:\\chromedriver.exe"
URL = "https://www.optibet.com/login"
driver = webdriver.Chrome(exec_path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

# Locate email and write value that exist on db side
emailValue = "xakellax@hotmail.com"
emailInputElement = driver.find_element_by_name("email")
emailInputElement.send_keys(emailValue)

# Write wrong value in password
password_name = "password"
wrongPassword = "123"
inputElement = driver.find_element_by_name("password")
inputElement.send_keys(wrongPassword)

# click on Login button 6 times in a row
login_css = ".cLMVUC"
login = driver.find_element_by_css_selector(login_css)
blockAttempts = 0
while True:
    login.click()
    blockAttempts += 1
    print("Attempt number:"+str(blockAttempts))
    if blockAttempts == 6:
        break
# Validate your account is blocked error message
expected_password_ExceptionText = "Your account has been blocked, please contact support for more info"
password_Exception_css = ".PasswordField__container___iXaqk-scss .Field__Info-hr4dpn-1"
actual_password_ExceptionText = driver.find_element_by_css_selector(password_Exception_css).text

if actual_password_ExceptionText == expected_password_ExceptionText:
    print("error message:" + actual_password_ExceptionText + " Is Correct")
else:
    print("error message:" + actual_password_ExceptionText + " Is Incorrect")
driver.quit()
