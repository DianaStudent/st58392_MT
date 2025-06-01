from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

class TestSeleniumTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_selenium_test(self):
        driver = self.driver
        base_url = "http://localhost:8080/en/"
        login_path = base_url + "login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art"
        register_path = base_url + "registration"

        driver.get(base_url)

        # Confirm the presence of key interface elements
        self.assertTrue("Shop" in driver.title)
        self.assertTrue("Cart" in driver.title)
        self.assertTrue("My account" in driver.title)
        self.assertTrue("Wishlists" in driver.title)

        # Test interacting with a button and checking the UI updates visually
        try:
            button = WebDriverWait(driver, 20).until(
                By.XPATH,