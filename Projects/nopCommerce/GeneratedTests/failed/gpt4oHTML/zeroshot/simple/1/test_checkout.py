from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.implicitly_wait(10)

    def test_checkout_as_guest(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for "book"
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # Add first product to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to cart from the success notification
        go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bar-notification.success a[href='/cart']")))
        go_to_cart_button.click()

        # Accept terms and proceed to checkout
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Checkout as Guest
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing form
        first_name_input = wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName")))
        first_name_input.send_keys("Test")
        last_name_input = driver.find_element(By.ID, "BillingNewAddress_LastName")
        last_name_input.send_keys("User")
        email_input = driver.find_element(By.ID, "BillingNewAddress_Email")
        email_input.send_keys("random_email")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.send_keys("Latvia")
        city_input = driver.find_element(By.ID, "BillingNewAddress_City")
        city_input.send_keys("Riga")
        address1_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
        address1_input.send_keys("Street 1")
        zip_postal_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        zip_postal_input.send_keys("LV-1234")
        phone_number_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        phone_number_input.send_keys("12345678")
        
        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

        # Choose shipping method
        shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_option.click()
        shipping_continue_button = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button")
        shipping_continue_button.click()

        # Choose payment method
        payment_method = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method.click()
        payment_continue_button = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button")
        payment_continue_button.click()

        # Fill payment info
        card_type_select = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        card_type_select.send_keys("Visa")
        cardholder_name_input = driver.find_element(By.ID, "CardholderName")
        cardholder_name_input.send_keys("Test User")
        card_number_input = driver.find_element(By.ID, "CardNumber")
        card_number_input.send_keys("4111111111111111")
        expire_month_select = driver.find_element(By.ID, "ExpireMonth")
        expire_month_select.send_keys("04")
        expire_year_select = driver.find_element(By.ID, "ExpireYear")
        expire_year_select.send_keys("2027")
        card_code_input = driver.find_element(By.ID, "CardCode")
        card_code_input.send_keys("123")

        payment_info_continue_button = driver.find_element(By.CLASS_NAME, "payment-info-next-step-button")
        payment_info_continue_button.click()

        # Confirm order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # Verify order completion
        order_completed_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".section.order-completed .title"))
        )
        success_text = order_completed_message.text

        self.assertIn("Your order has been successfully processed!", success_text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()