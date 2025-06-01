import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://max/"

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Navigate to the home page
        driver.get(f"{self.base_url}/home")
        
        # Step 2: Perform a search for the product
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-box-button")))
        search_button.click()
        
        # Step 3: Add first product to cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()
        
        # Step 4: Go to shopping cart from success popup
        view_cart_button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='bar-notification success']//a[contains(@href, '/cart')]")))
        view_cart_button.click()
        
        # Step 5: Accept terms of service and proceed to checkout
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        
        checkout_button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()
        
        # Step 6: Choose to checkout as a guest
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()
        
        # Step 7: Fill in billing information
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name_input.send_keys("Test")
        last_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_LastName")))
        last_name_input.send_keys("User")
        email_input = driver.find_element(By.ID, "BillingNewAddress_Email")
        email_input.send_keys("random_email@test.com")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.send_keys("Latvia")
        city_input = driver.find_element(By.ID, "BillingNewAddress_City")
        city_input.send_keys("Riga")
        address1_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
        address1_input.send_keys("Street 1")
        zip_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        zip_input.send_keys("LV-1234")
        phone_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        phone_input.send_keys("12345678")
        billing_continue_button = driver.find_element(By.XPATH, "//button[@class='button-1 new-address-next-step-button']")
        billing_continue_button.click()

        # Step 8: Choose shipping method
        shipping_option = driver.find_element(By.ID, "shippingoption_1")
        shipping_option.click()
        shipping_continue_button = driver.find_element(By.XPATH, "//button[@class='button-1 shipping-method-next-step-button']")
        shipping_continue_button.click()

        # Step 9: Select payment method
        payment_method_option = driver.find_element(By.ID, "paymentmethod_1")
        payment_method_option.click()
        payment_continue_button = driver.find_element(By.XPATH, "//button[@class='button-1 payment-method-next-step-button']")
        payment_continue_button.click()

        # Step 10: Fill in payment information
        card_type_select = driver.find_element(By.ID, "CreditCardType")
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
        payment_info_continue_button = driver.find_element(By.XPATH, "//button[@class='button-1 payment-info-next-step-button']")
        payment_info_continue_button.click()

        # Step 11: Confirm order
        confirm_order_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()

        # Step 12: Verify order completion
        order_success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//strong[contains(text(), 'Your order has been successfully processed!')]")))
        self.assertIsNotNone(order_success_message, "Order completion message not found, checkout failed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()