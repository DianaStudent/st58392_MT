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

        # Click on the "ART" category
        art_category_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul#top-menu > li.category > a[href*='9-art']"))
        )
        art_category_link.click()

        # Wait for the category page to load and click on the first product
        first_product = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#js-product-list > div.products > div.js-product > article > div.thumbnail-top > a"))
        )
        first_product.click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_button.click()

        # Wait for the modal popup to appear
        modal_title = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div#blockcart-modal div.modal-title"))
        )

        # Confirm that the modal title includes a success message
        self.assertIn("successfully added", modal_title.text)

        # Locate and assert the presence of a "Proceed to checkout" button inside the modal
        proceed_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-primary[href*='cart?action=show']"))
        )
        self.assertTrue(proceed_to_checkout_button.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()