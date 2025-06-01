import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Category A page
        category_a = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Category A")))
        category_a.click()

        # Open Product A page
        product_a = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Product A")))
        product_a.click()

        # Click "Add to cart" button
        add_to_cart_btn = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Add to cart"]')))
        add_to_cart_btn.click()

        # Click on the cart button
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart-button")))
        cart_button.click()

        # Click "GO TO CHECKOUT" button
        go_to_checkout = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))
        go_to_checkout.click()

        # Fill in the required checkout details
        email_field = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("mail@mail.com")

        mobile_field = driver.find_element(By.ID, "customer.mobile")
        mobile_field.send_keys("12345678")

        state_province_field = driver.find_element(By.ID, "shipping_address.state")
        state_province_field.send_keys("Riga")

        city_field = driver.find_element(By.ID, "shipping_address.city")
        city_field.send_keys("Riga")

        # Select shipping method
        shipping_method = driver.find_element(By.NAME, "shipping_method_id")
        shipping_method.click()

        # Select payment method
        payment_method = driver.find_element(By.NAME, "payment_method_id")
        payment_method.click()

        # Click "NEXT" button
        next_button = driver.find_element(By.XPATH, '//button[text()="Next"]')
        next_button.click()

        # Click "PLACE ORDER" button
        place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="Place Order"]')))
        place_order_button.click()

        # Verify success message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "Thanks for your order!")]')))
        self.assertIn("Thanks for your order!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()