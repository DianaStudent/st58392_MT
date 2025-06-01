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
        wait = self.wait
        
        # Step 1: Search for a product
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()
        
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_button = driver.find_element(By.CLASS_NAME, "button-1.search-button")
        
        search_input.send_keys("book")
        search_button.click()
        
        # Step 2: Add the first product to cart
        add_to_cart_button = wait.until( 
            EC.presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 3: Open the shopping cart via the success notification popup
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Step 4: Accept terms and checkout
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 5: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 6: Fill in the billing details
        first_name_input = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        last_name_input = driver.find_element(By.ID, "BillingNewAddress_LastName")
        email_input = driver.find_element(By.ID, "BillingNewAddress_Email")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        city_input = driver.find_element(By.ID, "BillingNewAddress_City")
        address1_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
        zip_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        phone_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        continue_button = driver.find_element(By.CLASS_NAME, "new-address-next-step-button")
        
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("random_email")
        country_select.send_keys("Latvia")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_input.send_keys("LV-1234")
        phone_input.send_keys("12345678")
        continue_button.click()

        # Step 7: Select shipping method
        shipping_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shippingoption_1")))
        shipping_option.click()

        shipping_continue = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button")
        shipping_continue.click()

        # Step 8: Select payment method
        payment_method_option = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))
        )
        payment_method_option.click()

        payment_continue = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button")
        payment_continue.click()

        # Step 9: Enter credit card details
        card_type_select = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        cardholder_name_input = driver.find_element(By.ID, "CardholderName")
        card_number_input = driver.find_element(By.ID, "CardNumber")
        expire_month_select = driver.find_element(By.ID, "ExpireMonth")
        expire_year_select = driver.find_element(By.ID, "ExpireYear")
        card_code_input = driver.find_element(By.ID, "CardCode")
        payment_info_continue = driver.find_element(By.CLASS_NAME, "payment-info-next-step-button")

        card_type_select.send_keys("Visa")
        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("4111111111111111")
        expire_month_select.send_keys("04")
        expire_year_select.send_keys("2027")
        card_code_input.send_keys("123")
        payment_info_continue.click()

        # Step 10: Confirm the order
        confirm_order_button = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Step 11: Validate successful order completion
        order_completion_message = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "order-completed"))
        )

        if not order_completion_message:
            self.fail("Order completion message not found!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()