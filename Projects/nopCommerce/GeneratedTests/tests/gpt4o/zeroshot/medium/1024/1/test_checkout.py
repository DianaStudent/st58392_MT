import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver

        # Navigate to Search page
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-button")))
        search_button.click()

        # Add first item to cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Open cart from success popup
        success_notification = self.wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
        if not success_notification:
            self.fail("Success notification not displayed.")
        cart_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Proceed to checkout
        terms_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Choose Checkout as Guest
        checkout_as_guest_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill in billing information
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName"))).send_keys("User")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Email"))).send_keys("random_email")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId"))).send_keys("Latvia")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_City"))).send_keys("Riga")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_Address1"))).send_keys("Street 1")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))).send_keys("LV-1234")
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))).send_keys("12345678")
        self.wait.until(EC.element_to_be_clickable((By.NAME, "save"))).click()

        # Select shipping method
        shipping_option = self.wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_option.click()
        shipping_continue = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shipping-method-next-step-button")))
        shipping_continue.click()

        # Select payment method
        payment_option = self.wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_option.click()
        payment_continue = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-method-next-step-button")))
        payment_continue.click()

        # Enter payment information
        self.wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        self.wait.until(EC.presence_of_element_located((By.ID, "CardNumber"))).send_keys("4111111111111111")
        self.wait.until(EC.presence_of_element_located((By.ID, "ExpireMonth"))).send_keys("04")
        self.wait.until(EC.presence_of_element_located((By.ID, "ExpireYear"))).send_keys("2027")
        self.wait.until(EC.presence_of_element_located((By.ID, "CardCode"))).send_keys("123")
        payment_info_continue = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_continue.click()

        # Confirm order
        confirm_order_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # Validate success message
        success_message = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "title")))
        self.assertTrue(success_message.is_displayed(), "Order completion message not displayed.")


if __name__ == "__main__":
    unittest.main()