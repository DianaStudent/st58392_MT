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
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Open the ART category page
        art_category_selector = (By.CSS_SELECTOR, "#category-9 .dropdown-item")
        art_category = wait.until(EC.presence_of_element_located(art_category_selector))
        art_category.click()

        # Wait for the ART category page to load
        product_list_selector = (By.ID, "js-product-list")
        self.assertIsNotNone(wait.until(EC.presence_of_element_located(product_list_selector)))

        # Click on the first product in the list
        first_product_selector = (By.CSS_SELECTOR, ".product .product-title a")
        first_product = wait.until(EC.presence_of_element_located(first_product_selector))
        first_product.click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button_selector = (By.CSS_SELECTOR, "button.add-to-cart")
        add_to_cart_button = wait.until(EC.element_to_be_clickable(add_to_cart_button_selector))
        add_to_cart_button.click()

        # Wait for the modal popup to appear
        modal_selector = (By.ID, "blockcart-modal")
        modal = wait.until(EC.visibility_of_element_located(modal_selector))

        # Confirm that the modal title includes a success message
        modal_title_selector = (By.CSS_SELECTOR, ".modal-title h6")
        modal_title = wait.until(EC.presence_of_element_located(modal_title_selector))
        modal_text = modal_title.text
        if not modal_text:
            self.fail("Modal title is missing or empty")
        self.assertIn("successfully added", modal_text.lower())

        # Locate and assert the presence of a "Proceed to checkout" button
        checkout_button_selector = (By.CSS_SELECTOR, ".cart-content-btn .btn-primary")
        checkout_button = wait.until(EC.presence_of_element_located(checkout_button_selector))
        if not checkout_button:
            self.fail("Proceed to checkout button is missing or not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()