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
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver
        
        try:
            # Header
            header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.assertTrue(header.is_displayed(), "Header is not visible")

            # Footer
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            self.assertTrue(footer.is_displayed(), "Footer is not visible")

            # Page Title
            page_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Welcome, Please Sign In!']")))
            self.assertTrue(page_title.is_displayed(), "Page title 'Welcome, Please Sign In!' is not visible")

            # Email Input
            email_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.assertTrue(email_input.is_displayed(), "Email input is not visible")

            # Password Input
            password_input = self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.assertTrue(password_input.is_displayed(), "Password input is not visible")

            # Login Button
            login_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
            self.assertTrue(login_button.is_displayed(), "Login button is not visible")

            # Register Button
            register_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
            self.assertTrue(register_button.is_displayed(), "Register button is not visible")

            # Clicking Register button
            register_button.click()
            WebDriverWait(driver, 10).until(EC.url_contains("register"))
            self.assertIn("register", driver.current_url, "Register button does not redirect to register page")

        except Exception as e:
            self.fail(str(e))

if __name__ == "__main__":
    unittest.main()