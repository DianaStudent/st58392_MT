from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import random

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_registration(self):
        driver = self.driver

        # Step 1: Click the login link from the top navigation
        login_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))
        )
        login_link.click()

        # Step 2: On the login page, click on the register link
        register_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))
        )
        register_link.click()

        # Step 3: Fill the registration form
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "field-id_gender-1"))
        ).click()

        driver.find_element(By.ID, "field-firstname").send_keys("Test")
        driver.find_element(By.ID, "field-lastname").send_keys("User")

        # Generate a dynamic email
        random_number = random.randint(100000, 999999)
        email = f"test_{random_number}@user.com"
        driver.find_element(By.ID, "field-email").send_keys(email)

        driver.find_element(By.ID, "field-password").send_keys("test@user1")
        driver.find_element(By.ID, "field-birthday").send_keys("01/01/2000")

        # Check the necessary checkboxes
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        if not privacy_checkbox.is_selected():
            privacy_checkbox.click()

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        if not newsletter_checkbox.is_selected():
            newsletter_checkbox.click()

        # Step 4: Submit the registration form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # Step 5: Confirm registration success by checking for "Sign out"
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Sign out"))
            )
        except Exception as e:
            self.fail(f"Registration failed. 'Sign out' not found on page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()