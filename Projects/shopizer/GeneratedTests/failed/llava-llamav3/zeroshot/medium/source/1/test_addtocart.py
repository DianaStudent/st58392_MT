from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestShoppingCart(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().get_chrome_driver())

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Step 1: Open the home page
        self.driver.get('http://localhost/')

        # Step 2: Hover over a product image to reveal the "Add to cart" button
        product_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "product-1")]')))
        ActionChains(self.driver).move_to_element(product_element)

        # Step 3: Click the "Add to cart" button
        self.driver.find_elements_by_css_selector('button.add-to-cart')[0].click()

        # Step 4: Open the cart popup by clicking the cart icon
        self.driver.get('http://localhost/cart')

        # Step 5: Verify that at least one product is listed in the popup cart
        item_in_cart = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[contains(@id, "item-cart-1")]')))