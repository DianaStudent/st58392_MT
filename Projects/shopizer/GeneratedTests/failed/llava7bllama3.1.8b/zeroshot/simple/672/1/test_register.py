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

    def test_registration(self):
        # Step 1: Navigate to the registration page
        self.driver.get("http://localhost/")

        # Fill all fields for registration
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "firstname"))
        ).send_keys("John")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "lastname"))
        ).send_keys("Doe")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        ).send_keys("test@example.com")  # Replace with dynamically generated email

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys("test**11")

        # Click Next button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
        ).click()

        # Fill all fields for registration (Step 2)
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "firstname"))
        ).send_keys("Jane")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "lastname"))
        ).send_keys("Doe")

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        ).clear()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "email"))
        ).send_keys("jane@example.com")  # Replace with dynamically generated email

        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).clear()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "password"))
        ).send_keys("test**11")

        # Click Next button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']"))
        ).click()

        # Review registration details and click Register button
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='review-registration']"))
        )

        self.driver.find_element(By.XPATH, "//button[text()='Register']").click()

        # Check that the browser is redirected to a page containing "/my-account" in the URL
        url = self.driver.current_url
        if "my-account" not in url:
            self.fail("Registration failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()