import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")  # URL to be replaced with the correct base URL
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the homepage.
        # The page is already opened in setUp()

        # Step 2: Navigate to the "Search" page and look for a product using the query "book".
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".button-1.search-button")))

        search_input.send_keys("book")
        search_button.click()

        # Step 3: Add the first result to the cart using a product tile button.
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Step 4: From the success notification, click the "shopping cart" link.
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Step 5: Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_of_service_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-button")))

        terms_of_service_checkbox.click()
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 7: Fill out the full billing form (from credentials).
        wait.until(EC.presence_of_element_located((By.ID, "opc-billing")))

        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("user_zz18872z@test.com")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        Select(driver.find_element(By.ID, "BillingNewAddress_CountryId")).select_by_value("124")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

        # Step 8: Proceed through the following steps.
        
        # Shipping method step
        wait.until(EC.presence_of_element_located((By.ID, "opc-shipping_method")))
        driver.find_element(By.ID, "shippingoption_1").click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()
        
        # Payment method step
        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_method")))
        driver.find_element(By.ID, "paymentmethod_1").click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()
        
        # Payment info step
        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_info")))
        Select(driver.find_element(By.ID, "CreditCardType")).select_by_value("visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        Select(driver.find_element(By.ID, "ExpireMonth")).select_by_value("4")
        Select(driver.find_element(By.ID, "ExpireYear")).select_by_value("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Step 9: On the confirm step, click “Confirm” and wait for the success message.
        wait.until(EC.presence_of_element_located((By.ID, "opc-confirm_order")))
        driver.find_element(By.CSS_SELECTOR, ".confirm-order-next-step-button").click()

        # Step 10: Confirm that the order has been completed.
        confirmation_message_locator = (By.TAG_NAME, "h1")
        confirmation_message = wait.until(EC.presence_of_element_located(confirmation_message_locator))
        
        self.assertTrue(confirmation_message and confirmation_message.text == "Thank you", "Order confirmation failed")

if __name__ == "__main__":
    unittest.main()