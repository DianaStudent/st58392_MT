from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_add_to_cart_and_confirm(self):
        # Wait for the modal (popup) confirmation to appear after adding to cart
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '[data-name="blockcart-modal"]')))

        # Confirm success by verifying the presence of the modal title that contains "successfully added"
        modal_title = self.driver.find_element(By.CSS_SELECTOR, "[class='modal-title h6 text-sm-center']")
        self.assertIn("successfully added", modal_title.text)
        self.fail("Modal title does not contain 'successfully added'")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()