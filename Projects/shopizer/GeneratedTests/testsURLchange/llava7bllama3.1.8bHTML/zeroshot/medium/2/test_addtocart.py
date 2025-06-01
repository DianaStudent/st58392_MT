from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestCart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_cart(self):
        # Open the home page.
        self.driver.get('http://localhost/')

        # Hover over a product item to reveal the "Add to cart" button.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.product > img'))
        ).click()

        # Click the "Add to cart" button.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//button[text()="Add to cart"]'))
        ).click()

        # Open the cart popup by clicking the cart icon.
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.cart > img'))
        ).click()

        # Verify that at least one product is listed in the popup cart.
        cart_popup = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, 'cart-popup'))
        )
        self.failUnless(cart_popup.text)
        products = cart_popup.find_elements(By.TAG_NAME, 'li')
        self.assertGreater(len(products), 0)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()