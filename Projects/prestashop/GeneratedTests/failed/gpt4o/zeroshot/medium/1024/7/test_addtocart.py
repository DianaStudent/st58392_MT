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
        self.driver.get('http://localhost:8080/en/')

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on the "Art" category from the top menu
        art_category = wait.until(
            EC.presence_of_element_located((By.XPATH, '//a[text()="Art"]'))
        )
        if not art_category:
            self.fail("Art category link not found.")
        art_category.click()

        # Step 3: Select the first product listed in the "Art" category
        first_product = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//a[contains(@href, "art/3-13-the-best-is-yet-to-come-")]'))
        )
        if not first_product:
            self.fail("First product link not found in the Art category.")
        first_product.click()

        # Step 4: Click the "Add to cart" button on the product detail page
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary add-to-cart"]'))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found on the product detail page.")
        add_to_cart_button.click()

        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        modal_title = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, '//h4[contains(@class, "modal-title")][contains(text(), "successfully added")]')
            )
        )
        if not modal_title:
            self.fail("Success modal not found after adding product to cart.")
        
        # Step 6: Verify the modal contains the confirmation message
        self.assertTrue(
            "successfully added" in modal_title.text,
            "The confirmation message is incorrect or missing from the modal."
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()