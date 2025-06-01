from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Go to store page
        try:
            nav_store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='nav-store-link']")))
            nav_store_link.click()
        except:
            self.fail("Could not find or click the store link.")

        # Go to product page
        try:
            product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
            product_link.click()
        except:
            self.fail("Could not find or click the product link.")

        # Select size
        try:
            size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='L']")))
            size_button.click()
        except:
            self.fail("Could not find or click the size button.")

        # Add to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the add to cart button.")

        # Go to cart
        try:
            nav_cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:'] a[data-testid='nav-cart-link']")))
            nav_cart_link.click()
        except:
            self.fail("Could not find or click the cart link.")

        # Go to checkout
        try:
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button")))
            go_to_checkout_button.click()
        except:
            self.fail("Could not find or click the go to checkout button.")

        # Fill shipping address
        try:
            shipping_first_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
            shipping_first_name_input.send_keys("user")

            shipping_last_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")))
            shipping_last_name_input.send_keys("test")

            shipping_address_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")))
            shipping_address_input.send_keys("street 1")

            shipping_postal_code_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")))
            shipping_postal_code_input.send_keys("LV-1021")

            shipping_city_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")))
            shipping_city_input.send_keys("Riga")

            shipping_country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
            shipping_country_select.send_keys("Denmark")

            shipping_email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")))
            shipping_email_input.send_keys("user@test.com")

            submit_address_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
            submit_address_button.click()
        except:
            self.fail("Could not fill shipping address or submit.")

       # Select delivery option
        try:
            delivery_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']:first-child button[data-testid='radio-button']")))
            delivery_option.click()

            submit_delivery_option_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
            submit_delivery_option_button.click()
        except:
            self.fail("Could not select delivery option or submit.")

        # Select payment option
        try:
            payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='headlessui-radiogroup-:rj:'] span[id='headlessui-radio-:rk:'] button[data-testid='radio-button']")))
            payment_option.click()

            submit_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
            submit_payment_button.click()
        except:
            self.fail("Could not select payment option or submit.")

        # Place order
        try:
            submit_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
            submit_order_button.click()
        except:
            self.fail("Could not find or click the place order button.")

        # Verify order success
        try:
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
            self.assertIn("Your order was placed successfully.", success_message.text)
        except:
            self.fail("Order was not placed successfully.")

if __name__ == "__main__":
    unittest.main()