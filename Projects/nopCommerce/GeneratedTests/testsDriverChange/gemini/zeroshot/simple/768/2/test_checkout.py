```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        # 1. Search for a product
        try:
            search_input = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "small-searchterms"))
            )
            search_input.send_keys("book")
            search_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
            )
            search_button.click()
        except Exception as e:
            self.fail(f"Search failed: {e}")

        # 2. Add the first product to the cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart failed: {e}")
        
        # 3. Click "shopping cart" from the success popup
        try:
            shopping_cart_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
            )
            shopping_cart_link.click()
        except Exception as e:
            self.fail(f"Could not find shopping cart link: {e}")

        # 4. Agree to terms of service
        try:
            terms_of_service_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "termsofservice"))
            )
            terms_of_service_checkbox.click()
        except Exception as e:
            self.fail(f"Could not agree to terms of service: {e}")
            
        # 5. Click Checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Checkout failed: {e}")

        # 6. Checkout as Guest
        try:
            guest_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
            )
            guest_checkout_button.click()
        except Exception as e:
            self.fail(f"Guest checkout failed: {e}")

        # 7. Fill in billing form
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
            )
            first_name_input.send_keys("Test")

            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
            )
            last_name_input.send_keys("User")

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
            )
            email_input.send_keys("random_email")

            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
            )
            country_select.send_keys("Latvia")

            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
            )
            state_select.send_keys("Other")

            city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
            )
            city_input.send_keys("Riga")

            address1_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
            )
            address1_input.send_keys("Street 1")

            zip_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
            )
            zip_input.send_keys("LV-1234")

            phone_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
            )
            phone_input.send_keys("12345678")
        except Exception as e:
            self.fail(f"Billing form filling failed: {e}")

        # 8. Continue to shipping method
        try:
            billing_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
            )
            billing_continue_button.click()
        except Exception as e:
            self.fail(f"Continue to shipping method failed: {e}")

        # 9. Select shipping method
        try:
            shipping_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "shippingoption_1"))
            )
            shipping_option.click()
        except Exception as e:
            self.fail(f"Shipping method selection failed: {e}")

        # 10. Continue to payment method
        try:
            shipping_method_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
            )
            shipping_method_continue_button.click()
        except Exception as e:
            self.fail(f"Continue to payment method failed: {e}")

        # 11. Select payment method
        try:
            payment_method_option = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
            )
            payment_method_option.click()
        except Exception as e:
            self.fail(f"Payment method selection failed: {e}")

        # 12. Continue to payment info
        try:
            payment_method_continue_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
            )
            payment_method_continue_button.click()
        except Exception as e:
            self.fail(f"Continue to payment info failed: {e}")

        # 13. Fill in payment info
        try:
            credit_card_type = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CreditCardType"))
            )
            credit_card_type.send_keys("visa")

            cardholder_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardholderName"))
            )
            cardholder_name.send_keys("Test User")

            card_number = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "CardNumber"))
            )
            card_number.send_keys("4111111111111111")

            expire_month = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "ExpireMonth"))