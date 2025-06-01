import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        # Set up the Chrome driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click on the product category 'Art' from the top menu
        art_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, 'Art')))
        art_category.click()

        # Select the first product listed in the category
        first_product = wait.until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "The best is yet to come")))
        first_product.click()

        # On the product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'add-to-cart')))
        add_to_cart_button.click()

        # Wait for the modal popup that confirms the product was added to the cart
        modal_title = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h4[contains(text(), 'Product successfully added to your shopping cart')]")
        ))

        # Verify the modal contains the confirmation message
        if not modal_title:
            self.fail("Confirmation modal did not appear.")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()