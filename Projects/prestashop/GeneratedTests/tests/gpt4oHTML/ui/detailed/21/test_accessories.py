from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AccessoriesPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")
        
    def test_accessories_page_ui(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Verify header and footer are present
        header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        footer = wait.until(EC.visibility_of_element_located((By.ID, 'footer')))
        
        if not header or not footer:
            self.fail("Header or Footer not found.")

        # Verify presence and visibility of main navigations
        main_nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-nav')))
        top_menu = wait.until(EC.visibility_of_element_located((By.ID, '_desktop_top_menu')))
        if not main_nav or not top_menu:
            self.fail("Main navigation or top menu not found.")

        # Verify search input is present
        search_widget = wait.until(EC.visibility_of_element_located((By.ID, 'search_widget')))
        search_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@name="s"]')))
        if not search_widget or not search_input:
            self.fail("Search widget or input not found.")

        # Verify sign-in link is present
        sign_in_link = wait.until(EC.visibility_of_element_located((By.XPATH, '//a[@href="http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F6-accessories"]')))
        if not sign_in_link:
            self.fail("Sign-in link not found.")

        # Verify cart preview is present
        cart_preview = wait.until(EC.visibility_of_element_located((By.ID, '_desktop_cart')))
        if not cart_preview:
            self.fail("Cart preview not found.")

        # Interact with an element, for example, click the cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.XPATH, '//i[@class="material-icons shopping-cart"]')))
        cart_icon.click()

        # Verify interaction resulted in UI change
        cart_products_count = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-products-count')))
        if not cart_products_count or cart_products_count.text != "(0)":
            self.fail("Cart interaction did not reflect expected visual change.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()