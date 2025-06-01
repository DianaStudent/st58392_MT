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

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        try:
            # Find the Art category and click on it
            art_category = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '9-art')]"))
            )
            art_category.click()

            # Find the product "The best is yet to come' Framed poster" and click on it
            product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@href, '3-13-the-best-is-yet-to-come-framed-poster.html')]"))
            )
            product.click()

            # Select the dimension
            dimension_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "group_3"))
            )

            # Find the "Add to cart" button and click it
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'add-to-cart')]"))
            )
            add_to_cart_button.click()

            # Wait for the modal to appear
            modal = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "blockcart-modal"))
            )

            # Verify the modal title
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h4[@class='modal-title h6 text-sm-center' and contains(text(), 'successfully added')]"))
            )
            self.assertTrue(modal_title.is_displayed(), "Modal title not found or not displayed.")

        except Exception as e:
            self.fail(f"Test failed: {e}")

if __name__ == "__main__":
    unittest.main()