import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # 1. Click the menu button
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 2. Click the "Store" link
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 3. Click on a product image (Thumbnail) - first product
        first_product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] li:nth-child(1) img")))
        first_product_image.click()

        # 4. Select size by clicking the size button "L"
        size_button_l = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
        size_button_l.click()

        # 5. Add the product to the cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if add_to_cart_button.text == "Out of stock":
            self.fail("Add to cart button indicates the product is out of stock.")
        add_to_cart_button.click()

        # 6. Explicitly click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # 7. Verify the "GO TO CHECKOUT" button is present
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button")))
            self.assertIsNotNone(go_to_checkout_button, "The 'GO TO CHECKOUT' button was not found.")
        except:
            self.fail("The 'GO TO CHECKOUT' button is not visible on the cart page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()