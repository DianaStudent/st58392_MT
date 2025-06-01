import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestUserRegistration(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def generate_random_email(self):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(10)) + "@example.com"

    def test_user_registration(self):
        driver = self.driver
        
        # Navigate to registration page
        my_account_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "My account"))
        )
        my_account_link.click()
        
        register_page_title = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        self.assertEqual(register_page_title.text, "Register", "Register page not loaded")

        # Fill in registration form
        email = self.generate_random_email()
        
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "gender-male"))
            ).click()
            driver.find_element(By.ID, "FirstName").send_keys("TestFirstName")
            driver.find_element(By.ID, "LastName").send_keys("TestLastName")
            driver.find_element(By.ID, "Email").send_keys(email)
            driver.find_element(By.ID, "Company").send_keys("TestCompany")
            driver.find_element(By.ID, "Newsletter").click()
            driver.find_element(By.ID, "Password").send_keys("test11")
            driver.find_element(By.ID, "ConfirmPassword").send_keys("test11")

            register_button = driver.find_element(By.ID, "register-button")
            ActionChains(driver).move_to_element(register_button).click(register_button).perform()

        except Exception as e:
            self.fail(f"Registration form filling failed: {str(e)}")

        # Confirm registration
        registration_result = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".result"))
        )
        self.assertEqual(registration_result.text, "Your registration completed", "Registration failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()