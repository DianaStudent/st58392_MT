from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        service = ChromeService(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8080/en/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        try:
            # Find the Art category link
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']"))
            )
            art_category_link.click()

            # Find the "The best is yet to come' Framed poster" product link
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/art/3-the-best-is-yet-to-come-framed-poster.html#/19-dimension-40x60cm']"))
            )
            product_link.click()

            # Find the "Add to cart" button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "add-to-cart"))
            )
            add_to_cart_button.click()

            # Wait for the modal to appear
            modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )

            # Verify the success message in the modal title
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "myModalLabel"))
            )
            self.assertIn("successfully added", modal_title.text.lower())

        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()