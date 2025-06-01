import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
import uuid

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.maximize_window()

    def test_register_user(self):
        driver = self.driver
        driver.get('http://localhost:8080/')  # Base URL should be set accordingly

        # Wait for the Cookie Consent button and click it
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            self.fail("Cookie consent button not found or clickable")

        # Navigate to the registration page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_button.click()

            register_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Register"))
            )
            register_link.click()
        except:
            self.fail("Register link not found or clickable")

        # Fill the registration form
        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "email"))
            )
            password_input = driver.find_element(By.NAME, "password")
            repeat_password_input = driver.find_element(By.NAME, "repeatPassword")
            first_name_input = driver.find_element(By.NAME, "firstName")
            last_name_input = driver.find_element(By.NAME, "lastName")

            email = f"test_{uuid.uuid4().hex[:6]}@user.com"
            password = "test**11"

            email_input.send_keys(email)
            password_input.send_keys(password)
            repeat_password_input.send_keys(password)
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")

            # Select a country
            country_select = driver.find_element(By.XPATH, "//select[@name='country']/option[text()='Canada']")
            country_select.click()

            # Select a state
            state_select = driver.find_element(By.XPATH, "//select[@name='state']/option[@value='QC']")
            state_select.click()

            register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
            register_button.click()

        except:
            self.fail("Error in filling out the registration form or elements not found")

        # Wait for redirection to "/my-account" page
        try:
            WebDriverWait(driver, 20).until(EC.url_contains("/my-account"))
        except:
            self.fail("Failed to redirect to '/my-account' after registration")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()