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

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on the ART category from the top navigation menu
        art_category = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Art")))
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "block-category")))

        # Step 4: Click on the first product in the list
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product .product-title a")))
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.add-to-cart")))
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear
        modal = wait.until(EC.presence_of_element_located((By.ID, "blockcart-modal")))

        # Step 7: Confirm that the modal title includes a success message
        modal_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#myModalLabel")))

        if not modal_title or "successfully added" not in modal_title.text:
            self.fail("Success message not found in the modal title.")

        # Step 8: Locate and assert the presence of a "Proceed to checkout" button inside the modal
        checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href*='cart?action=show']")))

        if not checkout_button:
            self.fail("Proceed to checkout button is missing in the modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()