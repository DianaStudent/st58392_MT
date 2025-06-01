from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.error import UnexpectedAlertPresent
from selenium.webdriver.common.alert import Alert

class TestSeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_screenshots_description(self):
        # Navigate to the main URL
        self.driver.get("http://localhost:3000")

        # Check that the main UI components are present and visible
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header")))
        navigation_menu = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//nav[@role='navigation']/ul[contains(@class,'nav-links')][contains(@class,'container')]//li[contains(@class,'nav-link')]")))
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Select Category')]")))
        reset_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text,'Reset')])")))

        # Check that these elements exist and are visible
        self.assertTrue(header)