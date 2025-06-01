from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class RegisterProcessTest(unittest.TestCase):

    def setUp(self):
        # Initialize Chrome
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_registration_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the home page
        driver.get("http://localhost:8080/en/")
        
        # Click on "Sign in"
        sign_in_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Sign in']")))
        sign_in_element.click()

        # Click on "No account? Create one here"
        register_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        register_link.click()

        # Fill the registration form
        wait.until(EC.presence_of_element_located((By.ID, "customer-form")))

        # Select title
        mr_title = driver.find_element(By.XPATH, "//label[@for='field-id_gender-1']/span/input")
        mr_title.click()

        # Fill first name
        first_name_input = driver.find_element(By.ID, "field-firstname")
        first_name_input.send_keys("Test")

        # Fill last name
        last_name_input = driver.find_element(By.ID, "field-lastname")
        last_name_input.send_keys("User")

        # Fill email
        email = f"testuser{int(time.time())}@example.com"
        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(email)

        # Fill password
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")

        # Check terms and conditions
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        # Check customer privacy
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()

        # Submit the registration
        submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.form-control-submit")
        submit_button.click()

        # Check success by verifying "Sign out" text is present
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'logout') and contains(text(),'Sign out')]")))
        except:
            self.fail("Registration failed - 'Sign out' link not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()