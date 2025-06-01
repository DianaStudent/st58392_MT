import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:3000/')

    def test_add_to_cart(self):
        # Click on product category
        category_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/category-a"]'))
        )
        category_link.click()

        # Select the first product
        product_card = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//div[@class="product-card"]//a[@href="/product-a"]'))
        )
        product_card.click()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@id="add-to-cart-button"]'))
        )
        add_to_cart_button.click()

        # Explicitly click the cart icon (shopping bag)
        cart_icon = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-button'))
        )
        cart_icon.click()

        # Wait for the mini-cart to become visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, '//div[@class="mini-cart"]'))
        )

        # Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.driver.find_element(By.XPATH, '//button[@id="go-to-checkout-button"]')
        self.assertTrue(go_to_checkout_button.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()