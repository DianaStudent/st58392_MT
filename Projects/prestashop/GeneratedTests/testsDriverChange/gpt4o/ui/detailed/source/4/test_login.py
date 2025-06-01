import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestLoginPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/login")

    def test_ui_elements_present(self):
        driver = self.driver
        
        try:
            # Wait for header and footer
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'header')))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'footer')))

            # Wait for navigation
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header-nav')))
            
            # Wait for login input elements
            email_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'field-email')))
            password_field = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'field-password')))
            
            # Wait for login button
            login_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, 'submit-login')))

            # Wait for register link
            register_link = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "No account? Create one here")))
            
            # Interacting with elements
            email_field.send_keys("test@example.com")
            password_field.send_keys("password123")
            login_button.click()
            
            # Confirm UI reactions
            WebDriverWait(driver, 20).until(EC.url_contains("login?back"))
        
        except Exception as e:
            self.fail(f"UI test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()