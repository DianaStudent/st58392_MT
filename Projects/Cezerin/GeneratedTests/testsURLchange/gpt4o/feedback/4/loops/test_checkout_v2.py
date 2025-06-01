import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open home page
        driver.get("http://localhost:3000/")

        # Step 2: Click on product category
        category_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]'))
        )
        self.assertIsNotNone(category_link, "Category link not found.")
        category_link.click()

        # Step 3: Select the first product
        product_link = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a/product-a"]'))
        )
        self.assertIsNotNone(product_link, "Product link not found.")
        product_link.click()

        # Step 4: Click the "Add to cart" button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.button-addtocart .button'))
        )
        self.assertIsNotNone(add_to_cart_button, "Add to cart button not found.")
        add_to_cart_button.click()

        # Step 5: Click the cart icon/button to open the shopping bag
        cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.cart-button'))
        )
        self.assertIsNotNone(cart_button, "Cart button not found.")
        cart_button.click()

        # Step 6: Verify that the "GO TO CHECKOUT" button is present inside the cart
        go_to_checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href="/checkout"]'))
        )
        self.assertIsNotNone(go_to_checkout_button, "GO TO CHECKOUT button not found.")

        # Step 7: Click the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Step 8: Fill required checkout fields
        email_input = wait.until(
            EC.presence_of_element_located((By.ID, "customer.email"))
        )
        self.assertIsNotNone(email_input, "Email input not found.")
        email_input.send_keys("mail@mail.com")

        phone_input = driver.find_element(By.ID, "customer.mobile")
        self.assertIsNotNone(phone_input, "Phone input not found.")
        phone_input.send_keys("12345678")

        state_input = driver.find_element(By.ID, "shipping_address.state")
        self.assertIsNotNone(state_input, "State input not found.")
        state_input.send_keys("Riga")

        city_input = driver.find_element(By.ID, "shipping_address.city")
        self.assertIsNotNone(city_input, "City input not found.")
        city_input.send_keys("Riga")

        # Step 9: Select a shipping and payment method
        shipping_method = driver.find_element(By.CSS_SELECTOR, 'input[name="shipping_method_id"]')
        self.assertIsNotNone(shipping_method, "Shipping method not found.")
        shipping_method.click()
        
        payment_method = driver.find_element(By.CSS_SELECTOR, 'input[name="payment_method_id"]')
        self.assertIsNotNone(payment_method, "Payment method not found.")
        payment_method.click()

        # Step 10: Click "Next"
        next_button = driver.find_element(By.CSS_SELECTOR, '.checkout-button-wrap .button')
        self.assertIsNotNone(next_button, "Next button not found.")
        next_button.click()

        # Step 11: Click "Place Order" to complete the process
        place_order_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-step:nth-child(2) .checkout-button-wrap button[type="submit"]'))
        )
        self.assertIsNotNone(place_order_button, "Place Order button not found.")
        place_order_button.click()

        # Step 12: Confirm that the success page contains the message: "Thanks for your order!"
        success_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.checkout-success-title'))
        )
        self.assertIsNotNone(success_message, "Success message not found.")
        self.assertIn("Thanks for your order!", success_message.text, "Success message not found in text.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()