from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

def load_page():
    driver = webdriver.Chrome()
    driver.get('http://localhost:8080/en/')
    return driver