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
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver

        # Find and click on the "Product A" link on the home page
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except:
            self.fail("Could not find or click on Product A link on the home page")

        # Find and click the "Add to cart" button on the product page
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-success') and text()='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click on the Add to cart button on the product page")

        # Find and click the cart button (shopping bag icon)
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']"))
            )
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button")

        # Verify that the "GO TO CHECKOUT" button is present in the mini-cart
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout"))
            )
        except:
            self.fail("The 'GO TO CHECKOUT' button is not present in the mini-cart after adding the product.")

if __name__ == "__main__":
    unittest.main()