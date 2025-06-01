import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("file://path_to_your_html_file/home_page.html")  # Load the local file

    def test_add_to_cart(self):
        driver = self.driver

        try:
            # Navigate to Category A
            category_a_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a']"))
            )
            category_a_link.click()

            # Load the Category A page from local file
            driver.get("file://path_to_your_html_file/category_a_page.html")

            # Navigate to Product A
            product_a_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()

            # Load the Product page from local file
            driver.get("file://path_to_your_html_file/product_page.html")

            # Add product to cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()

            # Load the Popup from local file, simulating that the product is added
            driver.get("file://path_to_your_html_file/popup.html")

            # Click on the cart button
            cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//span[@class='cart-button']"))
            )
            cart_button.click()

            # Verify if "GO TO CHECKOUT" is present which indicates success
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Go to checkout')]"))
            )

            if not go_to_checkout_button:
                self.fail("Failed to find 'GO TO CHECKOUT' button")

        except Exception as e:
            self.fail(f"Test failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()