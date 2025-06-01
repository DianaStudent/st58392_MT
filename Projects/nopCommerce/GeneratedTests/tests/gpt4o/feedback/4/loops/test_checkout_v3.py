import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_checkout_process(self):
        # Navigate to Search Page
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Perform Search
        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book" + Keys.RETURN)

        # Add first product to cart
        add_to_cart_button = self.wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button"))
        )[0]
        add_to_cart_button.click()

        # Go to shopping cart from success notification
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart"))).click()

        # Agree to terms and proceed to checkout
        terms_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Checkout as guest
        checkout_as_guest_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Fill out billing form
        self.wait.until(EC.presence_of_element_located((By.ID, "opc-billing")))
        
        first_name = self.driver.find_element(By.ID, "BillingNewAddress_FirstName")
        last_name = self.driver.find_element(By.ID, "BillingNewAddress_LastName")
        email = self.driver.find_element(By.ID, "BillingNewAddress_Email")
        country = self.driver.find_element(By.ID, "BillingNewAddress_CountryId")
        state = self.driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        city = self.driver.find_element(By.ID, "BillingNewAddress_City")
        address1 = self.driver.find_element(By.ID, "BillingNewAddress_Address1")
        zip_code = self.driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        phone = self.driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")

        first_name.send_keys("Test")
        last_name.send_keys("User")
        email.send_keys("random_email@test.com")
        country.send_keys("Latvia")
        state.send_keys("Other")
        city.send_keys("Riga")
        address1.send_keys("Street 1")
        zip_code.send_keys("LV-1234")
        phone.send_keys("12345678")

        # Continue to shipping method
        billing_continue_button = self.driver.find_element(By.CSS_SELECTOR, "#billing-buttons-container .new-address-next-step-button")
        billing_continue_button.click()

        # Select shipping method
        self.wait.until(EC.presence_of_element_located((By.ID, "opc-shipping_method")))
        shipping_option = self.driver.find_element(By.CSS_SELECTOR, "#shippingoption_1")
        shipping_option.click()
        shipping_continue_button = self.driver.find_element(By.CSS_SELECTOR, "#shipping-method-buttons-container .shipping-method-next-step-button")
        shipping_continue_button.click()

        # Select payment method
        self.wait.until(EC.presence_of_element_located((By.ID, "opc-payment_method")))
        payment_method = self.driver.find_element(By.CSS_SELECTOR, "#paymentmethod_1")
        payment_method.click()
        payment_continue_button = self.driver.find_element(By.CSS_SELECTOR, "#payment-method-buttons-container .payment-method-next-step-button")
        payment_continue_button.click()

        # Fill payment information
        self.wait.until(EC.presence_of_element_located((By.ID, "opc-payment_info")))
        credit_card_type = self.driver.find_element(By.ID, "CreditCardType")
        cardholder_name = self.driver.find_element(By.ID, "CardholderName")
        card_number = self.driver.find_element(By.ID, "CardNumber")
        expire_month = self.driver.find_element(By.ID, "ExpireMonth")
        expire_year = self.driver.find_element(By.ID, "ExpireYear")
        card_code = self.driver.find_element(By.ID, "CardCode")

        credit_card_type.send_keys("Visa")
        cardholder_name.send_keys("Test User")
        card_number.send_keys("4111111111111111")
        expire_month.send_keys("04")
        expire_year.send_keys("2027")
        card_code.send_keys("123")
        
        payment_info_continue_button = self.driver.find_element(By.CSS_SELECTOR, "#payment-info-buttons-container .payment-info-next-step-button")
        payment_info_continue_button.click()

        # Confirm order
        self.wait.until(EC.presence_of_element_located((By.ID, "opc-confirm_order")))
        confirm_order_button = self.driver.find_element(By.CSS_SELECTOR, "#confirm-order-buttons-container .confirm-order-next-step-button")
        confirm_order_button.click()

        # Verify order completion
        thank_you_text = self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
        self.assertEqual(thank_you_text, "Thank you", "Order was not completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()