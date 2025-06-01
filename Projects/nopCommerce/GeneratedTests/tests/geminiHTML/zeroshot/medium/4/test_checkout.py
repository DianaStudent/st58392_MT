import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import random

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
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Search" link and search for a product (e.g. "book").
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.send_keys("book")

        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        shopping_cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        shopping_cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button.
        terms_of_service_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill in the billing address.
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        last_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName")))
        email_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Email")))
        country_select = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        state_select = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
        city_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_City")))
        address1_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1")))
        zip_postal_code_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode")))
        phone_number_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys(f"user_{random.randint(10000000, 99999999)}@test.com")
        country_select.send_keys("Latvia")
        state_select.send_keys("Other")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_postal_code_input.send_keys("LV-1234")
        phone_number_input.send_keys("12345678")

        billing_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button")))
        billing_continue_button.click()

        # 8. Select shipping and payment methods.
        shipping_method_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_method_option.click()

        shipping_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button")))
        shipping_continue_button.click()

        payment_method_option = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
        payment_method_option.click()

        payment_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button")))
        payment_continue_button.click()

        # 9. Enter credit card details.
        credit_card_type_select = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        cardholder_name_input = wait.until(EC.presence_of_element_located((By.ID, "CardholderName")))
        card_number_input = wait.until(EC.presence_of_element_located((By.ID, "CardNumber")))
        expire_month_select = wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
        expire_year_select = wait.until(EC.presence_of_element_located((By.ID, "ExpireYear")))
        card_code_input = wait.until(EC.presence_of_element_located((By.ID, "CardCode")))

        credit_card_type_select.send_keys("visa")
        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("4111111111111111")
        expire_month_select.send_keys("4")
        expire_year_select.send_keys("2027")
        card_code_input.send_keys("123")

        payment_info_continue_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_continue_button.click()

        # 10. Confirm the order.
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # 11. Validate that the confirmation message or success section is visible.
        order_completed_title = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "order-completed-page")))
        if not order_completed_title:
            self.fail("Order completion message is not visible.")

        order_completed_text = driver.find_element(By.CLASS_NAME, "order-completed-page").text
        if not order_completed_text:
            self.fail("Order completion message is empty.")

        self.assertTrue("Your order has been successfully processed!" in order_completed_text)

if __name__ == "__main__":
    unittest.main()