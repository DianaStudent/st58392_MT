import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/login?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        try:
            # Verify that headers are present
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-upper")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-lower")))

            # Verify the logo
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-logo")))

            # Verify main menu links
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))

            # Verify login form components
            self.wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            self.wait.until(EC.visibility_of_element_located((By.ID, "RememberMe")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "login-button")))

            # Verify "Register" button
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "register-button")))

            # Verify footer and its components
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        except Exception as e:
            self.fail(f"An element was not found: {str(e)}")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()