import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def generate_email(self):
        return f"test_{random.randint(100000, 999999)}@user.com"

    def test_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 2: Click the login link
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#_desktop_user_info a[href*='login']")))
        login_link.click()

        # Step 3: Click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 4: Fill the registration form
        gender_radio = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_radio.click()

        firstname_input = driver.find_element(By.ID, "field-firstname")
        firstname_input.send_keys("Test")

        lastname_input = driver.find_element(By.ID, "field-lastname")
        lastname_input.send_keys("User")

        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(self.generate_email())

        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("01/01/2000")

        # Step 5: Tick checkboxes
        terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "psgdpr")))
        terms_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        newsletter_checkbox.click()

        # Step 6: Submit the form
        submit_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit_button.click()

        # Step 7: Wait for redirect after login
        account_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.account")))

        # Step 8: Confirm successful login
        sign_out_button = driver.find_elements(By.CSS_SELECTOR, "a.logout")
        username_display = driver.find_elements(By.CSS_SELECTOR, "a.account span")

        if not sign_out_button or not username_display:
            self.fail("Login was not successful. 'Sign out' button or username not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()