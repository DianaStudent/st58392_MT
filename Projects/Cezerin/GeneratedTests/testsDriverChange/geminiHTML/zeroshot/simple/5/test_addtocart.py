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
        # Find the link to Category A/Product A on the home page and navigate to the product page
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_link.click()
        except Exception as e:
            self.fail(f"Could not find or click product link: {e}")

        # Find the "Add to cart" button on the product page and click it
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Add to cart' button: {e}")

        # Click on the cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the cart button: {e}")

        # Verify that the "GO TO CHECKOUT" button is present in the mini-cart
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout"))
            )
            self.assertTrue(go_to_checkout_button.is_displayed(), "Go to checkout button is not displayed")
        except Exception as e:
            self.fail(f"Could not find 'GO TO CHECKOUT' button or it's not displayed: {e}")


if __name__ == "__main__":
    unittest.main()