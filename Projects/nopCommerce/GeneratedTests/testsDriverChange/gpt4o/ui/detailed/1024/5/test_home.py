import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        # Setup ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
    
    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header and its components
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        self.assertIsNotNone(header, "Header should be present and visible")

        # Check footer and its components
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        self.assertIsNotNone(footer, "Footer should be present and visible")

        # Check navigation menu
        nav_menu = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "top-menu")))
        self.assertIsNotNone(nav_menu, "Navigation menu should be present and visible")

        # Check search input and button
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-box-button")))
        self.assertIsNotNone(search_box, "Search box should be present and visible")
        self.assertIsNotNone(search_button, "Search button should be present and visible")

        # Check Register and Login links
        register_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.ico-register")))
        login_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.ico-login")))
        self.assertIsNotNone(register_link, "Register link should be present and visible")
        self.assertIsNotNone(login_link, "Login link should be present and visible")

        # Check interaction with search
        search_box.send_keys("test product")
        search_button.click()
        wait.until(EC.url_contains("/search?q=test+product"))

        # Check presence of wishlist and cart
        wishlist_qty = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "wishlist-qty")))
        cart_qty = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-qty")))
        self.assertIsNotNone(wishlist_qty, "Wishlist quantity should be present and visible")
        self.assertIsNotNone(cart_qty, "Cart quantity should be present and visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()