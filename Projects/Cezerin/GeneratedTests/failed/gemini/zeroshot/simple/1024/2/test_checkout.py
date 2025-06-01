import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to Category A
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            )
            category_a_link.click()
        except:
            self.fail("Could not find or click 'Category A' link.")

        # Click on Product A
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Product A"))
            )
            product_a_link.click()
        except:
            self.fail("Could not find or click 'Product A' link.")

        # Add Product A to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "button.is-success.is-fullwidth"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click 'Add to cart' button.")

        # Click on the cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span.cart-button img[alt='cart']"))
            )
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button.")

       # Click on "GO TO CHECKOUT" button
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Could not find or click 'Go to checkout' button.")

        # Fill in customer details
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
            email_field.send_keys("mail@mail.com")

            mobile_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "customer.mobile"))
            )
            mobile_field.send_keys("12345678")

            state_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "shipping_address.state"))
            )
            state_field.send_keys("Riga")

            city_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "shipping_address.city"))
            )
            city_field.send_keys("Riga")

            # Select Shipping method A
            shipping_method_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='shipping_method_id'][value='67ca982ef38a654a7c2c1a69']"))
            )
            shipping_method_radio.click()

            # Select PayPal payment method
            payment_method_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='payment_method_id'][value='67ca982ef38a654a7c2c1a6a']"))
            )
            payment_method_radio.click()

            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button.button.is-primary"))
            )
            next_button.click()

        except:
            self.fail("Could not fill customer details or select shipping/payment methods.")

        #Step 2 Shipping
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-button.button.is-primary"))
            )
            place_order_button.click()
        except:
            self.fail("Could not click 'Place Order' button.")

        # Verify success message
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[@class='checkout-success-title' and contains(text(), 'Thanks for your order!')]"))
            )
            self.assertIn("Thanks for your order!", success_message.text)
        except:
            self.fail("Success message not found or incorrect.")

if __name__ == "__main__":
    unittest.main()