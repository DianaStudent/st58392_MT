from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # 1. Open the home page. (Done in setUp)

        # 2. Click on the "Search" link and search for a product (e.g. "book").
        search_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = self.wait.until(EC.element_to_be_clickable((By.ID, "small-searchterms")))
        search_input.send_keys("book")

        search_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        shopping_cart_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        shopping_cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button.
        try:
            terms_of_service_checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
            terms_of_service_checkbox.click()
        except:
            self.fail("Terms of service checkbox not found")

        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # 6. Choose "Checkout as Guest".
        try:
            checkout_as_guest_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
            checkout_as_guest_button.click()
        except:
            self.fail("Checkout as Guest button not found")

        # 7. Fill in the billing address.
        first_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName")))
        last_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_LastName")))
        email_input = self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Email")))
        country_select = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        state_select = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
        city_input = self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_City")))
        address1_input = self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_Address1")))
        zip_postal_code_input = self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_ZipPostalCode")))
        phone_number_input = self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_PhoneNumber")))

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys(f"user_{random.randint(100000, 999999)}@test.com")
        # Select Latvia
        country_select.send_keys("United States of America")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_postal_code_input.send_keys("LV-1234")
        phone_number_input.send_keys("12345678")

        billing_continue_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new-address-next-step-button")))
        billing_continue_button.click()

        # 8. Select shipping and payment methods.
        shipping_method_next_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button")))
        shipping_method_next_button.click()

        payment_method_next_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button")))
        payment_method_next_button.click()

        # 9. Enter credit card details.
        cardholder_name_input = self.wait.until(EC.element_to_be_clickable((By.ID, "CardholderName")))
        card_number_input = self.wait.until(EC.element_to_be_clickable((By.ID, "CardNumber")))
        expire_month_select = self.wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth")))
        expire_year_select = self.wait.until(EC.presence_of_element_located((By.ID, "ExpireYear")))
        card_code_input = self.wait.until(EC.element_to_be_clickable((By.ID, "CardCode")))

        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("4111111111111111")
        expire_month_select.send_keys("4")
        expire_year_select.send_keys("2027")
        card_code_input.send_keys("123")

        payment_info_next_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_next_button.click()

        # 10. Confirm the order.
        confirm_order_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # 11. Validate that the confirmation message or success section is visible.
        try:
            order_completed_title = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='title']/strong[text()='Your order has been successfully processed!']")))
            self.assertTrue(order_completed_title.is_displayed())
        except:
            self.fail("Order completion message not found")

if __name__ == "__main__":
    unittest.main()