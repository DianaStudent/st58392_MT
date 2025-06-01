import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the header links
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-register")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-login")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-wishlist")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-cart")))
        except:
            self.fail("Header links are not visible.")

        # Check the registration fields
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "FirstName")))
            wait.until(EC.visibility_of_element_located((By.ID, "LastName")))
            wait.until(EC.visibility_of_element_located((By.ID, "Email")))
            wait.until(EC.visibility_of_element_located((By.ID, "Password")))
            wait.until(EC.visibility_of_element_located((By.ID, "ConfirmPassword")))
        except:
            self.fail("Registration form fields are not visible.")

        # Check the register button
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "register-button")))
        except:
            self.fail("Register button is not visible.")

        # Check search functionality
        try:
            wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except:
            self.fail("Search box or button is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()