import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/")
        self.wait = WebDriverWait(self.driver, 20)
        self.actions = ActionChains(self.driver)

    def test_checkout_process(self):
        driver = self.driver
        
        # Click on 'Category A'
        category_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a']")))
        category_a.click()

        # Select 'Product A'
        product_a = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/category-a/product-a']")))
        product_a.click()

        # Click 'Add to cart' button
        add_to_cart_btn = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-addtocart button")))
        add_to_cart_btn.click()

        # Click on the cart button to open mini-cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".cart-button img")))
        cart_button.click()

        # Verify 'GO TO CHECKOUT' button is present
        go_to_checkout = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/checkout']")))
        self.assertIsNotNone(go_to_checkout)

        # Click 'GO TO CHECKOUT' button
        go_to_checkout.click()

        # Fill checkout fields
        email_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        email_field.send_keys("test@example.com")

        mobile_field = self.wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        mobile_field.send_keys("12345678")

        country_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.country")))
        country_field.clear()
        country_field.send_keys("SG")

        state_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        state_field.send_keys("Riga")

        city_field = self.wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        city_field.send_keys("Riga")

        # Select shipping method
        shipping_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='shipping_method_id']")))
        shipping_method.click()

        # Select payment method
        payment_method = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='payment_method_id']")))
        payment_method.click()

        # Click 'Next' button then 'Place Order'
        next_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-button-wrap button")))
        next_button.click()

        place_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[onclick*='Place Order']")))
        place_order_button.click()

        # Confirm success page contains 'Thanks for your order!'
        success_message = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Thanks for your order!']"))
        )
        self.assertIsNotNone(success_message)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()