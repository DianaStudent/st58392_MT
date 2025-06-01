from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart(self):
        # Add product to cart
        add_to_bag_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-bag-button']")))
        add_to_bag_button.click()

        # Click on cart button and wait for "GO TO CHECKOUT" button to appear
        cart_button = self.driver.find_element(By.XPATH, "//a[@class='cart-link']")
        cart_button.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-test='go-to-checkout-button']")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()