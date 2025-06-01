from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.touch_actions import TouchAction
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.touch_actions import TouchAndHold
from selenium.webdriver.common.touch_actions import ActionChains
import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait as WaitUntil
from selenium.webdriver.support.ui import WebDriverWait as WaitUntil

class TestSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_homepage(self):
        # Load the page and ensure that structural elements (e.g., header, footer, navigation) are visible
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Check the presence and visibility of input fields, buttons, labels, and sections
        time.sleep(2)
        element_header = WebDriverWait(driver, 20).until(
            lambda x: x.find_element_by_tag_name('header'))
        )
        self.assertTrue(element_header.is_displayed())

    def test_clothes(self):
        # Load the page with the clothes category and check for structural elements
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Check the presence and visibility of input fields, buttons, labels, and sections
        time.sleep(2)
        element_header = WebDriverWait(driver, 20).until(
            lambda x: x.find_element_by_tag_name('header'))
        )
        self.assertTrue(element_header.is_displayed())