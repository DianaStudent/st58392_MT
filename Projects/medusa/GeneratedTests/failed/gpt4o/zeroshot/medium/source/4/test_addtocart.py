from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver
        wait = self.wait

        # Click on the menu button to open the menu
        menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="nav-menu-button"]')))
        menu_button.click()

        # Click on the "Store" link in the menu
        store_link = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="store-link"]')))
        store_link.click()

        # Click on a product image (thumbnail)
        product_thumbnail = wait.until(EC.presence_of_element_located(
            (By.XPATH, '(//ul[@data-testid="products-list"]/li//img)[1]')
        ))
        product_thumbnail.click()

        # Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="L"]')))
        size_button.click()

        # Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="add-product-button"]')))
        add_to_cart_button.click()

        # Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[@data-testid="nav-cart-link"]')))
        cart_button.click()

        # Verify that the "GO TO CHECKOUT" button is present
        checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@data-testid="checkout-button"]')))
        if not checkout_button:
            self.fail("The 'GO TO CHECKOUT' button is not present.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()