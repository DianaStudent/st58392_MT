from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class RegistrationTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        # Step 1: Open the home page.
        driver.get("http://localhost/")
        
        # Step 2: Click on the account icon/button.
        self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'pe-7s-user-female'))).click()
        
        # Step 3: Select the "Register" option.
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Register'))).click()
        
        # Step 4: Wait for the registration page to load.
        self.wait.until(EC.presence_of_element_located((By.NAME, 'email')))

        # Step 5: Fill in all fields: email, password, repeat password, first name, last name.
        email = self.generate_email()
        driver.find_element(By.NAME, 'email').send_keys(email)
        driver.find_element(By.NAME, 'password').send_keys("test**11")
        driver.find_element(By.NAME, 'repeatPassword').send_keys("test**11")
        driver.find_element(By.NAME, 'firstName').send_keys("Test")
        driver.find_element(By.NAME, 'lastName').send_keys("User")
        
        # Step 6: Select a first country from the dropdown and wait for region/state dropdown to load.
        country_select = Select(driver.find_element(By.XPATH, "//select[option[contains(text(), 'Select a country')]]"))
        country_select.select_by_index(1) # Select the second entry
        
        # Step 7: Select a first state only after selecting country and click on some place.
        state_select = Select(self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select[option[contains(text(), 'Select a state')]]"))))
        state_select.select_by_index(1) # Select the second entry
        
        # Click elsewhere to ensure dropdown updates
        driver.find_element(By.NAME, 'lastName').click()

        # Step 8: Submit the form.
        driver.find_element(By.XPATH, "//button[span[text()='Register']]").click()
        
        # Step 9: Wait for the page to redirect and confirm registration success.
        self.wait.until(lambda driver: '/my-account' in driver.current_url)
        
        # Check that resulting URL is correct
        if '/my-account' not in driver.current_url:
            self.fail('Registration did not redirect to my-account page.')

    def tearDown(self):
        # Teardown the WebDriver
        self.driver.quit()

    @staticmethod
    def generate_email():
        unique_string = str(int(time.time()))
        return f"test_{unique_string}@user.com"

if __name__ == '__main__':
    unittest.main()