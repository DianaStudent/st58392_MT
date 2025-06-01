import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestRegisterPageUI(unittest.TestCase):

    def setUp(self):
        # Set up Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")
        self.wait = WebDriverWait(self.driver, 20)

    def test_key_ui_elements_visible(self):
        try:
            # Verify header links are present and visible
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Wishlist")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))

            # Verify search box
            self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-box-button")))

            # Verify registration form
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-title")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='FirstName']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='LastName']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='Email']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='Password']")))
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='ConfirmPassword']")))

            # Verify newsletter checkbox
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='Newsletter']")))
            
            # Verify registration button
            self.wait.until(EC.visibility_of_element_located((By.ID, "register-button")))

        except Exception as e:
            self.fail(f"Key UI element verification failed: {e}")

    def tearDown(self):
        # Close the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()