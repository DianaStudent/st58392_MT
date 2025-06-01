import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the login link in the top menu.
        sign_in_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign in")))
        self.assertTrue(sign_in_link.is_displayed())
        sign_in_link.click()

        # Step 2: Click on the register link on the login page.
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        self.assertTrue(register_link.is_displayed())
        register_link.click()

        # Step 3: Fill in the registration form fields
        gender_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='field-id_gender-1']")))
        self.assertTrue(gender_radio_button.is_displayed())
        gender_radio_button.click()

        first_name_field = wait.until(EC.presence_of_element_located((By.ID, "field-firstname")))
        self.assertTrue(first_name_field.is_displayed())
        first_name_field.send_keys("Test")

        last_name_field = wait.until(EC.presence_of_element_located((By.ID, "field-lastname")))
        self.assertTrue(last_name_field.is_displayed())
        last_name_field.send_keys("User")

        email_field = wait.until(EC.presence_of_element_located((By.ID, "field-email")))
        self.assertTrue(email_field.is_displayed())
        email_field.send_keys(f"test_{int(time.time())}@user.com")

        password_field = wait.until(EC.presence_of_element_located((By.ID, "field-password")))
        self.assertTrue(password_field.is_displayed())
        password_field.send_keys("test@user1")

        birthday_field = wait.until(EC.presence_of_element_located((By.ID, "field-birthday")))
        self.assertTrue(birthday_field.is_displayed())
        birthday_field.send_keys("05/31/1970")
        
        # Step 4: Check required checkboxes.
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        self.assertTrue(terms_checkbox.is_displayed())
        terms_checkbox.click()

        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        self.assertTrue(privacy_checkbox.is_displayed())
        privacy_checkbox.click()

        # Step 5: Submit the form.
        submit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and contains(., 'Save')]")))
        self.assertTrue(submit_button.is_displayed())
        submit_button.click()

        # Step 6: Confirm success by checking for the presence of "Sign out" in the top bar.
        sign_out_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        self.assertTrue(sign_out_link.is_displayed())

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()