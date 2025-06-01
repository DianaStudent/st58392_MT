from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UserCheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_user_checkout(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page and click on "Search"
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Search for a product (e.g. "book")
        search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#q")))
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Step 3: Add the first search result to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Step 4: Open the shopping cart via the success notification popup
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Step 5: Accept terms of service
        terms_of_service_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()

        # Step 6: Click the "Checkout" button
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Step 7: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 8: Fill in the billing address
        self.fill_billing_address(wait)

        # Step 9: Select shipping method
        shipping_method_next_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.shipping-method-next-step-button")))
        shipping_method_next_button.click()

        # Step 10: Select payment method
        payment_method_next_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.payment-method-next-step-button")))
        payment_method_next_button.click()

        # Step 11: Enter credit card details
        self.enter_payment_info(wait)

        # Step 12: Confirm the order
        confirm_order_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.confirm-order-next-step-button")))
        confirm_order_button.click()

        # Step 13: Validate confirmation message
        confirmation_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.order-completed-page div.title strong")))
        self.assertTrue("successfully processed" in confirmation_message.text)

    def fill_billing_address(self, wait):
        # Fill in the billing address form
        first_name = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        last_name = driver.find_element(By.ID, "BillingNewAddress_LastName")
        email = driver.find_element(By.ID, "BillingNewAddress_Email")
        country = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        city = driver.find_element(By.ID, "BillingNewAddress_City")
        address = driver.find_element(By.ID, "BillingNewAddress_Address1")
        zip_code = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        phone_number = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")

        first_name.send_keys("Test")
        last_name.send_keys("User")
        email.send_keys("random_email@test.com")
        country.send_keys("Latvia")
        city.send_keys("Riga")
        address.send_keys("Street 1")
        zip_code.send_keys("LV-1234")
        phone_number.send_keys("12345678")

        continue_button = driver.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button")
        continue_button.click()

    def enter_payment_info(self, wait):
        # Enter payment information
        card_type = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        cardholder_name = driver.find_element(By.ID, "CardholderName")
        card_number = driver.find_element(By.ID, "CardNumber")
        expire_month = driver.find_element(By.ID, "ExpireMonth")
        expire_year = driver.find_element(By.ID, "ExpireYear")
        card_code = driver.find_element(By.ID, "CardCode")

        card_type.send_keys("visa")
        cardholder_name.send_keys("Test User")
        card_number.send_keys("4111111111111111")
        expire_month.send_keys("04")
        expire_year.send_keys("2027")
        card_code.send_keys("123")

        payment_info_next_button = driver.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button")
        payment_info_next_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()