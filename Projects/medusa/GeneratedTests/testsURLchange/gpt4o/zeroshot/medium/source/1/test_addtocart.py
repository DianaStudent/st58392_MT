from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Step 1: Open home page
        try:
            menu_button = self.wait.until(EC.presence_of_element_located((By.ID, "headlessui-popover-button-:R6qdtt7:")))
            menu_button.click()
        except Exception as e:
            self.fail(f"Menu button is not present: {str(e)}")

        # Step 2: Click on the menu button
        try:
            store_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='store-link']")))
            store_link.click()
        except Exception as e:
            self.fail(f"Store link is not present: {str(e)}")

        # Step 3: Click on a product image (thumbnail)
        try:
            product_image = self.wait.until(EC.presence_of_element_located((By.XPATH, "//ul[@data-testid='products-list']/li/a")))
            product_image.click()
        except Exception as e:
            self.fail(f"Product image is not present: {str(e)}")

        # Step 4: Select a size
        try:
            size_option = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='option-button'][text()='L']")))
            size_option.click()
        except Exception as e:
            self.fail(f"Size option is not present: {str(e)}")

        # Step 5: Click the "Add to Cart" button
        try:
            add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button is not present: {str(e)}")

        # Step 6: Click the cart button to open the cart
        try:
            cart_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button is not present: {str(e)}")

        # Step 7: Verify that the "GO TO CHECKOUT" button is present
        try:
            go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Go to checkout']")))
            # Ensure that the button exists and text is not empty
            if not go_to_checkout_button.text.strip():
                self.fail("GO TO CHECKOUT button text is empty")
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button is not present: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()