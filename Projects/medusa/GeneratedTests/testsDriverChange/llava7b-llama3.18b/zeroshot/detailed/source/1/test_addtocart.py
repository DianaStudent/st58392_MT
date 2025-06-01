import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Click the menu button ("Menu")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "menuButton"))).click()
        
        # Click the "Store" link
        store_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='category-link']")))
        if 'Sweatshirts' in self.driver.page_source:
            store_link.click()

        # Click on a product image (Thumbnail) - first product
        product_image = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@data-testid='product-thumbnail']")))
        product_image.click()
        
        # Select size by clicking the size button "L"
        size_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='size-button' and text()='L']")))
        size_button.click()

        # Add the product to the cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-to-cart-button']")))
        add_to_cart_button.click()
        
        # Explicitly click the cart button to open the cart
        cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='cart-link']")))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-checkout-button']")))
        self.assertIsNotNone(go_to_checkout_button)

if __name__ == "__main__":
    unittest.main()