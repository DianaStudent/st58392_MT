import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver
        
        # Step 2: Click on a product category from the top menu
        try:
            category = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#category-9 a"))
            )
            category.click()
        except Exception as e:
            self.fail(f"Category selection failed: {str(e)}")

        # Step 3: Select the first product listed in the category
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "div.js-product-miniature a.product-thumbnail")
                )
            )
            first_product.click()
        except Exception as e:
            self.fail(f"First product selection failed: {str(e)}")

        # Step 4: On the product detail page, click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button.add-to-cart")
                )
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button click failed: {str(e)}")

        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        try:
            modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )
        except Exception as e:
            self.fail(f"Modal did not appear: {str(e)}")

        # Step 6: Verify the modal contains a message like "Product successfully added to your shopping cart"
        try:
            modal_title = modal.find_element(By.CSS_SELECTOR, ".modal-title")
            self.assertIn("successfully added to your shopping cart", modal_title.text)
        except Exception as e:
            self.fail(f"Success message not found in modal: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()