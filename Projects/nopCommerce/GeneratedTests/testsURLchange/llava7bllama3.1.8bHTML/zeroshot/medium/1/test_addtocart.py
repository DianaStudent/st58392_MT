from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")  # Replace with your homepage URL

    def test_cart(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Search"))).click()
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "searchQuery")))
        search_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        search_input.send_keys("book")
        search_button.click()

        # Add to cart
        product_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h2/a"))).text
        add_to_cart_button = self.driver.find_elements(By.XPATH, "//a[@class='add-to-cart']")[0]
        add_to_cart_button.click()

        # Wait for success notification to appear
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success-notification']")))

        # Click shopping cart link inside notification
        notification = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='success-notification']")))
        cart_link = notification.find_elements(By.TAG_NAME, "a")[0]
        cart_link.click()

        # Check that cart page contains the added product
        cart_page_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='cart-title']"))).text
        self.assertEqual(cart_page_title, "Your Cart")
        product_in_cart = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//tr[td/a[text()='{product_title}']]")))
        self.assertIsNotNone(product_in_cart)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()