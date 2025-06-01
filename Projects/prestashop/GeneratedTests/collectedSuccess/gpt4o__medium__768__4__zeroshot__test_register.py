import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
from selenium.webdriver.chrome.service import Service as ChromeService

class UserRegistrationTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()
    
    def test_registration(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open home page and click on sign in link
        sign_in_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F']")))
        sign_in_link.click()
        
        # Step 2: Click on create account link
        create_account_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "No account? Create one here")))
        create_account_link.click()
        
        # Step 3: Fill out the registration form
        radio_mr = wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1")))
        radio_mr.click()
        
        firstname_input = driver.find_element(By.ID, "field-firstname")
        firstname_input.send_keys("Test")
        
        lastname_input = driver.find_element(By.ID, "field-lastname")
        lastname_input.send_keys("User")
        
        email_input = driver.find_element(By.ID, "field-email")
        email_input.send_keys(f"test_{random.randint(0, 10000)}@user.com")
        
        password_input = driver.find_element(By.ID, "field-password")
        password_input.send_keys("test@user1")
        
        birthday_input = driver.find_element(By.ID, "field-birthday")
        birthday_input.send_keys("05/31/1970")

        # Check required checkboxes
        privacy_checkbox = driver.find_element(By.NAME, "customer_privacy")
        privacy_checkbox.click()
        
        terms_checkbox = driver.find_element(By.NAME, "psgdpr")
        terms_checkbox.click()

        # Step 4: Submit the form
        save_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Save')]")
        save_button.click()

        # Step 5: Confirm registration success
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))

        try:
            sign_out = driver.find_element(By.LINK_TEXT, "Sign out")
            self.assertTrue(sign_out.is_displayed())
        except Exception as e:
            self.fail("Registration failed, 'Sign out' not found.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()