import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8000/dk')

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 2: Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='store-link']")))
        store_link.click()

        # Step 3: Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li a")))
        product_image.click()

        # Step 4: Select a size
        size_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='option-button']:nth-child(1)")))
        size_button.click()

        # Step 5: Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='add-product-button']")))
        if add_to_cart_button.text.strip().lower() == "out of stock":
            self.fail("Product is out of stock")
        add_to_cart_button.click()

        # Step 6: Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 7: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[data-testid='checkout-button']")))
        self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(verbosity=2)