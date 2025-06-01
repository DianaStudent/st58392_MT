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
    
    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to Art category
        art_category_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/en/9-art')]"))
        )
        art_category_link.click()

        # Navigate to product detail page
        product_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'/en/art/3-13-the-best-is-yet-to-come-framed-poster.html')]"))
        )
        product_link.click()

        # Add the product to the cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
        )
        add_to_cart_button.click()

        # Wait for the confirmation modal to appear
        modal_title = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h4[contains(text(), 'Product successfully added to your shopping cart')]"))
        )

        # Verify the modal confirmation
        self.assertIn("successfully added", modal_title.text, "Modal confirmation not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()