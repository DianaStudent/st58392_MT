import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.assertions import assert_that
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager import DriverManager
import time

class TestRegistrationPage(unittest.TestCase):
    def setUp(self):
        driver = webdriver.Chrome()
        self.driver = driver

    def tearDown(self):
        self.driver.quit()

    def test_register_page(self):
        self.driver.get("http://max/register?returnUrl=%2F")

        assert_that(self.driver, 'page is loaded', lambda x: x.current_url == 'http://max/register?returnUrl=%2F')

        first_name_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']")))
        last_name_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='lastName']")))
        email_address_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@name='emailAddress']")))
        terms_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[@for='termsOfService']/span")))

        # Interact with key UI elements
        first_name_field.send_keys('First Name')
        last_name_field.send_keys('Last Name')
        email_address_field.send_keys('email@example.com')
        terms_checkbox.click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements((By.XPATH,