import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click the menu button ("Menu").
        menu_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='nav-menu-button']")))
        menu_button.click()

        # Step 3: Click the "Store" link.
        store_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on a product image (Thumbnail) - first product.
        first_product_image = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@data-testid='products-list']//li[1]//img")))
        first_product_image.click()

        # Step 5: Select size by clicking the size button "L".
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
        size_button.click()

        # Step 6: Add the product to the cart.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button']")))
        if not add_to_cart_button.text:
            self.fail("Add to cart button is not loaded properly.")
        add_to_cart_button.click()

        # Step 7: Explicitly click the cart button to open the cart.
        cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 8: Verify that the "GO TO CHECKOUT" button is present.
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='checkout-button']")))
            if not go_to_checkout_button.is_displayed():
                self.fail("GO TO CHECKOUT button is not displayed.")
        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

if __name__ == '__main__':
    unittest.main()