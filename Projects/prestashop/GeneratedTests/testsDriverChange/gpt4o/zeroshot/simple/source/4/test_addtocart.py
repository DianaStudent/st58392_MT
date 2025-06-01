from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCartProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        
        try:
            # Navigate to the "Art" category from the home page
            art_category_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Art")))
            art_category_link.click()

            # Click on a specific product in the "Art" category
            product_link = self.wait.until(EC.presence_of_element_located(
                (By.PARTIAL_LINK_TEXT, "The best is yet to come")
            ))
            product_link.click()

            # Ensure the "Add to cart" button is present and click it
            add_to_cart_button = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "button.add-to-cart")
            ))
            add_to_cart_button.click()

            # Verify the modal appears and contains the success message
            modal_title = self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "h4.modal-title")
            ))
            self.assertIn("successfully added", modal_title.text.lower())

        except (TimeoutException, NoSuchElementException) as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()