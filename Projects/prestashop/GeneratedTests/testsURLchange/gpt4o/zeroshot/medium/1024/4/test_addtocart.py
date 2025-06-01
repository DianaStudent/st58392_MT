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

        # Step 2: Click on a product category
        category_selector = (By.LINK_TEXT, "Art")
        category_element = self.wait.until(EC.element_to_be_clickable(category_selector))
        category_element.click()

        # Step 3: Select the first product listed in the category
        first_product_selector = (By.CSS_SELECTOR, ".products .js-product a.product-thumbnail")
        first_product_element = self.wait.until(EC.element_to_be_clickable(first_product_selector))
        first_product_element.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button_selector = (By.CSS_SELECTOR, "button.add-to-cart")
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(add_to_cart_button_selector))
        add_to_cart_button.click()

        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        modal_title_selector = (By.CSS_SELECTOR, "#blockcart-modal .modal-title")
        modal_title_element = self.wait.until(EC.visibility_of_element_located(modal_title_selector))

        # Step 6: Verify the modal contains a success message
        if not modal_title_element or modal_title_element.text.strip() == "":
            self.fail("The confirmation modal did not appear or was empty.")
        
        self.assertIn("successfully added", modal_title_element.text, 
                      "The confirmation message does not contain 'successfully added'.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()