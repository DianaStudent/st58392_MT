import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
    
    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for the presence of the header
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        except:
            self.fail("Header area is not present or visible.")

        # Check for the 'Accept' button in the CookieConsent
        try:
            wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        except:
            self.fail("Cookie 'Accept' button is not present or visible.")

        # Check for the navigation menu links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        except:
            self.fail("Navigation menu links (Home, Tables, Chairs) are not present or visible.")

        # Check for the Login and Register links
        try:
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        except:
            self.fail("Login or Register links are not present or visible.")

        # Check for the 'Add to cart' button on a product
        try:
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Add to cart')]")))
        except:
            self.fail("'Add to cart' button is not present or visible on any product.")

        # Check for the 'Subscribe' form input and button
        try:
            wait.until(EC.visibility_of_element_located((By.NAME, 'email')))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(., 'Subscribe')]")))
        except:
            self.fail("Subscribe form input or button is not present or visible.")

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()