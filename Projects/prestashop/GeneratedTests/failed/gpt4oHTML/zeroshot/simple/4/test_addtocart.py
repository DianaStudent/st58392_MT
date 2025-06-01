from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get('http://localhost:8080/en/')

    def test_add_to_cart(self):
        driver = self.driver

        try:
            # Find and click on 'Art' category
            art_category = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category.click()

            # Find and click on a specified product
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable(
                    (By.LINK_TEXT, "The best is yet to come'..."))
            )
            product_link.click()

            # Set quantity and add the product to the cart
            quantity_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "quantity_wanted"))
            )
            quantity_input.clear()
            quantity_input.send_keys("1")

            add_to_cart_btn = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
            )
            add_to_cart_btn.click()

            # Wait for the modal confirming product is added to the cart to appear
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located(
                    (By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(),'successfully added')]"))
            )

            # Verify the success message
            self.assertIn("Product successfully added", modal_title.text)

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()