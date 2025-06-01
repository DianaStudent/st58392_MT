from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_register_user(self):
        # Open the home page.
        self.driver.get("http://localhost:8080/en/")

        # Click on the login link in the top menu.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))).click()

        # Click on the register link on the login page.
        self.driver.find_element(By.XPATH, "//button[text()='Register']").click()

        # Fill in the registration form fields:
        #   - Gender
        self.driver.find_element(By.XPATH, "//label[@data-name='gender']/../input").send_keys("Male")

        #   - First name
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='first_name']/../input"))).send_keys("John")

        #   - Last name
        self.driver.find_element(By.XPATH, "//label[@data-name='last_name']/../input").send_keys("Doe")

        #   - Email
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='email']/../input"))).send_keys(f"test_{self.random_string(8)}@user.com")

        #   - Password
        self.driver.find_element(By.XPATH, "//label[@data-name='password']/../input").send_keys("test@user1")

        #   - Birthday
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[@data-name='birthday']/../input"))).send_keys("1990-01-01")

        # Check required checkboxes.
        self.driver.find_element(By.XPATH, "//label[@data-name='terms_and_conditions']/..").click()
        self.driver.find_element(By.XPATH, "//label[@data-name='privacy_policy']/..").click()

        # Submit the form.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Register']"))).click()

        # Confirm success by checking for the presence of "Sign out" in the top bar.
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[text()='Sign out']")))

    def random_string(self, length):
        import random
        return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(length))

if __name__ == "__main__":
    unittest.main()