from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check for the presence of key UI elements
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header"))
            )

            navigation_links = driver.find_elements(By.CSS_SELECTOR, ".header-menu a")
            self.assertGreaterEqual(len(navigation_links), 6, "Not all navigation links are present")

            email_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Email"))
            )

            password_input = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "Password"))
            )

            login_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.login-button"))
            )

            register_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.register-button"))
            )
            
            # Click the Register button and check that the URL updates correctly
            register_button.click()
            WebDriverWait(driver, 20).until(
                EC.url_contains("http://max/register?returnUrl=%2F")
            )
            self.assertIn("register", driver.current_url, "Register button did not navigate correctly")

            # Return to login page for further tests
            driver.get("http://max/login?returnUrl=%2F")

            # Check for interactive elements and validate actions do not break UI
            email_input.send_keys("test@example.com")
            password_input.send_keys("password")
            login_button.click()
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "dialog-notifications-error"))
            )

        except Exception as e:
            self.fail(f"Failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()