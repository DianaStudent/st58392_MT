import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        # Initialize the Chrome Driver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://max/')  # Use your base URL for the e-commerce site
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product: Input "book" in the search bar and submit
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, 'small-searchterms')))
            search_box.send_keys('book')
            search_button = driver.find_element(By.CSS_SELECTOR, 'button.button-1.search-box-button')
            search_button.click()
        except Exception as e:
            self.fail(f"Failed at searching a product: {str(e)}")
        
        # Add the first product found to the cart
        try:
            add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'button.button-2.product-box-add-to-cart-button')))
            add_to_cart_buttons[0].click()
        except Exception as e:
            self.fail(f"Failed at adding product to cart: {str(e)}")
        
        # Click “shopping cart” from the success popup
        try:
            success_popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.bar-notification.success')))
            cart_link = success_popup.find_element(By.LINK_TEXT, 'shopping cart')
            cart_link.click()
        except Exception as e:
            self.fail(f"Failed at clicking shopping cart: {str(e)}")
        
        # Agree to terms of service and click Checkout
        try:
            terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, 'termsofservice')))
            terms_checkbox.click()
            checkout_button = driver.find_element(By.ID, 'checkout')
            checkout_button.click()
        except Exception as e:
            self.fail(f"Failed at starting checkout: {str(e)}")
        
        # Use the "Checkout as Guest" option
        try:
            guest_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.checkout-as-guest-button')))
            guest_checkout_button.click()
        except Exception as e:
            self.fail(f"Failed at checkout as Guest: {str(e)}")
        
        # Fill out the billing information form
        try:
            first_name = wait.until(EC.presence_of_element_located((By.ID, 'BillingNewAddress_FirstName')))
            first_name.send_keys("Test")
            last_name = driver.find_element(By.ID, 'BillingNewAddress_LastName')
            last_name.send_keys("User")
            email = driver.find_element(By.ID, 'BillingNewAddress_Email')
            email.send_keys("random_email")
            country = driver.find_element(By.ID, 'BillingNewAddress_CountryId')
            country.send_keys("Latvia")
            city = driver.find_element(By.ID, 'BillingNewAddress_City')
            city.send_keys("Riga")
            address1 = driver.find_element(By.ID, 'BillingNewAddress_Address1')
            address1.send_keys("Street 1")
            zip_code = driver.find_element(By.ID, 'BillingNewAddress_ZipPostalCode')
            zip_code.send_keys("LV-1234")
            phone_number = driver.find_element(By.ID, 'BillingNewAddress_PhoneNumber')
            phone_number.send_keys("12345678")
            continue_button = driver.find_element(By.CSS_SELECTOR, 'button.new-address-next-step-button')
            continue_button.click()
        except Exception as e:
            self.fail(f"Failed at filling billing form: {str(e)}")
        
        # Select shipping method
        try:
            next_day_air = wait.until(EC.presence_of_element_located((By.ID, 'shippingoption_1')))
            next_day_air.click()
            continue_button_shipping = driver.find_element(By.CSS_SELECTOR, 'button.shipping-method-next-step-button')
            continue_button_shipping.click()
        except Exception as e:
            self.fail(f"Failed at selecting shipping method: {str(e)}")
        
        # Select payment method
        try:
            credit_card_option = wait.until(EC.presence_of_element_located((By.ID, 'paymentmethod_1')))
            credit_card_option.click()
            continue_button_payment = driver.find_element(By.CSS_SELECTOR, 'button.payment-method-next-step-button')
            continue_button_payment.click()
        except Exception as e:
            self.fail(f"Failed at selecting payment method: {str(e)}")
        
        # Fill out payment information
        try:
            card_type = wait.until(EC.presence_of_element_located((By.ID, 'CreditCardType')))
            card_type.send_keys("Visa")
            cardholder_name = driver.find_element(By.ID, 'CardholderName')
            cardholder_name.send_keys("Test User")
            card_number = driver.find_element(By.ID, 'CardNumber')
            card_number.send_keys("4111111111111111")
            expire_month = driver.find_element(By.ID, 'ExpireMonth')
            expire_month.send_keys("04")
            expire_year = driver.find_element(By.ID, 'ExpireYear')
            expire_year.send_keys("2027")
            card_code = driver.find_element(By.ID, 'CardCode')
            card_code.send_keys("123")
            payment_info_continue = driver.find_element(By.CSS_SELECTOR, 'button.payment-info-next-step-button')
            payment_info_continue.click()
        except Exception as e:
            self.fail(f"Failed at filling payment info: {str(e)}")
        
        # Confirm order
        try:
            confirm_order_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button.confirm-order-next-step-button')))
            confirm_order_button.click()
        except Exception as e:
            self.fail(f"Failed during order confirmation: {str(e)}")
        
        # Check for success message
        try:
            success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div.order-completed strong')))
            self.assertEqual(success_message.text, "Your order has been successfully processed!")
        except Exception as e:
            self.fail(f"Order completion message not found: {str(e)}")
    
    def tearDown(self):
        # Close the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()