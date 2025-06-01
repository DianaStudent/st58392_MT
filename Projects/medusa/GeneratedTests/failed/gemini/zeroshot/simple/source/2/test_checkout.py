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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Go to store page
        try:
            menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
            menu_button.click()
            store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
            store_link.click()
        except:
            self.fail("Could not navigate to store page.")

        # Go to product page
        try:
            product_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
            product_link.click()
        except:
            self.fail("Could not navigate to product page.")

        # Select size and add to cart
        try:
            size_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='option-button']")))
            size_button.click()
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
            add_to_cart_button.click()
        except:
            self.fail("Could not add product to cart.")

        # Go to cart
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']")))
            cart_button.click()
            go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] button[data-testid='go-to-cart-button']")))
            go_to_cart_button.click()
        except:
            self.fail("Could not navigate to cart.")

        # Go to checkout
        try:
            checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button")))
            checkout_button.click()
        except:
            self.fail("Could not navigate to checkout.")

        # Fill shipping address
        try:
            first_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
            first_name_input.send_keys("user")
            last_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")))
            last_name_input.send_keys("test")
            address_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")))
            address_input.send_keys("street 1")
            postal_code_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")))
            postal_code_input.send_keys("LV-1021")
            city_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")))
            city_input.send_keys("Riga")
            country_select = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")))
            country_select.send_keys("Denmark")
            email_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")))
            email_input.send_keys("user@test.com")
            submit_address_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
            submit_address_button.click()
        except:
            self.fail("Could not fill shipping address.")

        # Select delivery option
        try:
            express_shipping_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button[data-testid='radio-button']")))
            express_shipping_button.click()
            submit_delivery_option_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
            submit_delivery_option_button.click()
        except:
            self.fail("Could not select delivery option.")

        # Select payment option
        try:
            manual_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:'] button[data-testid='radio-button']")))
            manual_payment_button.click()
            submit_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
            submit_payment_button.click()
        except:
            self.fail("Could not select payment option.")

        # Place order
        try:
            submit_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
            submit_order_button.click()
        except:
            self.fail("Could not place order.")

        # Verify order success
        try:
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[2]"))).text
            self.assertEqual(success_message, "Your order was placed successfully.")
        except:
            self.fail("Order was not placed successfully.")

if __name__ == "__main__":
    unittest.main()