import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestStoreUI(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

        # Wait helper
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_components(self):
        driver = self.driver

        # Check and wait for login elements
        try:
            welcome_title = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//h1[text()='Welcome, Please Sign In!']"))
            )

            email_label = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//label[@for='Email']"))
            )
            password_label = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//label[@for='Password']"))
            )

            login_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[@type='submit' and text()='Log in']"))
            )
            forgot_password_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[@href='/passwordrecovery']"))
            )
            register_button = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(@onclick, '/register')]"))
            )
        
        except Exception as e:
            self.fail(f"Required elements missing or not visible: {str(e)}")

    def tearDown(self):
        # Quit the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()