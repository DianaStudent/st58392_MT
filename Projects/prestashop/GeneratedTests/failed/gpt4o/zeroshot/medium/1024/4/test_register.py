from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class RegistrationTestCase(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver

        # 1. Open the home page
        # Already done in setUp method
        
        # 2. Click on the login link in the top menu
        sign_in_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a/span[text()='Sign in']")))
        sign_in_link.click()

        # 3. Click on the register link on the login page
        create_account_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here")))
        create_account_link.click()

        # 4. Fill in the registration form fields
        driver.find_element(By.ID, "field-id_gender-1").click()
        driver.find_element(By.ID, "field-firstname").send_keys("Test")
        driver.find_element(By.ID, "field-lastname").send_keys("User")
        
        email_element = driver.find_element(By.ID, "field-email")
        dynamic_email = f"test_{int(time.time())}@user.com"
        email_element.send_keys(dynamic_email)
        
        driver.find_element(By.ID, "field-password").send_keys("test@user1")
        driver.find_element(By.ID, "field-birthday").send_keys("01/01/1990")

        # 5. Check required checkboxes
        driver.find_element(By.NAME, "psgdpr").click()
        driver.find_element(By.NAME, "customer_privacy").click()

        # 6. Submit the form
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

        # 7. Confirm success by checking for the presence of "Sign out" in the top bar
        sign_out_text = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a/span[text()='Sign out']")))

        # Assert that "Sign out" is present
        self.assertIsNotNone(sign_out_text, "Registration failed. 'Sign out' text not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()