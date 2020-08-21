"""
Check that forgot your password link is visible and sent you
to new dialog window container with title "Forgot you password?"

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

# Click on Forgot your password
forgotPassword_linkText = "Forgot your password?"
forgotPassword = driver.find_element_by_link_text(forgotPassword_linkText)
forgotPassword.click()

# Check that new dialog window container with title "Forgot you password?" is opened
forgotPasswordTitle_css = ".DialogTitle__DialogTitleContent-sc-1274mlf-0"
try:
    forgotPasswordTitle = driver.find_element_by_css_selector(forgotPasswordTitle_css)
    print("Forgot you password title is visible")
except NoSuchElementException:
    print("Forgot you password title is not found")
finally:
    driver.quit()
