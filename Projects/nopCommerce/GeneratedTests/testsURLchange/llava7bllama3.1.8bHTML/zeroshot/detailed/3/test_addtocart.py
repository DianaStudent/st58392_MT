import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")  # Replace with the actual homepage URL

    def tearDown(self):
        self.driver.quit()

    def test_shopping_cart(self):
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Search')]"))
        )
        search_button.click()

        search_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search_term"))
        )
        search_field.send_keys("book")
        search_field.send_keys(Keys.RETURN)

        # Wait for the product grid to load
        product_grid = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-grid']"))
        )

        first_product = WebDriverWait(product_grid, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//a[@class='add-to-cart'])[1]"))
        )
        first_product.click()

        notification_bar = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//div[@class='notification-bar']"))
        )

        self.assertIn("The product has been added to your shopping cart", notification_bar.text)

        cart_link = notification_bar.find_element(By.TAG_NAME, "a")
        cart_link.click()

        cart_page = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='cart-page']"))
        )

        cart_item = WebDriverWait(cart_page, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//a[@class='remove-item'])[1]"))
        )
        self.assertGreater(len(cart_item.text), 0)

if __name__ == "__main__":
    unittest.main()