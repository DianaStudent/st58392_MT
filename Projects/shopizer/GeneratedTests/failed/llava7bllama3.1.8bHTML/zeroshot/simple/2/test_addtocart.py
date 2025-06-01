from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCartPopup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_cart_popup(self):
        # Navigate to the page
        self.driver.get("http://localhost/")  # Replace with actual URL

        # Hover over a product item
        product_item = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@class='product-item']")))
        product_item.hover()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']")))
        add_to_cart_button.click()

        # Open the cart popup
        cart_icon = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@id='cart-icon']")))
        cart_icon.click()

        # Confirm success by checking that the popup contains at least one item
        cart_popup_items = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='cart-popup-item']")))
        self.assertGreater(len(cart_popup_items), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()