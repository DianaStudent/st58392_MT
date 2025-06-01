import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_shopping_cart(self):
        # Navigate to the shopping cart page
        self.driver.get("https://example.com/shopping-cart")

        # Add a product to the cart (assuming there's an "ADD TO CART" button)
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart']"))
        )
        add_to_cart_button.click()

        # Click on the cart button to open the cart
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//span[@class='cart-icon']"))
        )
        cart_button.click()

        # Wait for the "GO TO CHECKOUT" button to appear
        go_to_checkout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='go-to-checkout']"))
        )

        # Click on the "GO TO CHECKOUT" button
        go_to_checkout_button.click()

        # Fill in the required checkout fields
        email_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='email']"))
        )
        email_field.send_keys("test@example.com")

        phone_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='phone']"))
        )
        phone_field.send_keys("(555) 123-4567")

        shipping_address_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//textarea[@id='shipping-address']"))
        )
        shipping_address_field.send_keys("123 Main St, Anytown USA")

        # Assuming there's a dropdown for Shipping
        shipping_selector = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//select[@id='shipping-method']"))
        )

        # Assuming the first option is selected by default
        if len(shipping_selector.find_elements(By.TAG_NAME, "option")) > 1:
            shipping_selector.find_element(By.TAG_NAME, "option").click()

        payment_method = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//input[@id='payment-method']"))
        )
        payment_method.send_keys("PayPal")

        # Place the order
        place_order_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@id='place-order']"))
        )
        place_order_button.click()

        # Confirm that the final success page contains the text "Thanks for your order!"
        self.assertEqual("Thanks for your order!", WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[@id='success-message']"))
        ).text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()