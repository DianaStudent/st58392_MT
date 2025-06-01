import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestAddToCartProcess(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)  # Implicit wait

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        driver.get("http://example.com")  # Replace with the actual URL

        # Step 2: Click on the product category
        category_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(@class, 'button-addtocart')]")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//span[contains(@class, 'cart-button')]")))
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(@class, 'button is-primary is-fullwidth') and contains(text(), 'Go to checkout')]")))
        
        # Assert that the "GO TO CHECKOUT" button is visible
        if not go_to_checkout_button:
            self.fail("The 'GO TO CHECKOUT' button was not found or is not visible in the cart.")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()