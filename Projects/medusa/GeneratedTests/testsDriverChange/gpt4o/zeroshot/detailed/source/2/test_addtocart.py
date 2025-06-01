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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        try:
            # Open menu
            menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
            menu_button.click()

            # Click Store link
            store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
            store_link.click()

            # Click on a product image (first product)
            first_product_image = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img[alt='Thumbnail']")))
            first_product_image.click()

            # Select size by clicking the size button "L"
            size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='L']")))
            size_button.click()

            # Add the product to the cart
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
            if add_to_cart_button.text.strip() == "":
                self.fail("Add to Cart button is missing or empty.")
            add_to_cart_button.click()

            # Click on cart button
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
            cart_button.click()

            # Verify presence of "GO TO CHECKOUT" button
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
            if go_to_checkout_button.text.strip() == "":
                self.fail("GO TO CHECKOUT button is missing or empty.")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()