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

        # Go to store page
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Store"))
            )
            store_link.click()
        except:
            self.fail("Store link not found or not clickable")

        # Go to product page
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']"))
            )
            product_link.click()
        except:
            self.fail("Product link not found or not clickable")

       # Select size
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button' and text()='L']"))
            )
            size_button.click()
        except:
            self.fail("Size button not found or not clickable")

        # Add to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Go to cart
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except:
            self.fail("Cart button not found or not clickable")

        # Go to checkout
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']"))
            )
            go_to_checkout_button.click()
        except:
            self.fail("Go to checkout button not found or not clickable")
        
        # Fill shipping address
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-first-name-input']"))
            )
            first_name_input.clear()
            first_name_input.send_keys("user")

            last_name_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-last-name-input']"))
            )
            last_name_input.clear()
            last_name_input.send_keys("test")

            address_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-address-input']"))
            )
            address_input.clear()
            address_input.send_keys("street 1")

            postal_code_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-postal-code-input']"))
            )
            postal_code_input.clear()
            postal_code_input.send_keys("LV-1021")

            city_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-city-input']"))
            )
            city_input.clear()
            city_input.send_keys("Riga")

            country_select = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select[@data-testid='shipping-country-select']"))
            )
            country_select.click()
            country_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//option[@value='dk']"))
            )
            country_option.click()

            email_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-email-input']"))
            )
            email_input.clear()
            email_input.send_keys("user@test.com")
            
            submit_address_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-address-button']"))
            )
            submit_address_button.click()

        except:
            self.fail("Shipping address form not found or could not be filled")

        # Select delivery option
        try:
            delivery_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio'][1]//button[@data-testid='radio-button']"))
            )
            delivery_option.click()

            submit_delivery_option_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-delivery-option-button']"))
            )
            submit_delivery_option_button.click()

        except:
            self.fail("Delivery option not found or could not be selected")

        # Select payment option
        try:
            payment_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@id='headlessui-radio-:rk:']//button[@data-testid='radio-button']"))
            )
            payment_option.click()

            submit_payment_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-payment-button']"))
            )
            submit_payment_button.click()

        except:
            self.fail("Payment option not found or could not be selected")

        # Place order
        try:
            submit_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']"))
            )
            submit_order_button.click()
        except:
            self.fail("Place order button not found or not clickable")

        # Verify order completion
        try:
            order_complete_text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[2]"))
            ).text
            self.assertEqual(order_complete_text, "Your order was placed successfully.")
        except:
            self.fail("Order completion text not found or incorrect")

if __name__ == "__main__":
    unittest.main()