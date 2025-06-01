import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
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
        if not search_box:
            self.fail("Search box not found")
        search_box.send_keys("book")

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button"))
        )
        if not search_button:
            self.fail("Search button not found")
        search_button.click()

        # Add product to cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button"))
        )
        if not add_to_cart_button:
            self.fail("Add to cart button not found")
        add_to_cart_button.click()

        # Go to shopping cart from success popup
        go_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'content')]/a"))
        )
        if not go_to_cart_button:
            self.fail("Go to cart button not found")
        go_to_cart_button.click()

        # Checkout as guest
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        if not checkout_as_guest_button:
            self.fail("Checkout as guest button not found")
        checkout_as_guest_button.click()

        # Fill billing form
        fields = {
            "BillingNewAddress_FirstName": "Test",
            "BillingNewAddress_LastName": "User",
            "BillingNewAddress_Email": "random_email@test.com",
            "BillingNewAddress_City": "Riga",
            "BillingNewAddress_Address1": "Street 1",
            "BillingNewAddress_ZipPostalCode": "LV-1234",
            "BillingNewAddress_PhoneNumber": "12345678",
        }
        for field, value in fields.items():
            input_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, field))
            )
            if not input_field:
                self.fail(f"{field} input not found")
            input_field.clear()
            input_field.send_keys(value)

        country_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))
        )
        if not country_select:
            self.fail("Country select not found")
        country_select.send_keys("Latvia")

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.NAME, "save"))
        )
        if not continue_button:
            self.fail("Continue button not found")
        continue_button.click()

        # Select shipping method
        shipping_method = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "shippingoption_1"))
        )
        if not shipping_method:
            self.fail("Shipping method not found")
        shipping_method.click()

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button"))
        )
        if not continue_button:
            self.fail("Continue button not found")
        continue_button.click()

        # Select payment method
        payment_method = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
        )
        if not payment_method:
            self.fail("Payment method not found")
        payment_method.click()

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method-next-step-button"))
        )
        if not continue_button:
            self.fail("Continue button not found")
        continue_button.click()

        # Fill payment info
        credit_card_fields = {
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "CardCode": "123",
        }
        for field, value in credit_card_fields.items():
            input_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, field))
            )
            if not input_field:
                self.fail(f"{field} input not found")
            input_field.clear()
            input_field.send_keys(value)

        expire_month = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ExpireMonth"))
        )
        if not expire_month:
            self.fail("Expire Month select not found")
        expire_month.send_keys("04")

        expire_year = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "ExpireYear"))
        )
        if not expire_year:
            self.fail("Expire Year select not found")
        expire_year.send_keys("2027")

        continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-info-next-step-button"))
        )
        if not continue_button:
            self.fail("Continue button not found")
        continue_button.click()

        # Confirm order
        confirm_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button"))
        )
        if not confirm_button:
            self.fail("Confirm button not found")
        confirm_button.click()

        # Check for order completion
        order_complete_message = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed .title strong"))
        )
        if not order_complete_message:
            self.fail("Order completion message not found")
        self.assertIn("Your order has been successfully processed!", order_complete_message.text)

if __name__ == "__main__":
    unittest.main()