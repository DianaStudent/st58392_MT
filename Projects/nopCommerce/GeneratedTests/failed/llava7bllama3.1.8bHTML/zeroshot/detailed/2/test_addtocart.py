from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestSearchProduct(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_search_product(self):
        # Navigate to the homepage.
        self.driver.get("http://max/")  # replace with actual url

        # Click on "Search" from the main menu.
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/search']"))
        )
        search_button.click()

        # Type the search term "book" into the search field.
        search_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_query"))
        )
        search_field.send_keys("book")

        # Submit the search.
        submit_search = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        )
        submit_search.click()

        # Wait for the product grid to load.
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='product-grid']"))
        )

        # Locate the first product result and click the "Add to cart" button.
        first_product = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//table[@class='product-grid'])[1]/tr/td/a"))
        )
        first_product.click()

        # Wait for the notification bar to appear "The product has been added to your shopping cart".
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='success-notification']"))
        )

        # From the notification, click the "shopping cart" link.
        cart_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        cart_link.click()

        # On the cart page, verify that the expected product is present.
        cart_table = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//table[@class='cart-table']"))
        )

        self.assertIsNotNone(cart_table.text)
        products_in_cart = cart_table.find_elements(By.TAG_NAME, "tr")
        self.assertGreater(len(products_in_cart), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()