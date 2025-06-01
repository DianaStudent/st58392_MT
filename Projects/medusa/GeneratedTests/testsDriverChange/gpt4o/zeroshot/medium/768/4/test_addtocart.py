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
        
        # 1. Open home page (already done in setUp)

        # 2. Click on the menu button
        menu_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
        menu_button.click()

        # 3. Click on the "Store" link
        store_link = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a[data-testid='store-link']")))
        store_link.click()

        # 4. Click on a product image (thumbnail)
        product_thumbnail = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ul[@data-testid='products-list']/li[1]/a/div/img")))
        product_thumbnail.click()

        # 5. Select a size
        size_option = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//button[text()='L']")))
        size_option.click()

        # 6. Click the "Add to Cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
        add_to_cart_button.click()

        # 7. Click the cart button to open the cart
        cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
        cart_button.click()

        # 8. Verify that the "GO TO CHECKOUT" button is present
        checkout_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
        if not checkout_button:
            self.fail("GO TO CHECKOUT button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()