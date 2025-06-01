import unittest
from selenium import webdriver
from webdriver_manager import ChromeDriverManager
from time import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

class MyTest(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome(ChromeDriverManager().get_driver_info())
        driver.get("https://example.com")

    def tearDown(self):
        pass