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

        # Go to Category A
        try:
            category_a_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Category A"))
            )
            category_a_link.click()
        except:
            self.fail("Could not find or click 'Category A' link.")

        # Go to Product A
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
                EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'is-success') and contains(text(), 'Add to cart')]"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click 'Add to cart' button.")

        # Click on the cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "cart-button"))
            )
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button.")

        # Click on "Go to checkout" button
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Go to checkout"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Could not find or click 'Go to checkout' button.")

        # Fill customer details form
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

        except:
            self.fail("Could not find or fill customer details fields.")

        # Select payment method
        try:
            payment_method_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='payment-methods']//input[@type='radio']"))
            )
            payment_method_radio.click()
        except:
            self.fail("Could not select payment method.")

        # Click Next button
        try:
            next_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Next')]"))
            )
            next_button.click()
        except:
            self.fail("Could not click 'Next' button.")

        # Place order
        try:
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Place Order')]"))
            )
            place_order_button.click()
        except:
            self.fail("Could not click 'Place Order' button.")

        # Verify success message
        try:
            success_message = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1[contains(@class, 'checkout-success-title') and contains(text(), 'Thanks for your order!')]"))
            )
            self.assertEqual("Thanks for your order!", success_message.text.split('\n')[-1])
        except:
            self.fail("Could not find success message or success message is incorrect.")

if __name__ == "__main__":
    unittest.main()