from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_add_to_cart(self):
        # Open the home page.
        self.driver.get("http://localhost/")

        # Hover over the first product to reveal the "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#product-1"))
        )
        hover = self.driver.find_element_by_css_selector("#product-1")
        hover.location_once_scrolled_into_view

        # Click the revealed "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#add-to-cart"))
        )
        add_to_cart_button = self.driver.find_element_by_css_selector("#add-to-cart")
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#cart"))
        )
        cart_icon = self.driver.find_element_by_css_selector("#cart")
        cart_icon.click()

        # Wait for the popup to become visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".popup-cart"))
        )

        # Click "View cart" or similar button inside the popup
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#view-cart"))
        )
        view_cart_button = self.driver.find_element_by_css_selector("#view-cart")
        view_cart_button.click()

        # On the cart page, verify that the product appears in the cart list
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-list"))
        )
        cart_list = self.driver.find_elements_by_css_selector(".cart-list")
        self.assertEqual(len(cart_list), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()