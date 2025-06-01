from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert
from unittest.mock import MagicMock
import time
import unittest
from selenium.webdriver.chrome.options import Options

class TestRegisterFunctionality(unittest.TestCase):
    def setUp(self):
        options = Options()
        options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)

    def tearDown(self):
        self.driver.quit()

    def test_register_functionality(self):
        email = "testuser1@fake.com"
        password = "test@user1"

        # Step 1: Fill in the required fields
        username_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='username']/parent::span/parent::input[1]")))
        self.driver.find_element_by_name("username").send_keys(email)

        phone_number_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='phone']/parent::span/parent::input[0]")))
        self.driver.find_element_by_name("phone").send_keys(email)

        # Step 2: Confirm the account
        terms_and_conditions_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='termsAndConditions']/parent::span/parent::input[1]")))
        self.driver.find_element_by_name("termsAndConditions").click()

        # Step 3: Agree to the privacy policy
        privacy_policy_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='privacyPolicy']/parent::span/parent::input[1]")))
        self.driver.find_element_by_name("privacyPolicy").click()

        # Step 4: Confirm the account
        confirm_account_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='confirmAccount']/parent::span/parent::input[1]")))
        self.driver.find_element_by_name("confirmAccount").click()

        # Check if the "Sign out" button appears
        sign_out_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='btn btn-primary btn-sm px-2 py-0 text-white']")