import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # 1. Navigate to Product A page
        try:
            product_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a/product-a']"))
            )
            product_a_link.click()
        except:
            self.fail("Could not find or click Product A link.")

        # 2. Add Product A to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-success') and contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click 'Add to cart' button.")

        # 3. Click on the cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@class='cart-button']"))
            )
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button.")

        # 4. Click on "Go to checkout" button
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Could not find or click 'Go to checkout' button.")

        # 5. Fill customer details form
        try:
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "customer.email"))
            )
            email_field.send_keys("mail@mail.com")

            mobile_field = driver.find_element(By.ID, "customer.mobile")
            mobile_field.send_keys("12345678")

            state_field = driver.find_element(By.ID, "shipping_address.state")
            state_field.send_keys("Riga")

            city_field = driver.find_element(By.ID, "shipping_address.city")
            city_field.send_keys("Riga")

            shipping_method_radio = driver.find_element(By.XPATH, "//input[@name='shipping_method_id']")
            shipping_method_radio.click()

            payment_method_radio = driver.find_element(By.XPATH, "//input[@name='payment_method_id']")
            payment_method_radio.click()

            next_button = driver.find_element(By.XPATH, "//button[text()='Next']")
            next_button.click()

        except:
            self.fail("Could not fill customer details form.")

        # 6. Fill shipping details form
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']"))
            )
            place_order_button.click()
        except:
            self.fail("Could not find or click 'Place Order' button.")

        # 7. Verify success message
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[@class='checkout-success-title' and contains(text(), 'Thanks for your order!')]"))
            )
            self.assertIn("Thanks for your order!", success_message.text)
        except:
            self.fail("Success message not found or incorrect.")

if __name__ == "__main__":
    unittest.main()