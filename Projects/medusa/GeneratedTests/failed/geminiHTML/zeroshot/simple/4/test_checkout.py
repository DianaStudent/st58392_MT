from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Open Menu
        try:
            menu_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']"))
            )
            menu_button.click()
        except:
            self.fail("Menu button not found")

        # Go to Store
        try:
            store_link = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']"))
            )
            store_link.click()
        except:
            self.fail("Store link not found")

        # Click on product
        try:
            product_link = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except:
            self.fail("Product link not found")

        # Select size
        try:
            size_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button' and text()='L']"))
            )
            size_button.click()
        except:
            self.fail("Size button not found")

        # Add to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # Go to cart
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:'] a[data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # Go to checkout
        try:
            go_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] button[data-testid='go-to-cart-button']"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Go to checkout button not found")

        # Fill shipping address
        try:
            shipping_first_name = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']"))
            )
            shipping_first_name.send_keys("user")
            shipping_last_name = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")
            shipping_last_name.send_keys("test")
            shipping_address = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")
            shipping_address.send_keys("street 1")
            shipping_postal_code = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")
            shipping_postal_code.send_keys("LV-1021")
            shipping_city = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")
            shipping_city.send_keys("Riga")
            shipping_country = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
            shipping_country.send_keys("Denmark")
            shipping_email = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")
            shipping_email.send_keys("user@test.com")

            submit_address_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
            submit_address_button.click()

        except:
            self.fail("Shipping address form not found or could not be filled")

        # Select delivery option
        try:
            express_shipping = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio'][1]//button[@data-testid='radio-button']"))
            )
            express_shipping.click()

            submit_delivery_option_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
            submit_delivery_option_button.click()
        except:
            self.fail("Delivery option not found or could not be selected")

        # Select payment option
        try:
            manual_payment = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:'] button[data-testid='radio-button']"))
            )
            manual_payment.click()

            submit_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
            submit_payment_button.click()
        except:
            self.fail("Payment option not found or could not be selected")

        # Place order
        try:
            submit_order_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
            )
            submit_order_button.click()
        except:
            self.fail("Submit order button not found")

        # Verify order success
        try:
            success_message = wait.until(
                EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']"))
            )
            self.assertIn("Your order was placed successfully", success_message.text)
        except:
            self.fail("Order was not placed successfully")

if __name__ == "__main__":
    unittest.main()