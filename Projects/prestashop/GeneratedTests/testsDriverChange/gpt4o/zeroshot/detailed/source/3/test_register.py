import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_user_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get("http://localhost:8080/en/")

        # Step 2: Click the login link
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="login?back"]')))
        login_link.click()

        # Step 3: Click the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Create one here")))
        register_link.click()

        # Step 4: Fill in the registration form
        gender_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_mr.click()

        firstname_input = driver.find_element(By.ID, "field-firstname")
        firstname_input.send_keys("Test")

        lastname_input = driver.find_element(By.ID, "field-lastname")
        lastname_input.send_keys("User")

        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(f"test_{int(time.time())}@user.com")

        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("01/01/2000")

        # Step 5: Tick checkboxes
        checkbox_privacy = driver.find_element(By.NAME, "customer_privacy")
        checkbox_privacy.click()

        checkbox_terms = driver.find_element(By.NAME, "psgdpr")
        checkbox_terms.click()

        # Step 6: Submit the registration form
        save_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        save_button.click()

        # Step 7 & 8: Check for successful login
        user_info = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#_desktop_user_info')))
        self.assertIn("Sign out", user_info.text, "Sign out button not found, registration might have failed.")
        self.assertIn("Test User", user_info.text, "Username not displayed after registration.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()