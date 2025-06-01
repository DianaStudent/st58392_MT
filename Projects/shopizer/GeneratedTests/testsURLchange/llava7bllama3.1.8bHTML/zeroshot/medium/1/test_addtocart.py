import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_cart(self):
        # Open the home page
        self.driver.get("http://localhost/")

        # Hover over a product image to reveal the "Add to cart" button.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//ul[@class='products']/li[1]/a"))).click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-image']//img"))).move_to_element(self.driver.find_element(By.XPATH, "//div[@class='product-image']//img"))
        # Click the "Add to cart" button.
        self.driver.find_element(By.XPATH, "//button[@title='Add to Cart']").click()

        # Open the cart popup by clicking the cart icon.
        self.driver.find_element(By.XPATH, "//span[@class='cart-icon']").click()
        
        # Verify that at least one product is listed in the popup cart.
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@title='View your shopping cart']"))).click()

        cart_items = self.driver.find_elements(By.XPATH, "//div[@class='product-cart-list-item']")
        if len(cart_items) < 1:
            self.fail("The popup cart is empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()