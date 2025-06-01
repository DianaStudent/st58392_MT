import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class UITests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost:8080/en/3-clothes")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header
            wait.until(EC.visibility_of_element_located((By.ID, "header")))

            # Check main navigation links
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Clothes")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Accessories")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Art")))

            # Check login link
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))

            # Check register link
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Create account")))

            # Check search bar presence
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[type='text'][name='s']")))

            # Check newsletter subscription form
            wait.until(EC.visibility_of_element_located((By.NAME, "email")))

            # Check subscription button
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[name='submitNewsletter'][type='submit']")))

            # Check cart info
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.blockcart.cart-preview")))

            # Check product list
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.products")))

        except Exception as e:
            self.fail(f"UI Element not found: {e}")

if __name__ == "__main__":
    unittest.main()