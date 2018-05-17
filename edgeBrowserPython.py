# AutomatEdgeBrowser
#Automate edge browser using python
#os build version important
import os
from selenium import webdriver

# create new Edge session
dir = os.path.dirname(__file__)
edge_path = r"C:\Users\Niranjan\Downloads\MicrosoftWebDriver.exe"
driver = webdriver.Edge(edge_path)
driver.implicitly_wait(10)
# driver.maximize_window()

driver.get("https://www.freelancer.in/")

#login_button = driver.find_element_by_class_name("LandingHeader-authBtn")
login_button = driver.find_element_by_class_name("LoginSection-btn")
login_button.click()
