from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_register_user(self):
        # Open the home page.
        self.driver.get("http://localhost:8080/en/")

        # Click on the login link in the top menu.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/login']"))).click()

        # Click on the register link on the login page.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/register']"))).click()

        # Fill in the registration form fields:
        self.driver.find_element(By.NAME, "gender").send_keys("Male")
        self.driver.find_element(By.NAME, "first_name").send_keys("John")
        self.driver.find_element(By.NAME, "last_name").send_keys("Doe")
        self.driver.find_element(By.NAME, "email").send_keys("test_user1@user.com")
        self.driver.find_element(By.NAME, "password").send_keys("test@user1")
        self.driver.find_element(By.NAME, "confirm_password").send_keys("test@user1")
        self.driver.find_element(By.NAME, "birthday").send_keys("1990-01-01")

        # Check required checkboxes.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='terms-checkbox']"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='policy-checkbox']"))).click()

        # Submit the form.
        self.driver.find_element(By.NAME, "register").submit()

        # Confirm success by checking for the presence of 'Sign out' in the top bar.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/logout']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()