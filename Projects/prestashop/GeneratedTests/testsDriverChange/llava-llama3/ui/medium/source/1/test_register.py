import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class TestRegistrationPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_registration_page(self):
        driver = self.driver

        # Open the registration page
        register_page_url = 'http://localhost:8080/en/'
        driver.get(register_page_url)

        # Confirm the presence of key interface elements
        header = WebDriverWait(driver, 20).until(
            By.XPATH, "//header[contains(text(), 'Sign Up')]")
        )
        form_fields = WebDriverWait(driver, 20).until(
            By.XPATH, "//form[@id='registration-form']")
        )
        buttons = WebDriverWait(driver, 20).until(
            By.XPATH, "//button[contains(text(), 'Create Account')]/span[1]"
        )

        # Interact with the elements
        button = WebDriverWait(driver, 20).until(
            By.XPATH,