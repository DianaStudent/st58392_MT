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
        self.driver.implicitly_wait(10)  # Implicitly wait for elements to load

    def test_add_to_cart_process(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Click on a product category (Art) from the top navigation menu
        wait = WebDriverWait(driver, 20)
        art_category = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//ul[@id='top-menu']/li[@id='category-9']/a")))
        art_category.click()

        # Wait for the category page to load and click on the first product
        first_product = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".js-product .product-title > a")))
        first_product.click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-add-to-cart .add-to-cart")))
        add_to_cart_button.click()

        # Wait for the modal popup to appear after the product is added
        modal_title = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "#blockcart-modal .modal-title")))

        # Confirm success by verifying the presence of the success message
        if "successfully added" not in modal_title.text:
            self.fail("Success message not found in modal title")

        # Optionally, locate and assert the presence of a "Proceed to checkout" button
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "a.btn-primary[href*='action=show']")))

        if not proceed_to_checkout_button.is_displayed():
            self.fail("Proceed to checkout button not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()