import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class AddToCartTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_add_to_cart_and_checkout(self):
        driver = self.driver

        # Step 2: Click on product category
        category_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']"))
        )
        category_link.click()

        # Step 3: Select the first product
        first_product_link = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']"))
        )
        first_product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.button.is-success.is-fullwidth"))
        )
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span.cart-button"))
        )
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a.button.is-primary.is-fullwidth.has-text-centered"))
        )

        if not go_to_checkout_button.is_displayed():
            self.fail("GO TO CHECKOUT button is not present in the cart.")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()
        
        # Step 8: Fill required checkout fields
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")

        mobile_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        mobile_field.send_keys("12345678")

        state_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        state_field.send_keys("Riga")

        city_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        city_field.send_keys("Riga")
        
        # Step 9: Select a shipping and payment method
        shipping_method = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='shipping_method_id']"))
        )
        shipping_method.click()

        payment_method = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='payment_method_id']"))
        )
        payment_method.click()

        # Step 10: Click "Next" and then "Place Order" to complete the process
        next_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.checkout-button.is-primary"))
        )
        next_button.click()

        place_order_button = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[class*='is-primary']"))
        )
        place_order_button.click()

        # Step 11: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-success-title"))
        )
        
        if not success_message.is_displayed() or "Thanks for your order!" not in success_message.text:
            self.fail("Order success message not found or incorrect.")

if __name__ == "__main__":
    unittest.main()