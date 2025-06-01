import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class RegisterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_register(self):
        driver = self.driver

        # Step 1: Open the homepage
        driver.get("http://max/")  # Replace this URL with the actual URL of the homepage

        # Step 2: Click the "Register" link in the top navigation
        try:
            register_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
            register_link.click()

            # Step 3: Wait for the registration form to load
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']")))

            # Step 4: Select the appropriate gender radio input based on the provided data
            gender_female_radio = self.wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
            gender_female_radio.click()

            # Step 5: Fill in all required fields
            first_name_input = driver.find_element(By.ID, "FirstName")
            first_name_input.send_keys("Test")

            last_name_input = driver.find_element(By.ID, "LastName")
            last_name_input.send_keys("User")

            email_input = driver.find_element(By.ID, "Email")
            email_input.send_keys(f'testuser{time.time()}@example.com')  # dynamically generated email

            company_input = driver.find_element(By.ID, "Company")
            company_input.send_keys("TestCorp")

            password_input = driver.find_element(By.ID, "Password")
            password_input.send_keys("test11")

            confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password_input.send_keys("test11")

            # Step 6: Submit the registration form
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

            # Step 7: Wait for the response page or confirmation message to load
            confirmation_element = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'result') and contains(text(), 'Your registration completed')]"))
            )

            # Step 8: Verify that registration succeeded
            if confirmation_element and confirmation_element.text:
                self.assertIn("Your registration completed", confirmation_element.text)
            else:
                self.fail("Registration confirmation message not found or is empty")

        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()