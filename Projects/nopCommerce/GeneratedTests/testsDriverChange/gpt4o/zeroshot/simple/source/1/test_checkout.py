import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        driver = self.driver
        
        # Search for a product
        search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book" + Keys.RETURN)
        
        # Add first product to cart
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-grid .item-box .button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()
        
        # Click “shopping cart” from the success popup
        cart_link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bar-notification a[href='/cart']")))
        cart_link.click()
        
        # Proceed as guest checkout
        checkout_button = self.wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        
        checkout_as_guest_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()
        
        # Fill billing form
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_LastName"))).send_keys("User")
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_Email"))).send_keys("random_email")
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_City"))).send_keys("Riga")
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_Address1"))).send_keys("Street 1")
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_ZipPostalCode"))).send_keys("LV-1234")
        self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_PhoneNumber"))).send_keys("12345678")
        
        country_dropdown = self.wait.until(EC.visibility_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_dropdown.send_keys(Keys.HOME, Keys.ARROW_DOWN, Keys.ENTER)  # Select first option
        
        continue_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".new-address-next-step-button")))
        continue_button.click()
        
        # Select shipping method
        shipping_option = self.wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_option.click()
        
        continue_button_shipping = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button")))
        continue_button_shipping.click()
        
        # Select payment method
        payment_option = self.wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
        payment_option.click()
        
        continue_button_payment = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method-next-step-button")))
        continue_button_payment.click()
        
        # Enter payment information
        self.wait.until(EC.visibility_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        self.wait.until(EC.visibility_of_element_located((By.ID, "CardNumber"))).send_keys("4111111111111111")
        expire_month = self.wait.until(EC.visibility_of_element_located((By.ID, "ExpireMonth")))
        expire_month.send_keys("04")
        expire_year = self.wait.until(EC.visibility_of_element_located((By.ID, "ExpireYear"))).send_keys("2027")
        self.wait.until(EC.visibility_of_element_located((By.ID, "CardCode"))).send_keys("123")
        
        continue_button_payment_info = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-info-next-step-button")))
        continue_button_payment_info.click()
        
        # Confirm order
        confirm_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()
        
        # Check for order completion
        thank_you_message = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-completed-page .title strong")))
        self.assertEqual(thank_you_message.text, "Your order has been successfully processed!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()