from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")

    def test_add_to_cart(self):
        # Click on 'Add to Cart' button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        add_to_cart_button.click()

        # Wait for presence of "GO TO CHECKOUT" button
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@id='cart']/p[3]/button"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()