import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistration(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_registration(self):
        # Load the URL and wait for the content to load
        self.driver.get("http://localhost:8080/en/")

        # Wait until 'Name' field is available
        name_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-name='name']"))
        )
        name_field.send_keys("Test Name")

        # Wait until 'Email' field is available
        email_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-name='email']"))
        )
        email_field.send_keys("test@example.com")

        # Wait until 'Password' field is available
        password_field = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-name='password']"))
        )
        password_field.send_keys("test@user1")

        # Wait until 'Next' button is clickable and click it
        next_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
        )
        next_button.click()

        # Wait for the form to submit and new page to load
        WebDriverWait(self.driver, 20)

        # Check that 'Sign out' link is available
        sign_out_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/sign-out']"))
        )

if __name__ == "__main__":
    unittest.main()