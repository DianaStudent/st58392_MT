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
        store_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Store")))
        store_link.click()

        # Click on the product
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/dk/products/sweatshirt']")))
        product_link.click()

        # Select size
        size_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='option-button' and text()='L']")))
        size_button.click()

        # Add to cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='add-product-button' and text()='Add to cart']")))
        add_to_cart_button.click()

        # Go to cart
        cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@data-testid='nav-cart-link']")))
        cart_button.click()

        # Go to checkout
        go_to_checkout_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='go-to-cart-button']")))
        go_to_checkout_button.click()

        # Fill shipping address
        shipping_first_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-first-name-input']")))
        shipping_first_name_input.send_keys("user")

        shipping_last_name_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-last-name-input']")))
        shipping_last_name_input.send_keys("test")

        shipping_address_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-address-input']")))
        shipping_address_input.send_keys("street 1")

        shipping_postal_code_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-postal-code-input']")))
        shipping_postal_code_input.send_keys("LV-1021")

        shipping_city_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-city-input']")))
        shipping_city_input.send_keys("Riga")

        shipping_country_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[@data-testid='shipping-country-select']")))
        shipping_country_select.send_keys("Denmark")

        shipping_email_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@data-testid='shipping-email-input']")))
        shipping_email_input.send_keys("user@test.com")

        submit_address_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-address-button']")))
        submit_address_button.click()

        # Select delivery option
        delivery_option = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@data-testid='delivery-option-radio'][1]//button[@data-testid='radio-button']")))
        delivery_option.click()

        submit_delivery_option_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-delivery-option-button']")))
        submit_delivery_option_button.click()

        # Select payment option
        payment_option = wait.until(EC.presence_of_element_located((By.XPATH, "//span[@id='headlessui-radio-:rk:']//button[@data-testid='radio-button']")))
        payment_option.click()

        submit_payment_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-payment-button']")))
        submit_payment_button.click()

        # Place order
        submit_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@data-testid='submit-order-button']")))
        submit_order_button.click()

        # Verify success message
        success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='order-complete-container']/h1/span[2]")))
        self.assertEqual(success_message.text, "Your order was placed successfully.")

if __name__ == "__main__":
    unittest.main()