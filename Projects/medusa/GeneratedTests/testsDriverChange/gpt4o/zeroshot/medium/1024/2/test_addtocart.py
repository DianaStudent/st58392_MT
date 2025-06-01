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
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page
        menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 2. Click on the menu button
        store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 3. Click on a product image (thumbnail)
        product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt'] img")))
        product_image.click()

        # 4. Select a size
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # 5. Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        if add_to_cart_button.text.strip() != "Add to cart":
            self.fail("Add to cart button not clickable")
        add_to_cart_button.click()

        # 6. Click the cart button to open the cart
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # 7. Verify that the "Go to checkout" button is present
        checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        if not checkout_button:
            self.fail("Go to checkout button not found")

if __name__ == "__main__":
    unittest.main()