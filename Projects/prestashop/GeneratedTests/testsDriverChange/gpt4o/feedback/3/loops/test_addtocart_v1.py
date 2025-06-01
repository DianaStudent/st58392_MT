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
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on a product category from the top navigation menu (e.g., "Art")
        art_category_locator = (By.CSS_SELECTOR, "li.category#category-9 a.dropdown-item")
        art_category = wait.until(EC.presence_of_element_located(art_category_locator))
        art_category.click()

        # Step 3: Wait for the category page to load
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1.h1")))

        # Step 4: Click on the first product in the list
        first_product_locator = (By.CSS_SELECTOR, "div.js-product")
        first_product = wait.until(EC.presence_of_element_located(first_product_locator))
        first_product.click()

        # Step 5: On the product detail page, click the "Add to cart" button
        add_to_cart_locator = (By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart")
        add_to_cart_button = wait.until(EC.presence_of_element_located(add_to_cart_locator))
        add_to_cart_button.click()

        # Step 6: Wait for the modal popup to appear after the product is added
        modal_locator = (By.CSS_SELECTOR, "div.modal-content")
        modal = wait.until(EC.presence_of_element_located(modal_locator))

        # Step 7: Confirm that the modal title or content includes a success message like "successfully added"
        modal_title_locator = (By.CSS_SELECTOR, "h4.modal-title")
        modal_title = wait.until(EC.presence_of_element_located(modal_title_locator))
        self.assertIn("successfully added", modal_title.text)

        # Step 8: Optionally, locate and assert the presence of a "Proceed to checkout" button inside the modal
        checkout_button_locator = (By.CSS_SELECTOR, "a.btn.btn-primary")
        checkout_button = wait.until(EC.presence_of_element_located(checkout_button_locator))
        self.assertTrue(checkout_button.is_displayed(), "Proceed to checkout button is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()