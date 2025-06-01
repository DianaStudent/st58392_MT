import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        
        # Step 1: Open the home page
        driver.get("http://max/")

        # Step 2: Click on the "Search" link and search for a product
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        search_box = self.wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.search-button")
        search_button.click()

        # Step 3: Click the "Add to cart" button for the first item in the search results
        add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.product-box-add-to-cart-button")))
        if not add_to_cart_buttons:
            self.fail("Add to cart buttons not found.")
        add_to_cart_buttons[0].click()

        # Step 4: Open the shopping cart via the success notification popup
        success_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        success_link.click()

        # Step 5: Accept terms of service and click the "Checkout" button
        tos_checkbox = self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        tos_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 7: Fill in the billing address
        first_name_input = self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name_input.send_keys("Test")
        
        last_name_input = driver.find_element(By.ID, "BillingNewAddress_LastName")
        last_name_input.send_keys("User")
        
        email_input = driver.find_element(By.ID, "BillingNewAddress_Email")
        email_input.send_keys("random_email@test.com")
        
        country_id_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_id_select.send_keys(Keys.TAB(124))
        
        state_id_select = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        state_id_select.send_keys(Keys.TAB(0))
        
        city_input = driver.find_element(By.ID, "BillingNewAddress_City")
        city_input.send_keys("Riga")
        
        address1_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
        address1_input.send_keys("Street 1")
        
        zip_code_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        zip_code_input.send_keys("LV-1234")
        
        phone_number_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        phone_number_input.send_keys("12345678")
        
        continue_button_billing = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button_billing.click()

        # Step 8: Select shipping and payment methods
        shipping_option = self.wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_option.click()
        
        continue_button_shipping = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        continue_button_shipping.click()
        
        payment_method = self.wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method.click()
        
        continue_button_payment = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        continue_button_payment.click()

        # Step 9: Enter credit card details
        card_type_select = self.wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
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

        continue_button_payment_info = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        continue_button_payment_info.click()

        # Step 10: Confirm the order
        confirm_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_button.click()

        # Step 11: Validate that the confirmation message or success section is visible
        order_complete_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed")))
        if not order_complete_message:
            self.fail("Order completion message not found.")
        self.assertTrue(order_complete_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()