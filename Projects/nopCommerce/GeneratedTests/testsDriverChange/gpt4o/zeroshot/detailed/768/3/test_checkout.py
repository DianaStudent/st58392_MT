from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestUserCheckout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 1. Navigate to the "Search" page and look for a product using the query "book".
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-box-button")
        search_button.click()

        # 2. Add the first result to the cart using a product tile button.
        add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        add_to_cart_buttons[0].click()

        # 3. From the success notification, click the "shopping cart" link.
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # 4. Check "Terms of service" and click "Checkout".
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # 5. Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-1.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 6. Fill out the billing form.
        self.fill_billing_form()

        # 7. Proceed through:
        # Shipping method step
        self.continue_on_shipping_method()
        # Payment method step
        self.continue_on_payment_method()
        # Payment info step and fill out credit card details
        self.fill_payment_info()

        # 8. Confirm the order
        self.confirm_order()

        # 9. Confirm that the order has been completed
        self.verify_order_completion()

    def fill_billing_form(self):
        wait = self.wait
        driver = self.driver

        first_name = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        last_name = driver.find_element(By.ID, "BillingNewAddress_LastName")
        email = driver.find_element(By.ID, "BillingNewAddress_Email")
        country = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        state = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        city = driver.find_element(By.ID, "BillingNewAddress_City")
        address = driver.find_element(By.ID, "BillingNewAddress_Address1")
        zip_code = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        phone = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")

        first_name.send_keys("Test")
        last_name.send_keys("User")
        email.send_keys("random_email")
        country.send_keys("Latvia")
        state.send_keys("Other")
        city.send_keys("Riga")
        address.send_keys("Street 1")
        zip_code.send_keys("LV-1234")
        phone.send_keys("12345678")

        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

    def continue_on_shipping_method(self):
        wait = self.wait
        driver = self.driver

        continue_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#opc-shipping_method .button-1")))
        continue_button.click()

    def continue_on_payment_method(self):
        wait = self.wait
        driver = self.driver
        
        payment_option = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_option.click()

        continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        continue_button.click()

    def fill_payment_info(self):
        wait = self.wait
        driver = self.driver
        
        card_type = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        cardholder_name = driver.find_element(By.ID, "CardholderName")
        card_number = driver.find_element(By.ID, "CardNumber")
        expire_month = driver.find_element(By.ID, "ExpireMonth")
        expire_year = driver.find_element(By.ID, "ExpireYear")
        card_code = driver.find_element(By.ID, "CardCode")

        card_type.send_keys("Visa")
        cardholder_name.send_keys("Test User")
        card_number.send_keys("4111111111111111")
        expire_month.send_keys("04")
        expire_year.send_keys("2027")
        card_code.send_keys("123")

        continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        continue_button.click()

    def confirm_order(self):
        wait = self.wait
        driver = self.driver

        confirm_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_button.click()

    def verify_order_completion(self):
        wait = self.wait
        
        thank_you_message = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertEqual(thank_you_message.text, "Thank you")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()