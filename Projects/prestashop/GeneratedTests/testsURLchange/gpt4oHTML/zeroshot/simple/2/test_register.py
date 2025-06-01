import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def generate_random_email(self):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(10)) + '@example.com'

    def test_register(self):
        driver = self.driver
        driver.get('http://localhost:8080/en/')

        # Navigate to registration page
        try:
            create_account_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Create account"))
            )
            create_account_link.click()
        except Exception as e:
            self.fail("Create account link not found or clickable: " + str(e))

        # Fill the registration form
        try:
            email = self.generate_random_email()
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='id_gender'][@value='1']"))
            ).click()
            
            driver.find_element(By.ID, 'field-firstname').send_keys("Test")
            driver.find_element(By.ID, 'field-lastname').send_keys("User")
            driver.find_element(By.ID, 'field-email').send_keys(email)
            driver.find_element(By.ID, 'field-password').send_keys("test@user1")
            
            optin_checkbox = driver.find_element(By.NAME, 'optin')
            psgdpr_checkbox = driver.find_element(By.NAME, 'psgdpr')
            newsletter_checkbox = driver.find_element(By.NAME, 'newsletter')
            customer_privacy_checkbox = driver.find_element(By.NAME, 'customer_privacy')
            
            optin_checkbox.click()
            psgdpr_checkbox.click()
            newsletter_checkbox.click()
            customer_privacy_checkbox.click()
            
            driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]").click()
            
        except Exception as e:
            self.fail("Failed to fill the registration form or click Save: " + str(e))

        # Confirm the user is registered by checking "Sign out" link presence
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Sign out"))
            )
        except Exception as e:
            self.fail("Registration failed, 'Sign out' link not present: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()