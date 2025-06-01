from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Assume 'http://max/' is the base URL for the home page

    def test_checkout_as_guest(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on "Search" link
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        if not search_link.text:
            self.fail("Missing Search link on the page")
        search_link.click()

        # Step 2: Search for "book"
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        if not search_input.get_attribute('type') or not search_button.text:
            self.fail("Missing search input or button on the page")
        search_input.send_keys("book")
        search_button.click()

        # Step 3: Add first item to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        if not add_to_cart_button.text:
            self.fail("Missing Add to Cart button on the page")
        add_to_cart_button.click()

        # Step 4: Open the shopping cart via the success notification popup
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        if not cart_link.text:
            self.fail("Success notification or Shopping cart link missing")
        cart_link.click()

        # Step 5: Accept terms of service and click "Checkout" button
        terms_of_service = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        checkout_button = driver.find_element(By.ID, "checkout")
        if not checkout_button.get_attribute('value') or not terms_of_service.get_attribute('type'):
            self.fail("Checkout button or terms of service checkbox is missing")
        terms_of_service.click()
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        if not checkout_as_guest_button.text:
            self.fail("Missing Checkout as Guest button on the page")
        checkout_as_guest_button.click()

        # Step 7: Fill in the billing address
        wait.until(EC.presence_of_element_located((By.ID, "opc-billing")))
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        driver.find_element(By.NAME, "save").click()

        # Step 8: Select shipping method
        shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        if not shipping_option.get_attribute('value'):
            self.fail("Shipping option is missing")
        shipping_option.click()
        shipping_continue_button = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button")
        if not shipping_continue_button.text:
            self.fail("Shipping continue button is missing")
        shipping_continue_button.click()

        # Step 9: Select payment method
        payment_method_option = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
        if not payment_method_option.get_attribute('value'):
            self.fail("Payment method option is missing")
        payment_method_option.click()
        payment_continue_button = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button")
        if not payment_continue_button.text:
            self.fail("Payment continue button is missing")
        payment_continue_button.click()

        # Step 10: Enter payment information
        wait.until(EC.presence_of_element_located((By.ID, "co-payment-info-form")))
        driver.find_element(By.ID, "CreditCardType").send_keys("visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        payment_info_continue_button = driver.find_element(By.CLASS_NAME, "payment-info-next-step-button")
        if not payment_info_continue_button.text:
            self.fail("Payment info continue button is missing")
        payment_info_continue_button.click()

        # Step 11: Confirm the order
        confirm_order_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "confirm-order-next-step-button")))
        if not confirm_order_button.text:
            self.fail("Confirm order button is missing")
        confirm_order_button.click()

        # Validate the confirmation message or success section
        confirmation_message = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "page-title")))
        if "Thank you" not in confirmation_message.text:
            self.fail("Order confirmation message is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()