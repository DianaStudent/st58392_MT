import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open home page.
        driver.get("http://localhost:3000/")  # replace with the actual URL

        # 2. Click on product category link with href="/category-a"
        category_a_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        if not category_a_link:
            self.fail("Category A link is not present on the home page.")
        category_a_link.click()

        # 3. Select the first product link with href="/category-a/product-a"
        product_a_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']")))
        if not product_a_link:
            self.fail("Product A link is not present in Category A page.")
        product_a_link.click()

        # 4. Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Add to cart']")))
        if not add_to_cart_button:
            self.fail("Add to cart button is not present on the product page.")
        add_to_cart_button.click()

        # 5. Click the cart icon/button (shopping bag)
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        if not cart_button:
            self.fail("Cart button is not present on the product page.")
        cart_button.click()

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout']")))
        if not go_to_checkout_button:
            self.fail("GO TO CHECKOUT button is not present in the mini-cart.")

        # If we reach here, it means all assertions have passed
        print("Test completed successfully.")


if __name__ == "__main__":
    unittest.main()