from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Click on the "Search" link
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Search for product (e.g. "book")
        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.clear()
        search_box.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-button")
        search_button.click()

        # Step 3: Add the first item to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Step 4: Open the shopping cart via success notification popup
        cart_popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bar-notification.success a")))
        cart_popup.click()

        # Step 5: Accept terms of service and click the "Checkout" button
        terms_of_service = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 7: Fill in the billing address
        wait.until(EC.presence_of_element_located((By.ID, "opc-billing")))
        billing_info = {
            "BillingNewAddress.FirstName": "Test",
            "BillingNewAddress.LastName": "User",
            "BillingNewAddress.Email": "random_email",
            "BillingNewAddress.City": "Riga",
            "BillingNewAddress.Address1": "Street 1",
            "BillingNewAddress.ZipPostalCode": "LV-1234",
            "BillingNewAddress.PhoneNumber": "12345678"
        }

        for field_id, value in billing_info.items():
            field = driver.find_element(By.ID, field_id)
            field.clear()
            field.send_keys(value)

        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.send_keys("Latvia")

        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

        # Step 8: Select shipping and payment methods
        wait.until(EC.presence_of_element_located((By.ID, "opc-shipping_method")))
        shipping_option = driver.find_element(By.CSS_SELECTOR, "#shippingoption_1")
        shipping_option.click()
        shipping_continue = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        shipping_continue.click()

        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_method")))
        payment_method = driver.find_element(By.CSS_SELECTOR, "#paymentmethod_1")
        payment_method.click()
        payment_continue = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue.click()

        # Step 9: Enter credit card details
        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_info")))
        card_info = {
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "CardCode": "123"
        }

        for field_id, value in card_info.items():
            field = driver.find_element(By.ID, field_id)
            field.clear()
            field.send_keys(value)

        driver.find_element(By.ID, "CreditCardType").send_keys("Visa")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")

        card_continue = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        card_continue.click()

        # Step 10: Confirm the order
        wait.until(EC.presence_of_element_located((By.ID, "opc-confirm_order")))
        confirm_order_button = driver.find_element(By.CSS_SELECTOR, ".confirm-order-next-step-button")
        confirm_order_button.click()

        # Step 11: Validate confirmation message
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed .title strong")))
        self.assertIn("Your order has been successfully processed!", success_message.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()