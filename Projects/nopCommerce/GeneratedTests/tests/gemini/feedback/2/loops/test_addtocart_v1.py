import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://max/"
        self.search_term = "book"

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Navigate to the homepage.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click on "Search" from the main menu.
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        # 3. Type the search term "book" into the search field.
        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_input.send_keys(self.search_term)

        # 4. Submit the search.
        search_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-1.search-box-button"))
        )
        search_button.click()

        # 5. Wait for the product grid to load.
        product_grid = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "product-grid"))
        )

        # 6. Locate the first product result and click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button-2.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 7. Wait for the notification bar to appear "The product has been added to your shopping cart".
        notification_bar = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "bar-notification"))
        )
        notification_text = notification_bar.find_element(By.CLASS_NAME, "content").text
        self.assertTrue("The product has been added to your shopping cart" in notification_text)

        # 8. From the notification, click the "shopping cart" link.
        shopping_cart_link = notification_bar.find_element(By.LINK_TEXT, "shopping cart")
        shopping_cart_link.click()

        # 9. On the cart page, verify that the expected product is present.
        cart_table = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart"))
        )

        product_name_element = cart_table.find_element(By.CLASS_NAME, "product-name")
        product_name = product_name_element.text

        self.assertTrue(product_name is not None and product_name != "", "Product name not found in cart.")
        self.assertTrue("Book1" in product_name, f"Expected 'Book1' in product name, but got '{product_name}'")

if __name__ == "__main__":
    unittest.main()