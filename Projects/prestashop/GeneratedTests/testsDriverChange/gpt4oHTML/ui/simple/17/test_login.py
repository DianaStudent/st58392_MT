import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIDisplay(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")
        self.wait = WebDriverWait(self.driver, 20)  # Timeout set to 20 seconds

    def test_ui_components_display(self):
        driver = self.driver
        
        # Check the header presence
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.ID, "header")))
        except Exception as e:
            self.fail(f"Header not found: {str(e)}")

        # Check if login form is present
        try:
            login_form = self.wait.until(EC.visibility_of_element_located((By.ID, "login-form")))
        except Exception as e:
            self.fail(f"Login form not found: {str(e)}")
        
        # Check email field
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-email")))
        except Exception as e:
            self.fail(f"Email field not found: {str(e)}")

        # Check password field
        try:
            password_field = self.wait.until(EC.visibility_of_element_located((By.ID, "field-password")))
        except Exception as e:
            self.fail(f"Password field not found: {str(e)}")
        
        # Check sign in button
        try:
            sign_in_button = self.wait.until(EC.visibility_of_element_located((By.ID, "submit-login")))
        except Exception as e:
            self.fail(f"Sign-in button not found: {str(e)}")
        
        # Check 'forgot password' link
        try:
            forgot_password_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'password-recovery')]"))
            )
        except Exception as e:
            self.fail(f"Forgot password link not found: {str(e)}")
        
        # Check 'No account? Create one here' link
        try:
            register_link = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, "//a[contains(@href, 'registration')]"))
            )
        except Exception as e:
            self.fail(f"Register link not found: {str(e)}")
        
        # Check navigation links
        navigation_links = {
            "home": "http://localhost:8080/en/",
            "clothes": "http://localhost:8080/en/3-clothes",
            "accessories": "http://localhost:8080/en/6-accessories",
            "art": "http://localhost:8080/en/9-art",
            "login": "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art",
            "register": "http://localhost:8080/en/registration",
        }
        
        for link_text in navigation_links:
            try:
                link = self.wait.until(
                    EC.visibility_of_element_located((By.XPATH, f"//a[@href='{navigation_links[link_text]}']"))
                )
            except Exception as e:
                self.fail(f"Navigation link '{link_text}' not found: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()