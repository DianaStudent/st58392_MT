import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def setUp(self):
    self.driver = webdriver.Chrome()
    self.wait = WebDriverWait(self.driver, 20)

class TestAddToCart(unittest.TestCase):
    def test_add_to_cart(self):
        # Open the website
        self.wait.until(lambda x: "http" in x.current_url())

        # Find the product to add
        product = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//img[contains(@src,'product-1.jpg')]"))))

        # Click on the product
        product.click()

        # Find and click the cart button
        cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'GO TO CHECKOUT')]"))))
        cart_button.click()

        # Check if the "Go to Checkout" button is visible
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[contains(@type,'button') and contains(@class,'btn btn-primary')]"))))

if __name__ == "__main__":
    unittest.main()