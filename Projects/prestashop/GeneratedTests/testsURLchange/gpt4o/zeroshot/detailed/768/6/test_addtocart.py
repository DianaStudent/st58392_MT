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
        wait = self.wait

        # Click on the 'ART' category from the top navigation menu
        art_category = wait.until(EC.presence_of_element_located((By.ID, "category-9")))
        art_category.click()

        # Wait for the category page to load and click on the first product
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".js-product a.product-thumbnail")))
        first_product.click()

        # Click the "Add to cart" button on the product detail page
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.add-to-cart")))
        add_to_cart_button.click()

        # Wait for the modal popup to appear and confirm success message
        modal = wait.until(EC.visibility_of_element_located((By.ID, "blockcart-modal")))
        modal_title = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-title.h6.text-sm-center")))
        
        if "successfully added" not in modal_title.text:
            self.fail("Success message not found in modal title.")
        
        # Assert the presence of "Proceed to checkout" button inside the modal
        checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.btn-primary[href*='cart?action=show']")))
        
        if not checkout_button.is_displayed():
            self.fail("Proceed to checkout button not found in modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()