import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page & Step 2: Click on a product category (e.g. ART)
        art_category_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#category-9 a.dropdown-item")))
        art_category_link.click()

        # Step 3: Wait for the category page to load & Step 4: Click on the first product
        first_product_link = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".products .js-product.product:first-child .product-title a")
            )
        )
        first_product_link.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button.add-to-cart")
            )
        )
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear & Step 7: Confirm that it includes a success message
        modal_title = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#blockcart-modal .modal-title.h6.text-sm-center")
            )
        )
        
        # Check that the modal title includes a success message
        self.assertIn("successfully added", modal_title.text.lower())

        # Step 8: Locate and assert the presence of a "Proceed to checkout" button inside the modal
        checkout_button = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "a.btn.btn-primary")
            )
        )
        self.assertIsNotNone(checkout_button, "Proceed to checkout button is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()