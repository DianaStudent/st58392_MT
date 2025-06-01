import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 2. Search for a product
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-button")))
        search_button.click()

        # 3. Add to cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. Open shopping cart
        shopping_cart_link = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='bar-notification success']//a[contains(@href, '/cart')]")))
        shopping_cart_link.click()

        # 5. Checkout
        terms_of_service = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service.click()
        checkout_button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

        # 6. Checkout as Guest
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill in billing address
        first_name = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name.send_keys("Test")
        last_name = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName")))
        last_name.send_keys("User")
        email = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Email")))
        email.send_keys("random_email")
        country = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country.send_keys("Latvia")
        state = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
        state.send_keys("Other")
        city = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_City")))
        city.send_keys("Riga")
        address1 = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1")))
        address1.send_keys("Street 1")
        zip_code = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode")))
        zip_code.send_keys("LV-1234")
        phone_number = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber")))
        phone_number.send_keys("12345678")

        billing_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new-address-next-step-button")))
        billing_continue_button.click()

        # 8. Select shipping method
        shipping_method = wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_method.click()
        shipping_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shipping-method-next-step-button")))
        shipping_continue_button.click()

        # Select payment method
        payment_method = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method.click()
        payment_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-method-next-step-button")))
        payment_continue_button.click()

        # 9. Enter credit card details
        card_type = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        card_type.send_keys("visa")
        cardholder_name = wait.until(EC.presence_of_element_located((By.ID, "CardholderName")))
        cardholder_name.send_keys("Test User")
        card_number = wait.until(EC.presence_of_element_located((By.ID, "CardNumber")))
        card_number.send_keys("4111111111111111")
        expire_month = wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
        expire_month.send_keys("4")
        expire_year = wait.until(EC.presence_of_element_located((By.ID, "ExpireYear")))
        expire_year.send_keys("2027")
        card_code = wait.until(EC.presence_of_element_located((By.ID, "CardCode")))
        card_code.send_keys("123")

        payment_info_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_continue_button.click()

        # 10. Confirm order
        confirm_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_button.click()

        # 11. Validate order completion
        order_completed_message = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='section order-completed']//strong")))
        if order_completed_message:
            self.assertIn("Your order has been successfully processed!", order_completed_message.text)
        else:
            self.fail("Order completion message not found.")

if __name__ == "__main__":
    unittest.main()