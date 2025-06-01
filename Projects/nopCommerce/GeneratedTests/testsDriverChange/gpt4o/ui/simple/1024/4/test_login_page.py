import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo img")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))

            # Check login section
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[text()='Welcome, Please Sign In!']")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".register-block .register-button")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-page form .login-button")))

            # Check form fields
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "RememberMe")))

            # Check footer elements
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Privacy notice")))

        except Exception as e:
            self.fail(f"UI element not found or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()