from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page (already done in setUp)

        # Step 2: Click on a product category from the top navigation menu (e.g. ART)
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "ul#top-menu a[href='/en/9-art']")))
        art_category_link.click()

        # Step 3: Wait for the category page to load
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#js-product-list div.js-product")))

        # Step 4: Click on the first product in the list
        first_product = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div#js-product-list div.js-product a.thumbnail")))
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart")))
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear after the product is added
        modal_popup = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#blockcart-modal")))

        # Step 7: Confirm that the modal title or content includes a success message like "successfully added"
        modal_title = modal_popup.find_element(By.CSS_SELECTOR, "h4.modal-title")
        if not modal_title or "successfully added" not in modal_title.text.lower():
            self.fail("Success message not found in modal title.")

        # Step 8 (Optional): Locate and assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button = modal_popup.find_element(By.CSS_SELECTOR, "a.btn.btn-primary")
        if not proceed_to_checkout_button:
            self.fail("'Proceed to checkout' button not found in modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()