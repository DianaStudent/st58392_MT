from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        # Step 2: Click on the "Art" category from the top menu
        art_category = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, "//a[text()='Art']"))
        )
        art_category.click()

        # Step 3: Select the first product listed in the category
        first_product = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.product-thumbnail"))
        )
        first_product.click()

        # Step 4: Click the "Add to cart" button on the product detail page
        add_to_cart_button = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_button.click()

        # Step 5: Wait for the modal popup that confirms the product was added to the cart
        modal = self.wait.until(
            EC.visibility_of_element_located((By.ID, "blockcart-modal"))
        )

        # Step 6: Verify the modal contains a message like "Product successfully added to your shopping cart"
        modal_title = self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".modal-title"))
        )
        title_text = modal_title.text

        if not title_text or "successfully added" not in title_text.lower():
            self.fail("Modal title does not confirm product was added to the cart successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()