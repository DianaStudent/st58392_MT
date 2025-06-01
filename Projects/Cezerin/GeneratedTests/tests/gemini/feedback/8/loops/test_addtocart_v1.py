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
        self.base_url = "http://localhost:3000/"
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart(self):
        driver = self.driver
        # 1. Open home page.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Click on product category.
        category_a_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Category A"))
        )
        if category_a_link:
            category_a_link.click()
        else:
            self.fail("Category A link not found")

        # 3. Select the first product.
        product_a_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Product A"))
        )

        if product_a_link:
            product_a_link.click()
        else:
            self.fail("Product A link not found")

        # 4. Click the "Add to cart" button.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "button.is-success.is-fullwidth"))
        )

        if add_to_cart_button:
            add_to_cart_button.click()
        else:
            self.fail("Add to cart button not found")
            
        # 5. Click the cart icon/button to open the shopping bag.
        cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "cart-button"))
        )
        if cart_button:
            cart_button.click()
        else:
            self.fail("Cart button not found")

        # 6. Verify that the "GO TO CHECKOUT" button is present inside the cart.
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout"))
        )

        if go_to_checkout_button:
            self.assertTrue(go_to_checkout_button.is_displayed(), "GO TO CHECKOUT button is not displayed")
        else:
            self.fail("GO TO CHECKOUT button not found")


if __name__ == "__main__":
    unittest.main()