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
        wait = WebDriverWait(driver, 20)

        # 1. Navigate to product page (Product A)
        try:
            product_a_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except:
            self.fail("Could not find or click Product A link")

        # 2. Add product to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-success') and text()='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click 'Add to cart' button")
        
        # 3. Click on the cart button (shopping bag)
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button")

        # 4. Wait for and click "Go to checkout" button
        try:
            go_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'is-primary') and contains(text(), 'Go to checkout')]"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Could not find or click 'Go to checkout' button")

        # 5. Fill in customer details
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

        except:
            self.fail("Could not find or fill customer details fields")

        # 6. Select shipping and payment methods and click Next
        try:
            shipping_method_radio = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='shipping_method_id' and @value='67ca982ef38a654a7c2c1a69']"))
            )
            shipping_method_radio.click()

            payment_method_radio = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//input[@name='payment_method_id' and @value='67ca982ef38a654a7c2c1a6a']"))
            )
            payment_method_radio.click()

            next_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-primary') and text()='Next']"))
            )
            next_button.click()
        except:
            self.fail("Could not select shipping/payment methods or click 'Next'")

        # 7. Fill in shipping comments and place order
        try:
            place_order_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-primary') and text()='Place Order']"))
            )
            place_order_button.click()
        except:
            self.fail("Could not find or click 'Place Order' button")

        # 8. Verify success message
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'checkout-success-title') and contains(text(), 'Thanks for your order!')]"))
            )
            self.assertTrue("Thanks for your order!" in success_message.text)
        except:
            self.fail("Success message not found or incorrect")

if __name__ == "__main__":
    unittest.main()