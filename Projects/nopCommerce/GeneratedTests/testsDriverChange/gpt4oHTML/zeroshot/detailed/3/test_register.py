from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
import string

class TestRegisterProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def generate_random_email(self):
        return 'test_user_' + ''.join(random.choices(string.ascii_lowercase + string.digits, k=5)) + '@example.com'

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Open the homepage
        driver.get("http://max/")
        
        # Click the "Register" link in the top navigation
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "My account")))
        register_link.click()
        
        # Wait for the registration form to load
        wait.until(EC.presence_of_element_located((By.ID, "register-button")))
        
        # Select the gender as Female
        gender_female_radio = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        gender_female_radio.click()
        
        # Fill in all required fields
        first_name_input = driver.find_element(By.ID, "FirstName")
        last_name_input = driver.find_element(By.ID, "LastName")
        email_input = driver.find_element(By.ID, "Email")
        company_input = driver.find_element(By.ID, "Company")
        password_input = driver.find_element(By.ID, "Password")
        confirm_password_input = driver.find_element(By.ID, "ConfirmPassword")
        
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys(self.generate_random_email())
        company_input.send_keys("TestCorp")
        password_input.send_keys("test11")
        confirm_password_input.send_keys("test11")
        
        # Submit the registration form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()
        
        # Wait for the response page or confirmation message to load
        result_confirmation = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
        
        # Verify that registration succeeded
        if not result_confirmation or "Your registration completed" not in result_confirmation.text:
            self.fail("Registration confirmation message is missing or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()