import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on a product category from the top navigation menu (e.g. ART)
        art_category = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.dropdown-item[href*='9-art']")))
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.js-product")))

        # Step 4: Click on the first product in the list
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.thumbnail.product-thumbnail")))
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart")))
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear after the product is added
        modal = wait.until(EC.visibility_of_element_located((By.ID, "blockcart-modal")))

        # Step 7: Confirm that the modal title or content includes a success message like "successfully added"
        # Ensure the modal and its title exist and are not empty
        modal_title = modal.find_element(By.CSS_SELECTOR, "h4.modal-title")
        if not modal_title or "successfully added" not in modal_title.text:
            self.fail("Success message not found in modal title.")

        # Step 8: Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button = modal.find_element(By.CSS_SELECTOR, "a.btn.btn-primary[href*='cart?action=show']")
        if not proceed_to_checkout_button:
            self.fail("'Proceed to checkout' button not found in the modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()