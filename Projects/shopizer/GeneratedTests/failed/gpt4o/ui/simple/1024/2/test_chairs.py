from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check header logo
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo img")))
        except:
            self.fail("Logo is not visible.")

        # Check main navigation links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
            self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']")))
        except:
            self.fail("Navigation links are not visible.")

        # Check account setting icon
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".same-style.account-setting button")))
        except:
            self.fail("Account setting icon is not visible.")

        # Check cart icon
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        except:
            self.fail("Cart icon is not visible.")

        # Check product div
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap")))
        except:
            self.fail("Product div is not visible.")

        # Check footer links
        try:
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        except:
            self.fail("Footer links are not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()