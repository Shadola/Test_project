"""
Here I'm going to Casino section and take first game from Isoftbet list

"""
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

# SetUp
exec_path = "D:\\chromedriver.exe"
URL = "https://www.optibet.com/login"
driver = webdriver.Chrome(exec_path)
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

# Send text to Email
email = "xakellax@hotmail.com"
inputElement = driver.find_element_by_name("email")
inputElement.send_keys(email)

# Send text to password
password = "Kalamala5"
inputElement = driver.find_element_by_name("password")
inputElement.send_keys(password)

# click on Login button
login_css = ".cLMVUC"
login = driver.find_element_by_css_selector(login_css)
login.click()

# Go to casino section
casinoButton_css = ".Welcome__link___2r67O-scss:nth-child(4) > .ButtonBase-t3o6yt-0"
casinoButton = driver.find_element_by_css_selector(".Welcome__link___2r67O-scss:nth-child(4) > .ButtonBase-t3o6yt-0")
casinoButton.click()

# Click on all providers
allProvidersButton_xpath = "//li[contains(.,'All providers')]"
allproviders = driver.find_element_by_xpath(allProvidersButton_xpath)
allproviders.click()

# Click on Isoftbet
isoftbet_xpath = "//li[contains(.,'iSoftBet')]"
isoftbet = driver.find_element_by_xpath(isoftbet_xpath)
isoftbet.click()

# mouse over and click on the first game in the list
action = ActionChains(driver)
gameThumb_css = ".GameThumb__game___3PJgg-scss:nth-child(1) .GameThumb__overlay___uVah1-scss"
game = driver.find_element_by_css_selector(gameThumb_css)
action.move_to_element(game).perform()
game.click()
print("game is running")
