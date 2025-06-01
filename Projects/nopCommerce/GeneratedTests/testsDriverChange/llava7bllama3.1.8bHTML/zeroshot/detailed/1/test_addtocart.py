import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchBook(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_search_book(self):
        # Navigate to the homepage
        self.driver.get("http://max/")

        # Click on "Search" from the main menu
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Search')]")))
        search_button.click()

        # Type the search term "book" into the search field
        search_field = self.driver.find_element(By.NAME, 'q')
        search_field.send_keys("book")

        # Submit the search
        search_form = self.driver.find_element(By.ID, 'searchform')
        search_form.submit()

        # Wait for the product grid to load
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='product-grid']//article")))

        # Locate the first product result and click the "Add to cart" button
        product_grid = self.driver.find_element(By.XPATH, "//div[@class='product-grid']")
        first_product = product_grid.find_elements(By.XPATH, ".//article")[0]
        add_to_cart_button = first_product.find_element(By.XPATH, ".//button[@title='Add to Cart']")
        add_to_cart_button.click()

        # Wait for the notification bar to appear "The product has been added to your shopping cart"
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element((By.ID, 'notification-bar'), 'The product has been added to your shopping cart'))

        # From the notification, click the "shopping cart" link
        notification_bar = self.driver.find_element(By.ID, 'notification-bar')
        shopping_cart_link = notification_bar.find_elements(By.XPATH, ".//a")[0]
        shopping_cart_link.click()

        # On the cart page, verify that the expected product is present
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h2[contains(text(), 'Your Cart')]")))
        self.assertTrue(self.is_product_in_cart("book"))

    def tearDown(self):
        self.driver.quit()

    def is_product_in_cart(self, product_name):
        cart_page = self.driver.find_element(By.XPATH, "//div[@class='cart-page']")
        products = cart_page.find_elements(By.XPATH, ".//table[@class='product-list']//td[2]")
        for product in products:
            if product.text.strip() == product_name:
                return True
        return False

if __name__ == '__main__':
    unittest.main()