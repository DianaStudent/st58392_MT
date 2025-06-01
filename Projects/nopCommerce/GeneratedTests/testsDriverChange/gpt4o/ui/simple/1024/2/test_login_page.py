from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class LoginPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-upper")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-lower")))

            # Check main page components
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-title")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "form[action='/login?returnurl=%2F']")))

            # Check form fields and buttons
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.login-button")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".button-1.register-button")))

            # Check links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot password?")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            
            # Footer elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".footer")))

        except Exception as e:
            self.fail(f"UI element is missing: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()