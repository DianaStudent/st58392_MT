import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://localhost:8080/en/"

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage
        driver.get(self.base_url + "/en/")

        # Step 2: Click the login link from the top navigation
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        login_link.click()

        # Step 3: On the login page, click on the register link
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 4: Fill in the registration form
        gender_radio = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        gender_radio.click()

        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.ID, "field-lastname")
        last_name_input.send_keys("User")

        email_input = driver.find_element(By.ID, "field-email")
        dynamic_email = f"test_{random.randint(100000, 999999)}@user.com"
        email_input.send_keys(dynamic_email)

        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("01/01/2000")

        # Step 5: Tick checkboxes for privacy, newsletter, terms, etc.
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        newsletter_checkbox.click()

        # Step 6: Submit the registration form
        submit_button = driver.find_element(By.CSS_SELECTOR, ".form-control-submit")
        submit_button.click()

        # Step 7: Wait for the redirect after login
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-info .logout")))

        # Step 8: Confirm that login was successful
        try:
            sign_out_button = driver.find_element(By.CSS_SELECTOR, ".user-info .logout")
            username_display = driver.find_element(By.CSS_SELECTOR, ".user-info .account span")
            if not sign_out_button.is_displayed() or "Test User" not in username_display.text:
                self.fail("Sign out or username is not displayed correctly.")
        except Exception as e:
            self.fail(f"Test failed due to missing element: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()