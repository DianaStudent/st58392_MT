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
        self.driver.get('http://max/login?returnUrl=%2F')
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check the Title of the Page
        self.assertIn("Your store. Login", driver.title)

        # Check main UI elements
        try:
            # Logo
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-logo a img")))

            # Header Links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Wishlist")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))

            # Menu Links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))

            # Welcome Title
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-title h1")))

            # Returning Customer Form
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.NAME, "RememberMe")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Forgot password?")))
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".login-button")))

            # New Customer Register Button
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".register-button")))

        except Exception as e:
            self.fail(f"Failed to verify UI elements: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()