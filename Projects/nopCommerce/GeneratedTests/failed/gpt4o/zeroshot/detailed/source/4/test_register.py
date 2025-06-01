from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from faker import Faker

class RegistrationTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
        self.fake = Faker()

    def test_user_registration(self):
        driver = self.driver

        # Step 1: Open the homepage (already opened in setUp)
        
        # Step 2: Click the "Register" link in the top navigation
        register_link = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.top-menu.notmobile li a[href='/customer/info']"))
        )
        register_link.click()

        # Step 3: Wait for the registration form to load
        registration_page_title = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.page.registration-page h1"))
        )
        self.assertEqual(registration_page_title.text.strip(), "Register", "Registration page did not load properly.")

        # Step 4: Select the appropriate gender radio input based on provided data
        female_radio = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input#gender-female"))
        )
        female_radio.click()

        # Step 5: Fill in all required fields
        first_name_input = driver.find_element(By.ID, "FirstName")
        last_name_input = driver.find_element(By.ID, "LastName")
        email_input = driver.find_element(By.ID, "Email")
        company_input = driver.find_element(By.ID, "Company")
        password_input = driver.find_element(By.ID, "Password")
        confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
        
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys(self.fake.email())
        company_input.send_keys("TestCorp")
        password_input.send_keys("test11")
        confirm_password_input.send_keys("test11")

        # Step 6: Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Step 7: Wait for the response page or confirmation message to load
        confirmation_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.result"))
        )

        # Step 8: Verify that registration succeeded
        self.assertIn("Your registration completed", confirmation_message.text, "Registration did not succeed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()