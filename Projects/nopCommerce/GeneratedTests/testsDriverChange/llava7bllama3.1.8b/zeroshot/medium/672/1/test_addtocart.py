import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_add_book_to_cart(self):
        # Click on the "Search" link in the top navigation
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Search')))
        search_link.click()

        # Enter "book" in the search field and submit the search
        search_field = self.driver.find_element_by_name('search')
        search_field.send_keys("book")
        search_button = self.driver.find_element_by_css_selector('.search-submit')
        search_button.click()

        # On the search results page, locate the first product and click "Add to cart"
        product_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.product-title')))
        product_link.click()
        add_to_cart_button = self.driver.find_element_by_css_selector('.add-to-cart')
        add_to_cart_button.click()

        # Wait for the success notification to appear
        success_notification = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.woocommerce-message')))

        # Click the "shopping cart" link inside the notification
        shopping_cart_link = self.driver.find_element_by_css_selector('.woocommerce-message a')
        shopping_cart_link.click()

        # Confirm success by checking that the cart page contains the added product
        cart_contents = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.woocommerce-cart-form__contents')))
        self.assertEqual(len(cart_contents.text.split('\n')), 2)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()