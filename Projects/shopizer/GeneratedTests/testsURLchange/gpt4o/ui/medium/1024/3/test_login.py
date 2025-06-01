import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/login")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify header links
        try:
            header_links = driver.find_elements(By.CSS_SELECTOR, ".main-menu a")
            self.assertTrue(len(header_links) > 0, "Header links are missing.")
            self.assertTrue(header_links[0].is_displayed(), "Header link is not visible.")
        except Exception as e:
            self.fail(f"Header links check failed: {str(e)}")
        
        # Verify login form and inputs
        try:
            username_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-box button[type='submit']")))

            self.assertTrue(username_input.is_displayed(), "Username input is not visible.")
            self.assertTrue(password_input.is_displayed(), "Password input is not visible.")
            self.assertTrue(login_button.is_displayed(), "Login button is not visible.")
        except Exception as e:
            self.fail(f"Login form check failed: {str(e)}")
        
        # Verify cookie consent button
        try:
            cookie_button = driver.find_element(By.ID, "rcc-confirm-button")
            self.assertTrue(cookie_button.is_displayed(), "Cookie consent button is not visible.")
        except Exception as e:
            self.fail(f"Cookie consent button check failed: {str(e)}")
        
        # Interaction with Login button
        try:
            username_input.send_keys("test@example.com")
            password_input.send_keys("password")
            login_button.click()

            # Here we expect some error message or UI update due to incorrect login.
            # This can be an additional check if an error message appears.
        except Exception as e:
            self.fail(f"Interaction with login button failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()