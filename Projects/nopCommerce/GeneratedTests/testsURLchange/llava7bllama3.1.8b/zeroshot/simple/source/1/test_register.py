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
        self.driver.get("http://max/")

    def test_registration(self):
        # Enter email address
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-email"))).send_keys("test_email@example.com")
        except Exception as e:
            self.fail(f"Failed to find email input field: {str(e)}")

        # Enter password
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-password"))).send_keys("test11")
        except Exception as e:
            self.fail(f"Failed to find password input field: {str(e)}")

        # Submit registration form
        register_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#register-button")))
        register_button.click()

        # Wait for successful registration message
        try:
            WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element((By.ID, "result"), "Your registration completed"))
        except Exception as e:
            self.fail(f"Failed to find successful registration message: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()