from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestRegisterSimple(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_register_simple(self):
        # Navigate to the homepage
        self.driver.get("http://localhost/")

        # Click on the "Register" button (not explicitly mentioned in the task, 
        # but necessary for proceeding with the registration process)
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/register']"))
        ).click()

        # Fill all fields for registration
        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))
        )
        email_input.send_keys("test**11")

        password_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='password']"))
        )
        password_input.send_keys("test**11")

        # Click on the "CONTINUE" button
        continue_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        continue_button.click()

        # Check if the browser is redirected to a page containing "/my-account" in the URL
        self.assertIn("/my-account", self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()