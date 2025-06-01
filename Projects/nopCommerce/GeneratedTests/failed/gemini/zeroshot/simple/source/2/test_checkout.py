from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Search for a product
        search_box = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_box.send_keys("book")
        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
        )
        search_button.click()

        # Add the first product to the cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Go to the shopping cart
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@id='bar-notification']//a[contains(@href, '/cart')]"))
        )
        shopping_cart_link.click()

        # Agree to terms of service
        terms_of_service = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_of_service.click()

        # Click Checkout
        checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "checkout"))
        )
        checkout_button.click()

        # Checkout as Guest
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Billing Form
        first_name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
        )
        first_name.send_keys("Test")

        last_name = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))
        )
        last_name.send_keys("User")

        email = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))
        )
        email.send_keys("random_email")

        country = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
        )
        country.send_keys("Latvia")

        state = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
        )
        state.send_keys("Other")

        city = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
        )
        city.send_keys("Riga")

        address1 = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
        )
        address1.send_keys("Street 1")

        zip_code = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
        )
        zip_code.send_keys("LV-1234")

        phone_number = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
        )
        phone_number.send_keys("12345678")

        billing_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
        )
        billing_continue_button.click()

        # Shipping Method
        shipping_method = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "shippingoption_1"))
        )
        shipping_method.click()

        shipping_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
        )
        shipping_continue_button.click()

        # Payment Method
        payment_method = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "paymentmethod_1"))
        )
        payment_method.click()

        payment_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
        )
        payment_continue_button.click()

        # Payment Information
        card_type = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CreditCardType"))
        )
        card_type.send_keys("visa")

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
        )
        expire_month.send_keys("4")

        expire_year = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ExpireYear"))
        )
        expire_year.send_keys("2027")

        card_code = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardCode"))
        )
        card_code.send_keys("123")

        payment_info_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button"))
        )
        payment_info_continue_button.click()

        # Confirm Order
        confirm_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
        )
        confirm_button.click()

        # Verify Order Completion
        order_completion_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='title']/strong[contains(text(), 'Your order has been successfully processed!')]"))
        )

        self.assertTrue("Your order has been successfully processed!" in order_completion_message.text)

if __name__ == "__main__":
    unittest.main()