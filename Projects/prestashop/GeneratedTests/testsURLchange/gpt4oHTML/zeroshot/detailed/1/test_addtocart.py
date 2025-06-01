import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        # Setup the Chrome WebDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get("http://localhost:8080/en/")

        # Wait and click on 'Art' category in the navigation menu
        art_category_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul#top-menu li#category-9 a"))
        )
        art_category_link.click()

        # Wait for the Art category page to load and click on the first product
        first_product_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.products div.js-product a.product-thumbnail"))
        )
        first_product_link.click()

        # Wait for the product detail page to load and click the "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.btn-primary.add-to-cart"))
        )
        add_to_cart_button.click()

        # Wait for the popup to appear after the product is added
        modal_popup = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "blockcart-modal"))
        )

        # Verify that the modal contains the success message
        modal_title = driver.find_element(By.CSS_SELECTOR, "div#blockcart-modal h4.modal-title")
        self.assertTrue("successfully added" in modal_title.text, "Success message not found in modal title.")

        # Optionally locate and assert the presence of "Proceed to checkout" button
        checkout_button = driver.find_element(By.CSS_SELECTOR, "a.btn-primary[href*='cart?action=show']")
        self.assertIsNotNone(checkout_button, "Proceed to checkout button not found in modal.")

    def tearDown(self):
        # Close the browser after each test
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()