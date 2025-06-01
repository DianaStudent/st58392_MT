import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Click on 'Category A'
        category_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        if not category_a:
            self.fail("Category A link is missing.")
        category_a.click()

        # Step 2: Select 'Product A'
        product_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        if not product_a:
            self.fail("Product A link is missing.")
        product_a.click()

        # Step 3: Click 'Add to cart' button
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        if not add_to_cart_btn:
            self.fail("Add to cart button is missing.")
        add_to_cart_btn.click()

        # Step 4: Click on the cart button to open mini-cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        if not cart_button:
            self.fail("Cart button is missing.")
        cart_button.click()

        # Step 5: Verify 'GO TO CHECKOUT' button is present
        go_to_checkout = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        if not go_to_checkout:
            self.fail("GO TO CHECKOUT button is missing.")
        
        # Step 6: Click 'GO TO CHECKOUT' button
        go_to_checkout.click()

        # Step 7: Fill checkout fields
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        if not email_field:
            self.fail("Email field is missing.")
        email_field.send_keys("mail@mail.com")

        mobile_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        if not mobile_field:
            self.fail("Mobile field is missing.")
        mobile_field.send_keys("12345678")

        state_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        if not state_field:
            self.fail("State field is missing.")
        state_field.send_keys("Riga")

        city_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        if not city_field:
            self.fail("City field is missing.")
        city_field.send_keys("Riga")

        # Step 8: Select shipping method
        shipping_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='shipping_method_id']")))
        if not shipping_method:
            self.fail("Shipping method radio button is missing.")
        shipping_method.click()

        # Step 9: Select payment method
        payment_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='payment_method_id']")))
        if not payment_method:
            self.fail("Payment method radio button is missing.")
        payment_method.click()

        # Step 10: Click 'Next' button
        next_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap button")))
        if not next_button:
            self.fail("Next button is missing.")
        next_button.click()

        # Step 11: Click 'Place Order' button
        place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button.is-primary")))
        if not place_order_button:
            self.fail("Place Order button is missing.")
        place_order_button.click()

        # Step 12: Confirm success page contains 'Thanks for your order!'
        success_message = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Thanks for your order!')]"))
        )
        if not success_message:
            self.fail("Success message is missing on the final page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()