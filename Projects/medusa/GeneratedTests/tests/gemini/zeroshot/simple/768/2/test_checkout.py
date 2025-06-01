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
            nav_menu_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='nav-menu-button']")))
            nav_menu_button.click()
        except:
            self.fail("Could not find or click the navigation menu button.")

        try:
            store_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='store-link']")))
            store_link.click()
        except:
            self.fail("Could not find or click the store link.")

        # Add product to cart
        try:
            product_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='/dk/products/sweatshirt']")))
            product_link.click()
        except:
            self.fail("Could not find or click the product link.")

        # Select size
        try:
            size_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='option-button']")))
            size_button.click()
        except:
            self.fail("Could not find or click the size button.")

        try:
            add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']")))
            add_to_cart_button.click()
        except:
            self.fail("Could not find or click the add to cart button.")

        # Go to cart
        try:
            cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']")))
            cart_button.click()
        except:
            self.fail("Could not find or click the cart button.")

        # Go to checkout
        try:
            go_to_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']")))
            go_to_checkout_button.click()
        except:
            self.fail("Could not find or click the go to checkout button.")

        # Fill shipping address
        try:
            shipping_first_name_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")))
            shipping_first_name_input.send_keys("user")
            shipping_last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")
            shipping_last_name_input.send_keys("test")
            shipping_address_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")
            shipping_address_input.send_keys("street 1")
            shipping_postal_code_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")
            shipping_postal_code_input.send_keys("LV-1021")
            shipping_city_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")
            shipping_city_input.send_keys("Riga")
            shipping_country_select = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
            shipping_country_select.send_keys("Denmark")
            shipping_email_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-email-input']")
            shipping_email_input.send_keys("user@test.com")
        except:
            self.fail("Could not find or fill the shipping address fields.")

        try:
            submit_address_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-address-button']")))
            submit_address_button.click()
        except:
            self.fail("Could not find or click the submit address button.")

        # Select delivery option
        try:
            delivery_option_radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio']")))
            delivery_option_radio.click()
        except:
            self.fail("Could not find or click the delivery option radio.")

        try:
            submit_delivery_option_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")))
            submit_delivery_option_button.click()
        except:
            self.fail("Could not find or click the submit delivery option button.")

        # Select payment method
        try:
            payment_method_radio = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "span[id='headlessui-radio-:rk:']")))
            payment_method_radio.click()
        except:
            self.fail("Could not find or click the payment method radio.")

        try:
            submit_payment_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")))
            submit_payment_button.click()
        except:
            self.fail("Could not find or click the submit payment button.")

        # Place order
        try:
            submit_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-order-button']")))
            submit_order_button.click()
        except:
            self.fail("Could not find or click the submit order button.")

        # Verify order completion
        try:
            order_complete_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']")))
            self.assertIn("Your order was placed successfully.", order_complete_text.text)
        except:
            self.fail("Order was not placed successfully.")

if __name__ == "__main__":
    unittest.main()