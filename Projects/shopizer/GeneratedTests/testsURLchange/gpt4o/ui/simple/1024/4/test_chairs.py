import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # Run in headless mode for test
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header elements
        logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo > a > img")))
        self.assertIsNotNone(logo, "Logo not found or not visible")

        # Verify menu items
        menu_items = ["Home", "Tables", "Chairs"]
        for item in menu_items:
            element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, item)))
            self.assertTrue(element.is_displayed(), f"Menu item '{item}' not visible")

        # Verify "Accept Cookies" button
        accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept Cookies button not visible")

        # Verify account links
        account_links = ["Login", "Register"]
        for link_text in account_links:
            link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(link.is_displayed(), f"Account link '{link_text}' not visible")

        # Verify cart icon
        cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        self.assertTrue(cart_icon.is_displayed(), "Cart icon not visible")

        # Verify product listings
        product = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-wrap")))
        self.assertIsNotNone(product, "Product listings not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()