from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Step 2: Click on the "Art" category from the top menu
        art_category_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/en/9-art')]")))
        art_category_link.click()

        # Step 3: Select the first product listed in the category
        first_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '/en/art/3-13-the-best-is-yet-to-come-framed-poster.html')]")))
        first_product.click()

        # Step 4: On the product detail page, click the "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'add-to-cart')]")))
        add_to_cart_button.click()

        # Step 5: Wait for the modal popup
        modal = self.wait.until(EC.visibility_of_element_located((By.ID, "blockcart-modal")))

        # Step 6: Verify the modal contains confirmation message
        modal_title = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//h4[contains(@class, 'modal-title') and contains(text(), 'successfully added')]")))

        self.assertIsNotNone(modal_title.text, "Confirmation modal title is missing or empty")
        if not modal_title.text:
            self.fail("The confirmation message in modal is missing or empty")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()