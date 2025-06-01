from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def test_add_to_cart(self):
        # Click on "Search" from the main menu.
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Search']"))
        )
        search_button.click()

        # Type the search term "book" into the search field.
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, 'search'))
        )
        search_input.send_keys("book")

        # Submit the search.
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Search']"))
        )
        submit_button.click()

        # Wait for the product grid to load.
        product_grid = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'product-grid'))
        )

        # Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = product_grid.find_elements(By.XPATH, ".//button")[0]
        add_to_cart_button.click()

        # Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'notification-bar'))
        )
        self.assertEqual(notification_bar.text, "The product has been added to your shopping cart")

        # From the notification, click the "shopping cart" link.
        cart_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='shopping cart']"))
        )
        cart_link.click()

        # On the cart page, verify that the expected product is present.
        product_name = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//span[@class='product-name'])[1]"))
        )
        self.assertIsNotNone(product_name.text)
        self.assertNotEqual(product_name.text.strip(), "")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()