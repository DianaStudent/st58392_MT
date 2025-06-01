import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("data:text/html;charset=utf-8," + html_data['home_page'])

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on Category A
        category_a = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="/category-a"]')))
        category_a.click()

        # Select the first product
        product = wait.until(EC.presence_of_element_located((By.XPATH, '//a[@href="/category-a/product-a"]')))
        product.click()

        # Click "Add to cart"
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Add to cart")]')))
        add_to_cart_button.click()

        # Click cart icon to open shopping bag
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.cart-button')))
        cart_icon.click()

        # Verify "GO TO CHECKOUT" button is present
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Go to checkout")))
        self.assertIsNotNone(go_to_checkout_button, "The 'GO TO CHECKOUT' button is not present!")

        # Click "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill in Checkout fields
        email_input = wait.until(EC.presence_of_element_located((By.ID, "customer.email")))
        self.assertIsNotNone(email_input, "Email input is missing!")
        email_input.send_keys("mail@mail.com")

        mobile_input = wait.until(EC.presence_of_element_located((By.ID, "customer.mobile")))
        self.assertIsNotNone(mobile_input, "Mobile input is missing!")
        mobile_input.send_keys("12345678")

        state_input = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.state")))
        self.assertIsNotNone(state_input, "State input is missing!")
        state_input.send_keys("Riga")

        city_input = wait.until(EC.presence_of_element_located((By.ID, "shipping_address.city")))
        self.assertIsNotNone(city_input, "City input is missing!")
        city_input.send_keys("Riga")

        # Select shipping method
        shipping_method = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="shipping_method_id"]')))
        shipping_method.click()

        # Select payment method
        payment_method = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@name="payment_method_id"]')))
        payment_method.click()

        # Click "Next"
        next_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Next"]')))
        next_button.click()

        # Click "Place Order"
        place_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Place Order"]')))
        place_order_button.click()

        # Confirm success page contains "Thanks for your order!"
        success_message = wait.until(EC.presence_of_element_located(
            (By.XPATH, '//h1[contains(., "Thanks for your order!")]')))
        self.assertTrue("Thanks for your order!" in success_message.text, "Success message not found!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    html_data = {
        "home_page": "...",  # Insert the whole HTML string here
        "category_a_page": "...",
        "product_page": "...",
        "popup": "...",
        "checkout_before_filling": "...",
        "checkout_after_filling": "...",
        "checkout_shipping": "...",
        "checkout_final": "..."
    }
    unittest.main()