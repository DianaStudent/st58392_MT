from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class TestRegisterMedium(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/")

    def test_register_medium(self):
        # Click on the login link in the top menu
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Login']"))).click()

        # Click on the register link on the login page
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Register']"))).click()

        # Fill in the registration form fields:
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-name='first_name']"))).send_keys("Test")
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-name='last_name']"))).send_keys("User")
        email = f"test_{int(time.time())}@user.com"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-name='email']"))).send_keys(email)
        password = "test@user1"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-name='password']"))).send_keys(password)

        # Check required checkboxes
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@data-name='terms']"))).click()

        # Submit the form
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Register']"))).click()

        # Confirm success by checking for the presence of "Sign out" in the top bar
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[normalize-space()='Sign out']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()