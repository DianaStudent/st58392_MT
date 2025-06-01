from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to home page
        driver.get("http://max/")

        # Search for a product
        search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#small-searchterms")))
        search_box.send_keys("book")
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-box-button")))
        search_button.click()

        # Add first product to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Handle success notification and go to cart
        notification = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.cart-button")))
        go_to_cart_button.click()

        # Agree to terms and check out
        agree_terms = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#termsofservice")))
        agree_terms.click()

        checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.checkout-button")))
        checkout_button.click()

        # Checkout as guest
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing form
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_Email").send_keys("random_email@example.com")
        driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_PhoneNumber").send_keys("12345678")

        country_select = driver.find_element(By.CSS_SELECTOR, "select#BillingNewAddress_CountryId")
        country_select.send_keys(Keys.DOWN) # move to correct country
        state_select = driver.find_element(By.CSS_SELECTOR, "select#BillingNewAddress_StateProvinceId")
        state_select.send_keys(Keys.DOWN) # set state to "Other"

        billing_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.new-address-next-step-button")))
        billing_continue_button.click()

        # Select shipping method
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#shippingoption_1"))).click()
        shipping_method_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.shipping-method-next-step-button")))
        shipping_method_button.click()

        # Select payment method
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input#paymentmethod_1"))).click()
        payment_method_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.payment-method-next-step-button")))
        payment_method_button.click()

        # Fill payment information
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "select#CreditCardType"))).send_keys("visa")
        driver.find_element(By.CSS_SELECTOR, "input#CardholderName").send_keys("Test User")
        driver.find_element(By.CSS_SELECTOR, "input#CardNumber").send_keys("4111111111111111")
        driver.find_element(By.CSS_SELECTOR, "select#ExpireMonth").send_keys("04")
        driver.find_element(By.CSS_SELECTOR, "select#ExpireYear").send_keys("2027")
        driver.find_element(By.CSS_SELECTOR, "input#CardCode").send_keys("123")

        payment_info_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.payment-info-next-step-button")))
        payment_info_button.click()

        # Confirm order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirm-order-next-step-button")))
        confirm_order_button.click()

        # Verify order completion
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.order-completed .title")))
        self.assertIn("Your order has been successfully processed!", success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()