import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Click on 'Category A'
        category_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        self.assertIsNotNone(category_a, "Category A link is missing.")
        category_a.click()

        # Step 2: Select 'Product A'
        product_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        self.assertIsNotNone(product_a, "Product A link is missing.")
        product_a.click()

        # Step 3: Click 'Add to cart' button
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        self.assertIsNotNone(add_to_cart_btn, "Add to cart button is missing.")
        add_to_cart_btn.click()

        # Step 4: Click on the cart button to open mini-cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        self.assertIsNotNone(cart_button, "Cart button is missing.")
        cart_button.click()

        # Step 5: Verify 'GO TO CHECKOUT' button is present
        go_to_checkout = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertIsNotNone(go_to_checkout, "GO TO CHECKOUT button is missing.")

        # Step 6: Click 'GO TO CHECKOUT' button
        go_to_checkout.click()

        # Step 7: Fill checkout fields
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        self.assertIsNotNone(email_field, "Email field is missing.")
        email_field.send_keys("mail@mail.com")

        mobile_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        self.assertIsNotNone(mobile_field, "Mobile field is missing.")
        mobile_field.send_keys("12345678")

        state_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        self.assertIsNotNone(state_field, "State field is missing.")
        state_field.send_keys("Riga")

        city_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        self.assertIsNotNone(city_field, "City field is missing.")
        city_field.send_keys("Riga")

        # Step 8: Select shipping method
        shipping_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='shipping_method_id']")))
        self.assertIsNotNone(shipping_method, "Shipping method radio button is missing.")
        shipping_method.click()

        # Step 9: Select payment method
        payment_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='payment_method_id']")))
        self.assertIsNotNone(payment_method, "Payment method radio button is missing.")
        payment_method.click()

        # Step 10: Click 'Next' button
        next_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap button")))
        self.assertIsNotNone(next_button, "Next button is missing.")
        next_button.click()

        # Step 11: Click 'Place Order' button
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.is-primary")))
        self.assertIsNotNone(place_order_button, "Place Order button is missing.")
        place_order_button.click()

        # Step 12: Confirm success page contains 'Thanks for your order!'
        success_message = self.wait.until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]")))
        self.assertIsNotNone(success_message, "Success message is missing on the final page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()