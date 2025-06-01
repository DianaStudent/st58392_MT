from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestRegistration(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_registration(self):
        # Find and fill in the registration form
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "full-name"))
        ).send_keys("user test")
        
        self.driver.find_element(By.ID, "email-address").send_keys(f"testuser{self.test_email}@example.com")
        self.driver.find_element(By.ID, "password").send_keys("testuser")
        self.driver.find_element(By.ID, "confirm-password").send_keys("testuser")

        # Fill in the company information
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "company-name"))
        ).send_keys("Test Company")
        
        self.driver.find_element(By.ID, "user-type").click()
        self.driver.find_element(By.XPATH, "//label[@class='radio'][1]/../input").click()  # Select individual

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "phone-number"))
        ).send_keys("1234567890")
        
        # Fill in the billing information
        self.driver.find_element(By.ID, "billing-address").send_keys("Test Billing Address")
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "city"))
        ).send_keys("Test City")
        
        self.driver.find_element(By.ID, "state-region").click()
        # The dropdown menu options are not visible in the screenshot so we'll skip this for now
        self.driver.find_element(By.ID, "postal-code").send_keys("12345")

        # Submit the form
        self.driver.find_element(By.ID, "next-button").click()

        # Verify that the welcome message is present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@class='welcome-message']"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()