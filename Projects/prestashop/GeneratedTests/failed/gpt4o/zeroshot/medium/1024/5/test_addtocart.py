from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        # Setup Chrome WebDriver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost:8080/en/"

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.base_url)

        try:
            # Select the category 'Art' from the top menu
            category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            category_link.click()

            # Select the first product in the 'Art' category
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-title a"))
            )
            first_product.click()

            # Click 'Add to cart' button
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.add-to-cart"))
            )
            add_to_cart_button.click()

            # Wait for the modal popup and verify the presence of success message
            modal_title = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".modal-title h6"))
            )

            self.assertIn("successfully added", modal_title.text)

        except Exception as e:
            self.fail(f"An element was not found or another exception occurred: {str(e)}")

    def tearDown(self):
        # Teardown the test case
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()