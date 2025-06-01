from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Check header presence
        try:
            header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".header-area")))
        except:
            self.fail("Header not found or not visible.")

        # Check menu links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))
        except:
            self.fail("Menu link not found or not visible.")

        # Check account settings
        try:
            account_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "account-setting-active")))
        except:
            self.fail("Account button not found or not visible.")

        # Check shopping cart
        try:
            cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
        except:
            self.fail("Cart button not found or not visible.")

        # Check product list presence
        try:
            product_list = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shop-area")))
        except:
            self.fail("Product list not found or not visible.")

        # Check footer presence
        try:
            footer = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer-area")))
        except:
            self.fail("Footer not found or not visible.")

        # Check subscribe form
        try:
            subscribe_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            subscribe_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "button")))
        except:
            self.fail("Subscribe form not found or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()