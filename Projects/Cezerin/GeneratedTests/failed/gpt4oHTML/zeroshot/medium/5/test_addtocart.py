from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get('data:text/html;charset=utf-8,' + html_data["home_page"])
        self.driver.implicitly_wait(10)

    def test_add_to_cart_process(self):
        driver = self.driver

        # Click on product category
        try:
            category_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a']"))
            )
            category_link.click()
        except Exception as e:
            self.fail("Category link is not found or could not be clicked: " + str(e))

        # Navigate to the category_a_page
        driver.get('data:text/html;charset=utf-8,' + html_data["category_a_page"])

        # Select the first product
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
            )
            product_link.click()
        except Exception as e:
            self.fail("Product link is not found or could not be clicked: " + str(e))

        # Navigate to the product_page
        driver.get('data:text/html;charset=utf-8,' + html_data["product_page"])

        # Click the "Add to cart" button
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart .button.is-success"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail("Add to cart button is not found or could not be clicked: " + str(e))

        # Click the cart icon/button to open shopping bag
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button"))
            )
            cart_button.click()
        except Exception as e:
            self.fail("Cart button is not found or could not be clicked: " + str(e))

        # Navigate to the popup
        driver.get('data:text/html;charset=utf-8,' + html_data["popup"])

        # Verify that "GO TO CHECKOUT" button is present inside the cart
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/checkout']"))
            )
            if not go_to_checkout_button.is_displayed():
                self.fail("GO TO CHECKOUT button is not displayed.")
        except Exception as e:
            self.fail("GO TO CHECKOUT button is not found: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()