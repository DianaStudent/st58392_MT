from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
    
    def test_add_to_cart(self):
        driver = self.driver

        # Wait for and click on Art category link
        try:
            art_category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Art"))
            )
            art_category_link.click()
        except Exception as e:
            self.fail(f"Art category link not found or clickable: {e}")

        # Wait for and click on 'The best is yet to come' product link
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//h2[@class='h3 product-title']/a[contains(text(), \"The best is yet to come\")]"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Product link 'The best is yet to come' not found or clickable: {e}")

        # Wait for and click on Add to Cart button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'add-to-cart')]"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to Cart button not found or clickable: {e}")

        # Wait for modal popup confirmation
        try:
            modal_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//h4[contains(@class, 'modal-title') and contains(text(), 'successfully added')]"))
            )
            self.assertIn("successfully added", modal_title.text)
        except Exception as e:
            self.fail(f"Modal popup with 'successfully added' message not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()