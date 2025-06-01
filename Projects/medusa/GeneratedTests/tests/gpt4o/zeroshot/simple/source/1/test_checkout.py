from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8000/dk")

    def test_checkout_process(self):
        driver = self.driver
        
        # Wait and click on the store link
        store_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-store-link']"))
        )
        store_link.click()

        # Click on the first product
        product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "ul[data-testid='products-list'] a"))
        )
        product.click()

        # Select size and click 'Add to cart'
        size_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='option-button']"))
        )
        size_button.click()

        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='add-product-button']"))
        )
        add_to_cart_button.click()

        # Go to cart
        cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='nav-cart-link']"))
        )
        cart_link.click()

        # Go to checkout
        go_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='go-to-cart-button']"))
        )
        go_to_checkout_button.click()

        # Fill in checkout form
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[data-testid='shipping-email-input']"))
        )
        email_input.send_keys("user@test.com")

        first_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-first-name-input']")
        first_name_input.send_keys("User")

        last_name_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-last-name-input']")
        last_name_input.send_keys("Test")

        address_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-address-input']")
        address_input.send_keys("Street 1")

        postal_code_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-postal-code-input']")
        postal_code_input.send_keys("LV-1021")

        city_input = driver.find_element(By.CSS_SELECTOR, "input[data-testid='shipping-city-input']")
        city_input.send_keys("Riga")

        country_select = driver.find_element(By.CSS_SELECTOR, "select[data-testid='shipping-country-select']")
        country_select.send_keys("Denmark")

        # Submit the address form
        submit_address_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-address-button']")
        submit_address_button.click()

        # Select delivery option
        delivery_option_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "span[data-testid='delivery-option-radio'] button"))
        )
        delivery_option_radio.click()

        continue_to_payment_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-delivery-option-button']")
        continue_to_payment_button.click()

        # Select payment option and proceed
        payment_radio_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#headlessui-radio-:rk: button"))
        )
        payment_radio_button.click()

        continue_to_review_button = driver.find_element(By.CSS_SELECTOR, "button[data-testid='submit-payment-button']")
        continue_to_review_button.click()

        # Finalize order
        place_order_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button[data-testid='submit-order-button']"))
        )
        place_order_button.click()

        # Verify order success
        success_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//*[text()='Your order was placed successfully.']"))
        )
        if not success_message:
            self.fail("Order was not successfully placed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()