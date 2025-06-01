import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class MedusaStoreTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart_process(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="nav-menu-button"]')))
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="store-link"]')))
        store_link.click()

        # Step 4: Click on a product image (thumbnail)
        product_thumbnail = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'ul[data-testid="products-list"] li a')))
        product_thumbnail.click()

        # Step 5: Select a size
        option_button = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button[data-testid="option-button"]')))
        if option_button:
            option_button[0].click()
        else:
            self.fail("Size options are not available")

        # Step 6: Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-testid="add-product-button"]')))
        if add_to_cart_button and add_to_cart_button.text == "Add to cart":
            add_to_cart_button.click()
        else:
            self.fail("Add to Cart button is not available or in wrong state")

        # Step 7: Click the cart button to open the cart
        cart_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'a[data-testid="nav-cart-link"]')))
        cart_link.click()

        # Step 8: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[data-testid="checkout-button"]')))
        if not go_to_checkout_button.is_displayed():
            self.fail("'GO TO CHECKOUT' button is not present")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()