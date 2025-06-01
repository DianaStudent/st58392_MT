import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class TestUserCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_user_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Add the first product to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Click "shopping cart" from the success popup
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Click "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill in billing information
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        last_name_input = driver.find_element(By.ID, "BillingNewAddress_LastName")
        email_input = driver.find_element(By.ID, "BillingNewAddress_Email")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        city_input = driver.find_element(By.ID, "BillingNewAddress_City")
        address1_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
        zip_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        phone_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("random_email")
        country_select.send_keys("Latvia")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_input.send_keys("LV-1234")
        phone_input.send_keys("12345678")

        # Click continue on billing
        continue_button_billing = driver.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button")
        continue_button_billing.click()

        # Select shipping method
        shipping_method = wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_method.click()

        # Continue to payment method
        continue_button_shipping = driver.find_element(By.CSS_SELECTOR, "button.shipping-method-next-step-button")
        continue_button_shipping.click()

        # Select payment method
        payment_method = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method.click()

        # Continue to payment information
        continue_button_payment_method = driver.find_element(By.CSS_SELECTOR, "button.payment-method-next-step-button")
        continue_button_payment_method.click()

        # Fill in payment information
        cardholder_name = wait.until(EC.presence_of_element_located((By.ID, "CardholderName")))
        card_number = driver.find_element(By.ID, "CardNumber")
        expire_month = driver.find_element(By.ID, "ExpireMonth")
        expire_year = driver.find_element(By.ID, "ExpireYear")
        card_code = driver.find_element(By.ID, "CardCode")

        cardholder_name.send_keys("Test User")
        card_number.send_keys("4111111111111111")
        expire_month.send_keys("04")
        expire_year.send_keys("2027")
        card_code.send_keys("123")

        # Continue to confirm order
        continue_button_payment_info = driver.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button")
        continue_button_payment_info.click()

        # Confirm order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirm-order-next-step-button")))
        confirm_order_button.click()

        # Check for order completed message
        order_completed_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title > h1")))
        self.assertEqual(order_completed_message.text, "Thank you")

if __name__ == "__main__":
    unittest.main()