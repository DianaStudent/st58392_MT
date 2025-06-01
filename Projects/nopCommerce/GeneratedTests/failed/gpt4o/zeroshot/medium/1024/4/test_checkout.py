from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
        
    def test_checkout_process(self):
        driver = self.driver

        # 1. Open the home page (already opened in setUp)
        
        # 2. Click on the "Search" link and search for a product (e.g. "book").
        search_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        
        search_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.search-button")))
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # 4. Open the shopping cart via the success notification popup.
        cart_success = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_success.click()

        # 5. Accept terms of service and click the "Checkout" button.
        terms_service_checkbox = self.wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_service_checkbox.click()

        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest".
        checkout_as_guest_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-1.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill in the billing address.
        self.fill_billing_information()

        # 8. Select shipping and payment methods.
        self.select_shipping_method()
        self.select_payment_method()

        # 9. Enter credit card details.
        self.enter_payment_information()

        # 10. Confirm the order.
        confirm_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-1.confirm-order-next-step-button")))
        confirm_button.click()

        # 11. Validate that the confirmation message or success section is visible.
        confirmation_message = self.wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.order-completed strong")))
        if not confirmation_message or "successfully processed" not in confirmation_message.text:
            self.fail("Order completion message not found.")

    def fill_billing_information(self):
        driver = self.driver
        self.wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("124")
        driver.find_element(By.ID, "BillingNewAddress_StateProvinceId").send_keys("0")
        next_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-1.new-address-next-step-button")))
        next_button.click()

    def select_shipping_method(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1"))).click()
        continue_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-1.shipping-method-next-step-button")))
        continue_button.click()

    def select_payment_method(self):
        self.wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1"))).click()
        continue_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-1.payment-method-next-step-button")))
        continue_button.click()

    def enter_payment_information(self):
        driver = self.driver
        driver.find_element(By.ID, "CreditCardType").send_keys("visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("4")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        continue_button = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.button-1.payment-info-next-step-button")))
        continue_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()