"""
Check that validation message is thrown on login page when Email or Password is wrong(valid data)
Will check only Wrong password on real email, because I don't know which email data is not exist on db side
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

# click on Login button
login_css = ".cLMVUC"
login = driver.find_element_by_css_selector(login_css)
login.click()

# Validate password error message
expected_password_ExceptionText = "The username or password is incorrect"
password_Exception_css = ".PasswordField__container___iXaqk-scss .Field__Info-hr4dpn-1"
actual_password_ExceptionText = driver.find_element_by_css_selector(password_Exception_css).text

if actual_password_ExceptionText == expected_password_ExceptionText:
    print("password error message:" + actual_password_ExceptionText + " Is Correct")
else:
    print("password error message:" + actual_password_ExceptionText + " Is Incorrect")
driver.quit()
