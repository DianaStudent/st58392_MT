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
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        # Check header links
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-register")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-login")))
        except:
            self.fail("Header links are missing or not visible")

        # Check login form fields
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
        except:
            self.fail("Login form fields are missing or not visible")

        # Check login button
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))
        except:
            self.fail("Login button is missing or not visible")

        # Check Register button
        try:
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))
        except:
            self.fail("Register button is missing or not visible")

        # Check search box
        try:
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Search box or button is missing or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()