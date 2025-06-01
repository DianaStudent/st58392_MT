import unittest
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # 1. Navigate to the "Search" page and look for a product using the query "book".
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")

        search_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()

        # 3. Add the first result to the cart using a product tile button.
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. From the success notification, click the "shopping cart" link.
        shopping_cart_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        shopping_cart_link.click()

        # 5. Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_of_service_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()

        checkout_button = self.wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill out the full billing form.
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name_input.send_keys("Test")

        last_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName")))
        last_name_input.send_keys("User")

        email_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Email")))
        email_input.send_keys(f"user_{random.randint(10000000, 99999999)}@test.com")

        country_select = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_select.send_keys("Latvia")

        state_province_select = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
        state_province_select.send_keys("Other")

        city_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_City")))
        city_input.send_keys("Riga")

        address1_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1")))
        address1_input.send_keys("Street 1")

        zip_postal_code_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode")))
        zip_postal_code_input.send_keys("LV-1234")

        phone_number_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber")))
        phone_number_input.send_keys("12345678")

        billing_continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-address-next-step-button")))
        billing_continue_button.click()

        # 8. Proceed through the following:
        #    - Shipping method step.
        shipping_method_option = self.wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_method_option.click()

        shipping_method_continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button")))
        shipping_method_continue_button.click()

        #    - Payment method step.
        payment_method_option = self.wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method_option.click()

        payment_method_continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button")))
        payment_method_continue_button.click()

        #    - Payment info step (fill in credit card details).
        credit_card_type_select = self.wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        credit_card_type_select.send_keys("visa")

        cardholder_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "CardholderName")))
        cardholder_name_input.send_keys("Test User")

        card_number_input = self.wait.until(EC.presence_of_element_located((By.ID, "CardNumber")))
        card_number_input.send_keys("4111111111111111")

        expire_month_select = self.wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
        expire_month_select.send_keys("04")

        expire_year_select = self.wait.until(EC.presence_of_element_located((By.ID, "ExpireYear")))
        expire_year_select.send_keys("2027")

        card_code_input = self.wait.until(EC.presence_of_element_located((By.ID, "CardCode")))
        card_code_input.send_keys("123")

        payment_info_continue_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_continue_button.click()

        # 9. On the confirm step, click “Confirm” and wait for the success message.
        confirm_order_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # 10. Confirm that the order has been completed.
        thank_you_header = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        if thank_you_header:
            thank_you_text = thank_you_header.text
            if thank_you_text and "Thank you" in thank_you_text:
                print("Order completed successfully!")
            else:
                self.fail("Order completion message 'Thank you' not found.")
        else:
            self.fail("Header element not found.")

if __name__ == "__main__":
    unittest.main()