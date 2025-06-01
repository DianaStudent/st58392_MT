import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class UserRegistrationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_registration(self):
        driver = self.driver

        # Go to login page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Sign in"))).click()

        # Go to registration page
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "No account? Create one here"))).click()

        # Fill the registration form
        self.wait.until(EC.presence_of_element_located((By.ID, "field-id_gender-1"))).click()
        driver.find_element(By.ID, "field-firstname").send_keys("Test")
        driver.find_element(By.ID, "field-lastname").send_keys("User")
        
        # Generate a random email for registration
        random_email = f"test_{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}@example.com"
        driver.find_element(By.ID, "field-email").send_keys(random_email)
        driver.find_element(By.ID, "field-password").send_keys("test@user1")
        
        # Check all required checkboxes
        driver.find_element(By.NAME, "psgdpr").click()
        driver.find_element(By.NAME, "customer_privacy").click()

        # Submit the registration form
        submit_button = driver.find_element(By.XPATH, "//button[text()='Save']")
        self.wait.until(EC.element_to_be_clickable(submit_button)).click()

        # Verify successful registration
        sign_out_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Sign out")))
        self.assertTrue("Sign out" in sign_out_link.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()