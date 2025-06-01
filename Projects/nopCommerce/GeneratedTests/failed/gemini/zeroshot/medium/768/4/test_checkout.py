from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
```python
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

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

        country_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
        )
        select_country = Select(country_select)
        select_country.select_by_value("124")

        state_province_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId"))
        )
        select_state = Select(state_province_select)
        select_state.select_by_value("0")

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
        shipping_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))
        )
        shipping_method_option.click()

        shipping_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button"))
        )
        shipping_continue_button.click()

        payment_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1"))
        )
        payment_method_option.click()

        payment_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button"))
        )
        payment_continue_button.click()

        # 9. Enter credit card details.
        credit_card_type_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CreditCardType"))
        )
        select_card_type = Select(credit_card_type_select)
        select_card_type.select_by_value("visa")

        cardholder_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardholderName"))
        )
        cardholder_name_input.send_keys("Test User")

        card_number_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardNumber"))
        )
        card_number_input.send_keys("4111111111111111")

        expire_month_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ExpireMonth"))
        )
        select_expire_month = Select(expire_month_select)
        select_expire_month.select_by_value("4")

        expire_year_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ExpireYear"))
        )
        select_expire_year = Select(expire_year_select)
        select_expire_year.select_by_value("2027")

        card_code_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CardCode"))
        )
        card_code_input.send_keys("12