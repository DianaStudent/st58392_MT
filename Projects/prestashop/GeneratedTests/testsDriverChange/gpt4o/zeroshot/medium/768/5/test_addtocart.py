import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click on a product category from the top menu
        category = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))
        category.click()

        # Select the first product listed in the category
        first_product = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-13-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']")))
        first_product.click()

        # Click the "Add to cart" button on the product detail page
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn.btn-primary.add-to-cart")))
        add_to_cart_button.click()

        # Wait for the modal popup that confirms the product was added to the cart
        modal_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h4.modal-title.h6.text-sm-center")))

        # Verify the modal contains a success message
        if modal_title is None or modal_title.text.strip() == "":
            self.fail("Modal title not found or empty.")

        self.assertIn("Product successfully added to your shopping cart", modal_title.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()