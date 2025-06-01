from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")
        self.driver.maximize_window()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Click on the menu button
        menu_button = wait.until(EC.element_to_be_clickable((By.ID, "headlessui-popover-button-:R6qdtt7:")))
        menu_button.click()

        # Step 3: Click on the "Store" link
        store_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='store-link']")))
        store_link.click()

        # Step 4: Click on a product image (thumbnail)
        product_thumbnail = wait.until(EC.presence_of_element_located((By.XPATH, "//img[@alt='Thumbnail']")))
        product_thumbnail.click()

        # Step 5: Select a size
        size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
        size_button.click()

        # Step 6: Click the "Add to Cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
        add_to_cart_button.click()

        # Step 7: Click the cart button to open the cart
        cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # Step 8: Verify that the "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))

        if not go_to_checkout_button:
            self.fail("The 'GO TO CHECKOUT' button was not found or is empty.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()