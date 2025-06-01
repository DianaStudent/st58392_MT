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

        # Navigate to store page
        try:
            nav_menu_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "nav-menu-button")))
            nav_menu_button.click()
            store_link = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "store-link")))
            store_link.click()
        except:
            self.fail("Could not navigate to the store page.")

        # Add product to cart
        try:
            product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
            product_link.click()

            size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button'][text()='L']")))
            size_button.click()

            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "add-product-button")))
            add_to_cart_button.click()
        except:
            self.fail("Could not add product to cart.")

        # Go to cart
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "nav-cart-link")))
            cart_button.click()

            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "go-to-cart-button")))
            go_to_checkout_button.click()
        except:
            self.fail("Could not go to cart.")

        # Fill address form
        try:
            shipping_first_name_input = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "shipping-first-name-input")))
            shipping_first_name_input.send_keys("user")

            shipping_last_name_input = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "shipping-last-name-input")))
            shipping_last_name_input.send_keys("test")

            shipping_address_input = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "shipping-address-input")))
            shipping_address_input.send_keys("street 1")

            shipping_postal_code_input = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "shipping-postal-code-input")))
            shipping_postal_code_input.send_keys("LV-1021")

            shipping_city_input = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "shipping-city-input")))
            shipping_city_input.send_keys("Riga")

            shipping_country_select = wait.until(EC.presence_of_element_located((By.DATA_TEST_ID, "shipping-country-select")))
            shipping_country_select.send_keys("Denmark")

            shipping_email_input = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "shipping-email-input")))
            shipping_email_input.send_keys("user@test.com")

            submit_address_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "submit-address-button")))
            submit_address_button.click()
        except:
            self.fail("Could not fill address form.")

        # Select delivery option
        try:
            delivery_option_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio']//button[@data-testid='radio-button']")))
            delivery_option_radio.click()

            submit_delivery_option_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "submit-delivery-option-button")))
            submit_delivery_option_button.click()
        except:
            self.fail("Could not select delivery option.")

        # Select payment option
        try:
            payment_radio_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='headlessui-radiogroup-:rj:']//button[@data-testid='radio-button']")))
            payment_radio_button.click()

            submit_payment_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "submit-payment-button")))
            submit_payment_button.click()
        except:
            self.fail("Could not select payment option.")

        # Place order
        try:
            submit_order_button = wait.until(EC.element_to_be_clickable((By.DATA_TEST_ID, "submit-order-button")))
            submit_order_button.click()
        except:
            self.fail("Could not place order.")

        # Verify order completion
        try:
            order_complete_text = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[2]"))).text
            self.assertEqual(order_complete_text, "Your order was placed successfully.")
        except:
            self.fail("Order was not placed successfully.")

if __name__ == "__main__":
    unittest.main()