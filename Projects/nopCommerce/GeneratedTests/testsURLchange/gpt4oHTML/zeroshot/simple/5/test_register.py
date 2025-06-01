import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class RegisterTest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # replace with actual register page URL

    def generate_random_email(self):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)) + "@test.com"

    def test_register(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Fill out registration form
        try:
            # Select gender
            gender_male = wait.until(EC.presence_of_element_located((By.ID, "gender-male")))
            gender_male.click()
            
            # Fill first name
            first_name = driver.find_element(By.ID, "FirstName")
            first_name.send_keys("Test")
            
            # Fill last name
            last_name = driver.find_element(By.ID, "LastName")
            last_name.send_keys("User")
            
            # Fill email
            email = driver.find_element(By.ID, "Email")
            generated_email = self.generate_random_email()
            email.send_keys(generated_email)
            
            # Fill company name
            company = driver.find_element(By.ID, "Company")
            company.send_keys("Test Company")
            
            # Deselect newsletter if needed
            newsletter = driver.find_element(By.ID, "Newsletter")
            if not newsletter.is_selected():
                newsletter.click()
            
            # Fill password
            password = driver.find_element(By.ID, "Password")
            password.send_keys("test11")
            
            # Fill confirm password
            confirm_password = driver.find_element(By.ID, "ConfirmPassword")
            confirm_password.send_keys("test11")
            
            # Submit the form
            register_button = driver.find_element(By.ID, "register-button")
            register_button.click()

            # Verify registration completion message
            registration_result = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='result' and text()='Your registration completed']")))
            self.assertIsNotNone(registration_result, "Registration success message not found.")

        except Exception as e:
            self.fail(f"Registration process failed: {str(e)}")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()