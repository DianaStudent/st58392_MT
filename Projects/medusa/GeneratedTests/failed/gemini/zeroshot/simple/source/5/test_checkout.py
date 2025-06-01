from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost:8000/dk")
        self.driver.implicitly_wait(10)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Open the store page
        try:
            store_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Medusa Store"))
            )
            store_link.click()
        except TimeoutException:
            self.fail("Store link not found or not clickable")

        # Click on the first product "Medusa Sweatshirt"
        try:
            product_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Medusa Sweatshirt"))
            )
            product_link.click()
        except TimeoutException:
            self.fail("Product link not found or not clickable")

        # Select size "L"
        try:
            size_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='L']"))
            )
            size_button.click()
        except TimeoutException:
            self.fail("Size button not found or not clickable")

        # Add the product to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to cart']"))
            )
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Add to cart button not found or not clickable")

        # Click on the cart button
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@data-testid='nav-cart-link']"))
            )
            cart_button.click()
        except TimeoutException:
            self.fail("Cart button not found or not clickable")

        # Click on the "Go to checkout" button
        try:
            go_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='go-to-checkout-button']"))
            )
            go_to_checkout_button.click()
        except TimeoutException:
            self.fail("Go to checkout button not found or not clickable")

        # Fill in the shipping address form
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@data-testid='shipping-first-name-input']"))
            )
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

            submit_address_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-address-button']")
            submit_address_button.click()

        except TimeoutException:
            self.fail("Shipping address form not found or could not be filled")

        # Select delivery option
        try:
            express_shipping_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='delivery-option-radio'][1]//button[@data-testid='radio-button']"))
            )
            express_shipping_radio.click()

            submit_delivery_option_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-delivery-option-button']")
            submit_delivery_option_button.click()

        except TimeoutException:
            self.fail("Delivery options not found or could not be selected")

        # Select payment option
        try:
            manual_payment_radio = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='radio-button']"))
            )
            manual_payment_radio.click()

            submit_payment_button = driver.find_element(By.XPATH, "//button[@data-testid='submit-payment-button']")
            submit_payment_button.click()

        except TimeoutException:
            self.fail("Payment options not found or could not be selected")

        # Place the order
        try:
            submit_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='submit-order-button']"))
            )
            submit_order_button.click()
        except TimeoutException:
            self.fail("Submit order button not found or not clickable")

        # Verify order confirmation
        try:
            order_confirmation_text = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h1/span[text()='Your order was placed successfully.']"))
            ).text
            self.assertEqual(order_confirmation_text, "Your order was placed successfully.")
        except TimeoutException:
            self.fail("Order confirmation text not found")


if __name__ == "__main__":
    unittest.main()