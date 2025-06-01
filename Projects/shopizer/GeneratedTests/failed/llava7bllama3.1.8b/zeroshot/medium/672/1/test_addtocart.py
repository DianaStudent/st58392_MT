from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestCartFunctionality(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_cart_functionality(self):
        # Open the home page
        self.driver.get('http://localhost/')

        # Hover over a product image to reveal the "Add to cart" button
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-list']//li[1]"))).click()

        # Click the "Add to cart" button
        add_to_cart_button = self.driver.find_element_by_xpath("//button[@class='add-to-cart']")
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        cart_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@title='View my shopping cart']")))
        cart_icon.click()

        # Verify that at least one product is listed in the popup cart
        cart_popup = self.driver.find_element_by_xpath("//div[@class='cart-popup']")
        self.assertTrue(cart_popup.is_displayed(), "Cart popup not displayed")

        cart_contents = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//table[@class='cart-contents']//tr")))
        self.assertGreater(len(cart_contents.find_elements_by_xpath(".//td")), 0, "No products in cart")

if __name__ == "__main__":
    unittest.main()