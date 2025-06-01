import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShopPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/category/tables")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_presence(self):
        driver = self.driver

        # Verify header is present
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area")))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Verify navigation links are present
        nav_links = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "nav ul li a")))
        expected_links = ["Home", "Tables", "Chairs"]
        actual_links = [link.text for link in nav_links]
        for expected_link in expected_links:
            self.assertIn(expected_link, actual_links, f"{expected_link} link is missing")

        # Verify Cookie Consent button is present
        cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
        self.assertTrue(cookie_button.is_displayed(), "Cookie button is not visible")

        # Interact with Cookie Consent button
        cookie_button.click()

        # Verify product list is present
        product_list = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shop-bottom-area")))
        self.assertTrue(product_list.is_displayed(), "Product list is not visible")

        # Verify Add to Cart button is present
        add_to_cart_buttons = self.wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".pro-cart button")))
        self.assertGreater(len(add_to_cart_buttons), 0, "Add to Cart buttons are missing")

        # Interact with first Add to Cart button
        add_to_cart_buttons[0].click()

        # Verify no UI errors after clicking Add to Cart button
        cart_content = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content")))
        self.assertIn("No items added to cart", cart_content.text, "Unexpected content in cart")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()