from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class AddToCartTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_add_to_cart_process(self):
        driver = self.driver
        
        # Wait and click the menu button
        try:
            menu_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "headlessui-popover-button-:R6qdtt7:"))
            )
            menu_button.click()
        except:
            self.fail("Menu button not found or not interactable.")

        # Wait and click on the store link from the menu
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Store"))
            )
            store_link.click()
        except:
            self.fail("Store link not found in menu.")

        # Wait and click on a product link (e.g. Medusa Sweatshirt)
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except:
            self.fail("Product link not found.")

        # Wait and select a size
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='L']"))
            )
            size_button.click()
        except:
            self.fail("Size button not found or not interactable.")

        # Wait and click the add to cart button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not interactable.")

        # Wait and click on the cart link
        try:
            cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']"))
            )
            cart_link.click()
        except:
            self.fail("Cart link not found or not interactable.")

        # Wait for the "GO TO CHECKOUT" button
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Go to checkout']"))
            )
        except:
            self.fail("Go to checkout button not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()