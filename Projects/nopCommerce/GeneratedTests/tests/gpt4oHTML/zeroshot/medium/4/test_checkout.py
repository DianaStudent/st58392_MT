import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Open the home page
        driver.get("http://example.com")  # replace with actual URL

        # Step 2: Click on the "Search" link and search for a product (e.g. "book").
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 3: Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Step 4: Open the shopping cart via the success notification popup.
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "bar-notification")))
        cart_link = driver.find_element(By.CSS_SELECTOR, ".bar-notification .content a")
        cart_link.click()

        # Step 5: Accept terms of service and click the "Checkout" button.
        terms_of_service_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()
        checkout_button = driver.find_element(By.NAME, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest".
        checkout_as_guest_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 7: Fill in the billing address.
        self.fill_billing_address()

        # Step 8: Select shipping and payment methods.
        self.select_shipping_method()
        self.select_payment_method()

        # Step 9: Enter credit card details.
        self.enter_payment_information()

        # Step 10: Confirm the order.
        confirm_order_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # Step 11: Validate that the confirmation message or success section is visible.
        confirmation_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "order-completed")))
        if not confirmation_message.is_displayed():
            self.fail("Order confirmation message not visible")

    def fill_billing_address(self):
        driver = self.driver
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'BillingNewAddress_FirstName'))
        )
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        Select(driver.find_element(By.ID, "BillingNewAddress_CountryId")).select_by_value('124')  # Latvia
        Select(driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")).select_by_value('0')  # Other
        driver.find_element(By.NAME, "save").click()

    def select_shipping_method(self):
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1"))).click()  # Next Day Air
        driver.find_element(By.CSS_SELECTOR, "button.shipping-method-next-step-button").click()

    def select_payment_method(self):
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1"))).click()  # Credit Card
        driver.find_element(By.CSS_SELECTOR, "button.payment-method-next-step-button").click()

    def enter_payment_information(self):
        driver = self.driver
        self.wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        Select(driver.find_element(By.ID, "ExpireMonth")).select_by_value("4")
        Select(driver.find_element(By.ID, "ExpireYear")).select_by_value("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()