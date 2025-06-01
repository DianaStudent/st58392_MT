from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_ui_elements(self):
        driver = self.driver
        
        # Check if logo is visible
        logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.logo a img')))
        self.assertIsNotNone(logo, "Logo is not present or visible.")

        # Check if header menu items are present
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        
        self.assertIsNotNone(home_link, "Home link is not present or visible.")
        self.assertIsNotNone(tables_link, "Tables link is not present or visible.")
        self.assertIsNotNone(chairs_link, "Chairs link is not present or visible.")
        
        # Check if footer elements are present
        footer_logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer-logo img')))
        self.assertIsNotNone(footer_logo, "Footer logo is not present or visible.")
        
        copyright_text = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='copyright mb-30 ']/p")))
        self.assertIsNotNone(copyright_text, "Copyright text is not present or visible.")
        
        # Check if cookie consent is visible
        cookie_consent = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertIsNotNone(cookie_consent, "Cookie consent button is not present or visible.")
        
        # Check if login link is visible
        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
        self.assertIsNotNone(login_link, "Login link is not present or visible.")
        
        # Check if register link is visible
        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        self.assertIsNotNone(register_link, "Register link is not present or visible.")
        
        # Check if product grid is visible
        product_grid = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.shop-bottom-area .grid')))
        self.assertIsNotNone(product_grid, "Product grid is not present or visible.")
        
        # Check if cart button is visible
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.icon-cart')))
        self.assertIsNotNone(cart_button, "Cart button is not present or visible.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()