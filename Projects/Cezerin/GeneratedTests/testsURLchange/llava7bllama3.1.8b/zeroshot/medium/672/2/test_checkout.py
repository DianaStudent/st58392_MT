import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000/')

    def test_checkout_process(self):
        # Click on product category
        product_category_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Category A']")))
        product_category_link.click()

        # Select the first product
        first_product_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "(//a[@href='/product/1'])[1]")))
        first_product_link.click()

        # Click the "Add to cart" button
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']")))
        add_to_cart_button.click()

        # Open the shopping bag
        cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button")))
        cart_button.click()
        WebDriverWait(self.driver, 20).until(EC.text_to_be_present_in_element_value((By.XPATH, "//div[@class='mini-cart']//button"), "GO TO CHECKOUT"))

        # Click the "GO TO CHECKOUT" button
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='mini-cart']//button[text()='GO TO CHECKOUT']")))
        go_to_checkout_button.click()

        # Fill required checkout fields
        email_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "email")))
        email_input.send_keys("test@example.com")
        
        phone_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "phone")))
        phone_input.send_keys("1234567890")
        
        shipping_address_input = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "shipping-address")))
        shipping_address_input.send_keys("Test Address")

        # Select a shipping and payment method
        shipping_method_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/shipping-method']")))
        shipping_method_link.click()
        
        payment_method_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/payment-method']")))
        payment_method_link.click()

        # Click "Next" and then "Place Order"
        next_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Next']")))
        next_button.click()
        
        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Confirm that the success page contains the message: "Thanks for your order!"
        thanks_for_your_order_text = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='success-message'][text()='Thanks for your order!']")))
        self.assertTrue(thanks_for_your_order_text.text == "Thanks for your order!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()