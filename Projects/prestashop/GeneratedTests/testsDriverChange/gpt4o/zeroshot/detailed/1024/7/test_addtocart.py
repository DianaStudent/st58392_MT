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
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Click on the "Art" category link
        art_category_link = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ul[@id='top-menu']//a[normalize-space(text())='Art']")))
        art_category_link.click()

        # Wait for the first product in the "Art" category to be present and click it
        first_product = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.products div.js-product a.product-thumbnail")))
        first_product.click()

        # Click on "Add to cart" button on the product detail page
        add_to_cart_button = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.product-add-to-cart button.add-to-cart")))
        add_to_cart_button.click()

        # Wait for the modal to appear
        cart_modal = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "blockcart-modal")))

        # Check that the modal title includes "successfully added"
        modal_title = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='blockcart-modal']//h4[contains(text(), 'successfully added')]")))

        if not modal_title:
            self.fail("Success message not found in modal.")

        # Check for "Proceed to checkout" button inside modal
        proceed_to_checkout_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@id='blockcart-modal']//a[contains(., 'Proceed to checkout')]")))

        if not proceed_to_checkout_button:
            self.fail("'Proceed to checkout' button not found in modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()