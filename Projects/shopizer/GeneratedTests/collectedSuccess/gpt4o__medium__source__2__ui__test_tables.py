import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopizerHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_main_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Check for main logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
            self.assertTrue(logo.is_displayed())
        except:
            self.fail("Logo not present or not visible.")
        
        # Check for navigation links
        try:
            nav_links = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav ul li a[href='/']")))
            self.assertTrue(nav_links.is_displayed())
        except:
            self.fail("Navigation links not present or not visible.")
        
        # Check for Cookie Consent button
        try:
            cookie_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertTrue(cookie_button.is_displayed())
            cookie_button.click()
        except:
            self.fail("Cookie consent button not present or not clickable.")
        
        # Check for product categories
        try:
            categories = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".main-menu nav ul li")))
            self.assertTrue(any(category.is_displayed() for category in categories))
        except:
            self.fail("Product categories not present or not visible.")
        
        # Check for cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
            self.assertTrue(cart_icon.is_displayed())
            # Interact with cart button
            cart_icon.click()
        except:
            self.fail("Cart icon not present or not clickable.")
        
        # Confirm no items in cart
        try:
            no_items_text = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content p")))
            self.assertEqual(no_items_text.text, "No items added to cart")
        except:
            self.fail("Cart details not present or incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()