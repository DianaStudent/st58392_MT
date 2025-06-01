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
            store_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Store")))
            store_link.click()
        except:
            self.fail("Store link not found or not clickable")

        # Go to product page
        try:
            product_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
            product_link.click()
        except:
            self.fail("Product link not found or not clickable")

        # Select size
        try:
            size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
            size_button.click()
        except:
            self.fail("Size button not found or not clickable")

        # Add to cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found or not clickable")

        # Go to cart
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']")))
            cart_button.click()
        except:
            self.fail("Cart button not found or not clickable")

        # Go to checkout
        try:
            go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
            go_to_checkout_button.click()
        except:
            try:
                go_to_checkout_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
                go_to_checkout_button.click()
            except:
                self.fail("Go to checkout button not found or not clickable")

        # Fill shipping address
        try:
            first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']")))
            first_name_input.send_keys("user")
            last_name_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-last-name-input']")
            last_name_input.send_keys("test")
            address_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-address-input']")
            address_input.send_keys("street 1")
            postal_code_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-postal-code-input']")
            postal_code_input.send_keys("LV-1021")
            city_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-city-input']")
            city_input.send_keys("Riga")
            country_select = driver.find_element(By.XPATH, "//select[@data-testid='shipping-country-select']")
            country_select.send_keys("Denmark")
            email_input = driver.find_element(By.XPATH, "//input[@data-testid='shipping-email-input']")
            email_input.send_keys("user@test.com")

            submit_address_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-address-button']")))
            submit_address_button.click()

        except:
            self.fail("Shipping address form not found or not fillable")

        # Select delivery option
        try:
            express_shipping_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio']//button[@data-testid='radio-button']")))
            express_shipping_radio.click()

            submit_delivery_option_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
            submit_delivery_option_button.click()
        except:
            self.fail("Delivery option not found or not selectable")

        # Select payment option
        try:
            manual_payment_radio = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@id='headlessui-radio-:rk:']//button[@data-testid='radio-button']")))
            manual_payment_radio.click()

            submit_payment_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-payment-button']")))
            submit_payment_button.click()
        except:
            self.fail("Payment option not found or not selectable")

        # Place order
        try:
            submit_order_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']")))
            submit_order_button.click()
        except:
            self.fail("Place order button not found or not clickable")

        # Verify order success
        try:
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']//h1//span[text()='Your order was placed successfully.']")))
            self.assertEqual("Your order was placed successfully.", success_message.text)
        except:
            self.fail("Order was not placed successfully")

if __name__ == "__main__":
    unittest.main()