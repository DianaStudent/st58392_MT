from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to Search page
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Enter search term
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.send_keys("book")
        
        # Click search button
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Add first product to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Click 'shopping cart' in the success notification
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Agree to terms of service and proceed to checkout
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_checkbox.click()

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Choose checkout as guest
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable(
            (By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing form
        fields = {
            "BillingNewAddress_FirstName": "Test",
            "BillingNewAddress_LastName": "User",
            "BillingNewAddress_Email": "random_email",
            "BillingNewAddress_City": "Riga",
            "BillingNewAddress_Address1": "Street 1",
            "BillingNewAddress_ZipPostalCode": "LV-1234",
            "BillingNewAddress_PhoneNumber": "12345678"
        }
        
        for field_id, value in fields.items():
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.send_keys(value)

        # Select country
        country_dropdown = Select(wait.until(EC.presence_of_element_located(
            (By.ID, "BillingNewAddress_CountryId"))))
        country_dropdown.select_by_value("124")  # Latvia

        # Click Continue on billing form
        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

        # Shipping Method Selection
        shipping_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1")))
        shipping_option.click()
        shipping_continue_button = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        shipping_continue_button.click()

        # Payment Method Selection
        payment_option = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1")))
        payment_option.click()
        payment_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_button.click()

        # Payment Information
        credit_card_fields = {
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "ExpireMonth": "4",
            "ExpireYear": "2027",
            "CardCode": "123"
        }

        for field_id, value in credit_card_fields.items():
            field = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            field.send_keys(value)

        card_choose = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        card_choose.select_by_value("visa")

        # Confirm order
        confirm_button = driver.find_element(By.CSS_SELECTOR, ".confirm-order-next-step-button")
        confirm_button.click()

        # Check order completion
        thank_you = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title h1")))
        self.assertEqual(thank_you.text, "Thank you", "Order was not completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()