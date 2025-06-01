import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import random
import string
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUserRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_registration(self):
        driver = self.driver
        wait = self.wait

        # Wait for the Register link and click
        register_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Register")))
        register_link.click()

        # Wait for the Registration page title
        page_title = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Register']")))
        self.assertTrue(page_title is not None, "Registration page not loaded")

        # Fill registration form
        gender_female = wait.until(EC.presence_of_element_located((By.ID, "gender-female")))
        first_name = driver.find_element(By.ID, "FirstName")
        last_name = driver.find_element(By.ID, "LastName")
        email = driver.find_element(By.ID, "Email")
        company = driver.find_element(By.ID, "Company")
        password = driver.find_element(By.ID, "Password")
        confirm_password = driver.find_element(By.ID, "ConfirmPassword")

        gender_female.click()
        first_name.send_keys("Test")
        last_name.send_keys("User")
        email.send_keys(f"testuser{''.join(random.choices(string.ascii_lowercase + string.digits, k=5))}@example.com")
        company.send_keys("TestCorp")
        password.send_keys("test11")
        confirm_password.send_keys("test11")

        # Submit the form
        register_button = driver.find_element(By.ID, "register-button")
        register_button.click()

        # Verify registration result
        registration_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".result")))
        self.assertIn("Your registration completed", registration_result.text, "Registration failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()