from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart(self):
        driver = self.driver

        # Click on the "ART" category from the top menu
        art_category_selector = (By.CSS_SELECTOR, 'a[href="/en/9-art"]')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(art_category_selector)).click()

        # Wait for the category page to load and click on the first product
        first_product_selector = (By.CSS_SELECTOR, '.products .product-miniature:first-child a.product-thumbnail')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(first_product_selector)).click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button_selector = (By.CSS_SELECTOR, 'button.add-to-cart')
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button_selector)).click()

        # Wait for the modal popup to appear
        modal_selector = (By.ID, 'blockcart-modal')
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located(modal_selector))

        # Confirm the success message appears
        modal_title_selector = (By.CSS_SELECTOR, '#blockcart-modal .modal-title')
        modal_title_element = WebDriverWait(driver, 20).until(EC.presence_of_element_located(modal_title_selector))
        self.assertIn("successfully added", modal_title_element.text.lower())

        # Assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button_selector = (By.CSS_SELECTOR, 'a[href*="cart"]')
        if not WebDriverWait(driver, 20).until(EC.element_to_be_clickable(proceed_to_checkout_button_selector)):
            self.fail("Proceed to checkout button not found in modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()