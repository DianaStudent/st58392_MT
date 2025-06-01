from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

        # Click on the 'Art' category from the top menu
        art_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))
        art_category.click()

        # Select the first product listed in the Art category
        first_product = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.thumbnail.product-thumbnail"))
        )
        first_product.click()

        # On product detail page, click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_button.click()

        # Wait for the modal popup that confirms the product was added to the cart
        modal_title = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#blockcart-modal .modal-title"))
        )

        # Verify the modal contains the success message
        if modal_title.text and "successfully added to your shopping cart" in modal_title.text:
            pass
        else:
            self.fail("Success message not found in modal.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()