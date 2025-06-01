from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/search")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        
        # List of UI elements to verify
        elements_to_verify = [
            (By.CSS_SELECTOR, "a[href='/']"), # Home page link
            (By.CSS_SELECTOR, "a[href='/newproducts']"), # New products link
            (By.CSS_SELECTOR, "a[href='/search']"), # Search link
            (By.CSS_SELECTOR, "a[href='/customer/info']"), # My account link
            (By.CSS_SELECTOR, "a[href='/blog']"), # Blog link
            (By.CSS_SELECTOR, "a[href='/contactus']"), # Contact us link
            (By.CSS_SELECTOR, "#small-search-box-form input[name='q']"), # Search input
            (By.CSS_SELECTOR, "#small-search-box-form button[type='submit']"), # Search button
            (By.CSS_SELECTOR, ".product-filters .filter-title"), # Filter by price
            (By.CSS_SELECTOR, ".button-1.product-box-add-to-cart-button"), # Add to cart button
            (By.CSS_SELECTOR, ".button-1.add-to-compare-list-button"), # Add to compare list button
            (By.CSS_SELECTOR, ".button-1.add-to-wishlist-button"), # Add to wishlist button
        ]

        # Check presence and visibility of each element
        for selector in elements_to_verify:
            element = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(selector),
                message=f"Element with selector {selector} is not visible"
            )

        # Interaction: Click on "Add to cart" button of the first product
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.product-box-add-to-cart-button")),
            message="Add to Cart button is not clickable"
        )
        add_to_cart_button.click()

        # Verify that interactive elements update the UI without errors
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#dialog-notifications-success")),
            message="Success notification not visible"
        )

if __name__ == "__main__":
    unittest.main()