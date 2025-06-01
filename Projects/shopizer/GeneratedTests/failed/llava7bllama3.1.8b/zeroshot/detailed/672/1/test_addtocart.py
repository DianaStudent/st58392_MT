from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost/')

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        # Open the home page
        self.assertEqual(self.driver.title, 'Home Page')

        # Hover over the first product to reveal "Add to cart" button
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-item']")))
        self.driver.find_element_by_xpath("//div[@class='product-item']").click()

        # Click the revealed "Add to cart" button
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@data-action='add-to-cart']")))
        self.driver.find_element_by_xpath("//button[@data-action='add-to-cart']").click()

        # Open the popup cart by clicking the cart icon
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='cart-icon']")))
        self.driver.find_element_by_xpath("//a[@class='cart-icon']").click()

        # Wait for the popup to become visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='popup-cart']")))

        # Click "View cart" or similar button inside the popup
        self.driver.find_element_by_xpath("//button[@data-action='view-cart']").click()

        # On the cart page, verify that the product appears in the cart list
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//table[@class='cart-table']")))
        self.assertIn('Product Name', self.driver.page_source)

if __name__ == '__main__':
    unittest.main()