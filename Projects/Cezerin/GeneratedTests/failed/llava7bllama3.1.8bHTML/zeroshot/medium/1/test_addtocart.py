from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("data:text/html," + html_data)

    def test_add_to_cart(self):
        # Open home page
        pass  # Home page is already loaded in the browser

        # Click on product category
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href=\"/category-a\"]"))).click()

        # Select the first product
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(), 'Product A')]")))

        # Click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='button is-success is-fullwidth']"))).click()

        # Click the cart icon/button to open the shopping bag.
        self.driver.find_element(By.CSS_SELECTOR, ".cart-button").click()

        # Wait for presence of "GO TO CHECKOUT" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'GO TO CHECKOUT')]")))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()