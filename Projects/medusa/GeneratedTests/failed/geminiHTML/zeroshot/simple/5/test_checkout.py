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

        # Open the menu
        try:
            menu_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
            menu_button.click()
        except:
            self.fail("Menu button not found")

        # Go to the store page
        try:
            store_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='store-link']")))
            store_link.click()
        except:
            self.fail("Store link not found")

        # Click on the first product
        try:
            first_product = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
            first_product.click()
        except:
            self.fail("First product link not found")

       # Select a size
        try:
            size_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='option-button'][text()='L']")))
            size_button.click()
        except:
            self.fail("Size button not found")

        # Add the product to the cart
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # Go to the cart
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='headlessui-popover-button-:Rrmdtt7:']")))
            cart_button.click()
        except:
            self.fail("Cart button not found")

        # Go to checkout
        try:
            go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/dk/cart'] button[data-testid='go-to-cart-button']")))
            go_to_cart_button.click()
        except:
            self.fail("Go to cart button not found")

        # Go to checkout from cart page
        try:
            checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-testid='checkout-button'] button")))
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # Fill in shipping address
        try:
            first_name_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
            first_name_input.send_keys("user")
            last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")
            last_name_input.send_keys("test")
            address_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")
            address_input.send_keys("street 1")
            postal_code_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")
            postal_code_input.send_keys("LV-1021")
            city_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")
            city_input.send_keys("Riga")
            country_select = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
            country_select.send_keys("Denmark")
            email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")
            email_input.send_keys("user@test.com")
        except:
            self.fail("Shipping address fields not found")

        # Submit shipping address
        try:
            submit_address_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
            submit_address_button.click()
        except:
            self.fail("Submit address button not found")

        # Continue to delivery (select express shipping)
        try:
            express_shipping = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio'][.//*[text()='Express Shipping']]//button[@data-testid='radio-button']")))
            express_shipping.click()
        except:
            self.fail("Express Shipping option not found")

        # Submit delivery option
        try:
            submit_delivery_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
            submit_delivery_button.click()
        except:
            self.fail("Submit delivery option button not found")

        # Continue to payment
        try:
            submit_payment_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
            submit_payment_button.click()
        except:
            self.fail("Submit payment button not found")

        # Place order
        try:
            place_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
            place_order_button.click()
        except:
            self.fail("Place order button not found")

        # Verify order success message
        try:
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
            self.assertIn("Your order was placed successfully", success_message.text)
        except:
            self.fail("Order success message not found")

if __name__ == "__main__":
    unittest.main()