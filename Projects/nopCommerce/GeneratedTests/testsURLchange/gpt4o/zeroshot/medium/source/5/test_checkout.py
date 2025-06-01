from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.base_url = "http://max/"

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # Step 1: Open home page
        self.assertIn("nopCommerce", driver.title)

        # Step 2: Click on "Search" and search for "book"
        search_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        search_box = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "q"))
        )
        search_box.send_keys("book" + Keys.RETURN)

        # Step 3: Add the first product to the cart
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 4: Open the shopping cart via notification popup
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success"))
        )
        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Step 5: Accept terms of service and checkout
        terms_checkbox = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "termsofservice"))
        )
        terms_checkbox.click()

        checkout_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "checkout"))
        )
        checkout_button.click()

        # Step 6: Checkout as Guest
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 7: Fill in billing details
        self.fill_billing_details(driver)

        # Step 8: Select shipping method
        shipping_option = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "shippingoption_1"))
        )
        shipping_option.click()

        shipping_continue_button = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        shipping_continue_button.click()

        # Step 9: Select payment method
        payment_method = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "paymentmethod_1"))
        )
        payment_method.click()

        payment_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_button.click()

        # Step 10: Enter payment info
        self.fill_payment_info(driver)

        # Step 11: Confirm the order
        confirm_button = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button"))
        )
        confirm_button.click()

        # Validation: Check for order completion
        order_completed_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-completed"))
        )
        self.assertTrue(order_completed_message)

    def fill_billing_details(self, driver):
        fields = {
            "BillingNewAddress_FirstName": "Test",
            "BillingNewAddress_LastName": "User",
            "BillingNewAddress_Email": "random_email",
            "BillingNewAddress_City": "Riga",
            "BillingNewAddress_Address1": "Street 1",
            "BillingNewAddress_ZipPostalCode": "LV-1234",
            "BillingNewAddress_PhoneNumber": "12345678",
        }

        for field_id, value in fields.items():
            field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, field_id))
            )
            field.send_keys(value)

        country_select = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "BillingNewAddress_CountryId"))
        )
        for option in country_select.find_elements_by_tag_name('option'):
            if option.text == 'Latvia':
                option.click()
                break

        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

    def fill_payment_info(self, driver):
        fields = {
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "CardCode": "123",
        }

        for field_id, value in fields.items():
            field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, field_id))
            )
            field.send_keys(value)

        expiry_month_select = driver.find_element(By.ID, "ExpireMonth")
        expiry_month_select.send_keys("04")

        expiry_year_select = driver.find_element(By.ID, "ExpireYear")
        expiry_year_select.send_keys("2027")

        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()