import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Search for a product
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-box-button")))
        search_button.click()

        # Add product to cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to shopping cart from notification
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Checkout as guest
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing details
        first_name = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        first_name.send_keys("Test")
        last_name = driver.find_element(By.ID, "BillingNewAddress_LastName")
        last_name.send_keys("User")
        email = driver.find_element(By.ID, "BillingNewAddress_Email")
        email.send_keys("random_email@test.com")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.send_keys("Latvia")
        city = driver.find_element(By.ID, "BillingNewAddress_City")
        city.send_keys("Riga")
        address1 = driver.find_element(By.ID, "BillingNewAddress_Address1")
        address1.send_keys("Street 1")
        zip_code = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        zip_code.send_keys("LV-1234")
        phone = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")
        phone.send_keys("12345678")

        # Continue to shipping method
        continue_button = driver.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button")
        continue_button.click()

        # Select shipping method
        shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_option.click()
        continue_button = driver.find_element(By.CSS_SELECTOR, "button.shipping-method-next-step-button")
        continue_button.click()

        # Select payment method
        payment_method = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
        payment_method.click()
        continue_button = driver.find_element(By.CSS_SELECTOR, "button.payment-method-next-step-button")
        continue_button.click()

        # Fill payment info
        credit_card_type = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        credit_card_type.send_keys("Visa")
        cardholder_name = driver.find_element(By.ID, "CardholderName")
        cardholder_name.send_keys("Test User")
        card_number = driver.find_element(By.ID, "CardNumber")
        card_number.send_keys("4111111111111111")
        expire_month = driver.find_element(By.ID, "ExpireMonth")
        expire_month.send_keys("04")
        expire_year = driver.find_element(By.ID, "ExpireYear")
        expire_year.send_keys("2027")
        card_code = driver.find_element(By.ID, "CardCode")
        card_code.send_keys("123")

        continue_button = driver.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button")
        continue_button.click()

        # Confirm order
        confirm_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirm-order-next-step-button")))
        confirm_button.click()

        # Assert order confirmation
        confirmation_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.order-completed")))
        self.assertIn("Your order has been successfully processed!", confirmation_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()