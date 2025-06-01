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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        # 1. Open the home page.
        self.assertEqual(driver.current_url, "http://max/")

        # 2. Click on the "Search" link and search for a product (e.g. "book").
        search_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_input.send_keys("book")

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
        )
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        shopping_cart_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        shopping_cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button.
        terms_of_service_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_of_service_checkbox.click()

        checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # 7. Fill in the billing address.
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

        country_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
        )
        country_dropdown.send_keys("Latvia")

        state_dropdown = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
        )
        state_dropdown.send_keys("Other")

        city_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))
        )
        city_input.send_keys("Riga")

        address1_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))
        )
        address1_input.send_keys("Street 1")

        zip_postal_code_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))
        )
        zip_postal_code_input.send_keys("LV-1234")

        phone_number_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))
        )
        phone_number_input.send_keys("12345678")

        billing_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button"))
        )
        billing_continue_button.click()

        # 8. Select shipping and payment methods.
        shipping_method = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))
        )
        shipping_method.click()

        shipping_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
        )
        shipping_continue_button.click()

        payment_method = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1"))
        )
        payment_method.click()

        payment_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
        )
        payment_continue_button.click()

        # 9. Enter credit card details.
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

        # 10. Confirm the order.
        confirm_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # 11. Validate that the