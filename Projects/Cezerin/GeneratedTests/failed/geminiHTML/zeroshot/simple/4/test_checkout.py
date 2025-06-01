import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Navigate to Product A page
        try:
            product_a_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except Exception as e:
            self.fail(f"Could not find or click on Product A link: {e}")

        # 2. Add Product A to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-success') and text()='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Add to cart' button: {e}")

        # 3. Click on the cart button
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']/img[@alt='cart']"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click the cart button: {e}")

        # 4. Go to checkout
        try:
            go_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'is-primary') and contains(@href, '/checkout')]"))
            )
            go_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Could not find or click 'Go to checkout' button: {e}")

        # 5. Fill customer details
        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
            email_field.send_keys("mail@mail.com")

            mobile_field = wait.until(
                EC.presence_of_element_located((By.ID, "customer.mobile"))
            )
            mobile_field.send_keys("12345678")

            state_field = wait.until(
                EC.presence_of_element_located((By.ID, "shipping_address.state"))
            )
            state_field.send_keys("Riga")

            city_field = wait.until(
                EC.presence_of_element_located((By.ID, "shipping_address.city"))
            )
            city_field.send_keys("Riga")

            # Select shipping method
            shipping_method = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='shipping_method_id' and @value='67ca982ef38a654a7c2c1a69']"))
            )
            shipping_method.click()

            # Select payment method
            payment_method = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='payment_method_id' and @value='67ca982ef38a654a7c2c1a6a']"))
            )
            payment_method.click()

            next_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-primary') and text()='Next']"))
            )
            next_button.click()

        except Exception as e:
            self.fail(f"Could not fill customer details or proceed to next step: {e}")

        # 6. Fill shipping details
        try:
            place_order_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-primary') and text()='Place Order']"))
            )
            place_order_button.click()
        except Exception as e:
            self.fail(f"Could not place the order: {e}")

        # 7. Verify success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h1[@class='checkout-success-title' and contains(text(), 'Thanks for your order!')]"))
            )
            self.assertIn("Thanks for your order!", success_message.text)
        except Exception as e:
            self.fail(f"Could not verify success message: {e}")

if __name__ == "__main__":
    unittest.main()