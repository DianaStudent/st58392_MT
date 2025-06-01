import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLoginPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def test_ui_elements(self):
        driver = self.driver

        # Load page
        driver.get("http://max/login?returnUrl=%2F")
        
        try:
            # Wait for header to be visible
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))

            # Check presence of specific elements in the header
            self.assertTrue(driver.find_element(By.CLASS_NAME, "header-links").is_displayed(), "Header links not visible")
            self.assertTrue(driver.find_element(By.CLASS_NAME, "header-logo").is_displayed(), "Header logo not visible")

            # Check presence of main elements on login page
            self.assertTrue(driver.find_element(By.CLASS_NAME, "page-title").is_displayed(), "Page title not visible")
            self.assertTrue(driver.find_element(By.NAME, "Email").is_displayed(), "Email input not visible")
            self.assertTrue(driver.find_element(By.NAME, "Password").is_displayed(), "Password input not visible")
            self.assertTrue(driver.find_element(By.CLASS_NAME, "login-button").is_displayed(), "Login button not visible")
            self.assertTrue(driver.find_element(By.CLASS_NAME, "register-button").is_displayed(), "Register button not visible")

            # Check presence and visibility of footer
            self.assertTrue(driver.find_element(By.CLASS_NAME, "footer").is_displayed(), "Footer not visible")

            # Interact with elements (e.g., toggle password visibility)
            password_eye = driver.find_element(By.CLASS_NAME, "password-eye")
            password_eye.click()
            
            # Confirm UI reaction by checking the password field type change
            password_field = driver.find_element(By.NAME, "Password")
            field_type = password_field.get_attribute("type")
            self.assertEqual(field_type, "text", "Password field type did not toggle to text")

        except Exception as e:
            self.fail(f"UI element check failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()