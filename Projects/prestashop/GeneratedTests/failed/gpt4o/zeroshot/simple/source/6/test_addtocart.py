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

        try:
            # Go to Art category
            art_category_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()

            # Go to the specific product page
            product_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "The best is yet to come'..."))
            )
            product_link.click()

            # Wait for the Add to Cart button and click it
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary.add-to-cart"))
            )
            add_to_cart_button.click()

            # Wait for the modal to appear and verify it
            modal_success = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h4[contains(text(), 'Product successfully added to your shopping cart')]")
                )
            )
            self.assertIsNotNone(modal_success, "Success modal did not appear.")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()