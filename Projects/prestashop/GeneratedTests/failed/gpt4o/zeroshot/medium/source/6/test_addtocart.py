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
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click on the "Art" category from the top menu
        art_category = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Art")))
        art_category.click()

        # Select the first product listed in the art category
        first_product = wait.until(EC.element_to_be_clickable((
            By.CSS_SELECTOR, ".products .product a.product-thumbnail")))
        first_product.click()

        # Add the product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart")))
        add_to_cart_button.click()

        # Wait for the modal popup that confirms the product was added to the cart
        modal_title = wait.until(EC.visibility_of_element_located((
            By.XPATH, "//h4[contains(text(),'successfully added to your shopping cart')]")))

        # Verify the modal contains the success message
        if not modal_title:
            self.fail("Success modal did not appear or the message is incorrect.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()