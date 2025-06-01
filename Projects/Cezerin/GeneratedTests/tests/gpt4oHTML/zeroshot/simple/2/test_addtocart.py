import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("url_of_the_home_page")  # Replace with actual URL
        self.wait = WebDriverWait(self.driver, 20)

    def test_add_to_cart(self):
        driver = self.driver

        # Navigate to Category A
        try:
            category_a_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
            category_a_link.click()
        except Exception as e:
            self.fail(f"Category A link not found or clickable: {str(e)}")

        # Navigate to Product A
        try:
            product_a_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
            product_a_link.click()
        except Exception as e:
            self.fail(f"Product A link not found or clickable: {str(e)}")

        # Add Product A to the cart
        try:
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or clickable: {str(e)}")

        # Click to open the cart popup
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']")))
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found or clickable: {str(e)}")

        # Verify if the 'GO TO CHECKOUT' button is present
        try:
            go_to_checkout_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Go to checkout']")))
        except Exception as e:
            self.fail(f"GO TO CHECKOUT button not found or not clickable: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()