import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.url = "http://localhost:8080/en/"
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the homepage.
        driver.get(self.url)
        
        # Step 2: Click the login link from the top navigation.
        sign_in_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#_desktop_user_info a")))
        sign_in_link.click()
        
        # Step 3: On the login page, click on the register link.
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Step 4: Fill in the registration form fields using credentials.
        gender_radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#field-id_gender-1")))
        gender_radio.click()

        first_name_input = driver.find_element(By.CSS_SELECTOR, "#field-firstname")
        first_name_input.send_keys("Test")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "#field-lastname")
        last_name_input.send_keys("User")

        email_address = f"test_{int(time.time())}@user.com"
        email_input = driver.find_element(By.CSS_SELECTOR, "#field-email")
        email_input.send_keys(email_address)

        password_input = driver.find_element(By.CSS_SELECTOR, "#field-password")
        password_input.send_keys("test@user1")

        birthday_input = driver.find_element(By.CSS_SELECTOR, "#field-birthday")
        birthday_input.send_keys("01/01/2000")

        # Step 5: Tick checkboxes for privacy, newsletter, terms, etc.
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        newsletter_checkbox = driver.find_element(By.NAME, "newsletter")
        newsletter_checkbox.click()
        
        # Step 6: Submit the registration form.
        save_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        save_button.click()

        # Step 7: Wait for the redirect after login.
        sign_out_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".logout.hidden-sm-down")))

        # Step 8: Confirm that login was successful by checking that:
        # The "Sign out" button is present in the top navigation
        # The username (e.g. "Test User") is also visible in the top navigation.
        account_link = driver.find_element(By.CSS_SELECTOR, ".user-info a.account span.hidden-sm-down")
        
        assert "Sign out" in sign_out_button.text
        assert "Test User" in account_link.text

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()