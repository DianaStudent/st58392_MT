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
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        # 1. Open home page.
        self.driver.get("http://localhost:3000/")

        # 2. Click on product category.
        category_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # 3. Select the first product.
        product_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/product-a']")))
        product_link.click()

        # 4. Click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-success is-fullwidth']")))
        add_to_cart_button.click()

        # 5. Explicitly click the cart icon (shopping bag) to open the mini-cart.
        cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()

        # 6. Wait for the mini-cart to become visible.
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='mini-cart']")))

        # 7. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='GO TO CHECKOUT']")))
        self.assertTrue(checkout_button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()