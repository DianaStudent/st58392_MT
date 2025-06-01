import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCartPopup(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_cart_popup(self):
        # Open the webpage
        self.driver.get("http://example.com")  # Replace with your webpage URL

        # Find product item
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "div.product-item"))
        )
        product_item = self.driver.find_element(By.CSS_SELECTOR, "div.product-item")

        # Hover over product item to reveal the "Add to cart" button
        hover_action = self.driver.actions()
        hover_action.move_to_element(product_item).perform()

        # Find and click the "Add to cart" button
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#add-to-cart-button"))
        )
        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-button")
        add_to_cart_button.click()

        # Open the cart popup by clicking the cart icon
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "i.cart-icon"))
        )
        cart_icon = self.driver.find_element(By.CSS_SELECTOR, "i.cart-icon")
        cart_icon.click()

        # Confirm success by checking that the popup contains at least one item
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#cart-items"))
        )
        cart_items = self.driver.find_element(By.CSS_SELECTOR, "#cart-items")
        self.assertGreater(len(cart_items.text.splitlines()), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()