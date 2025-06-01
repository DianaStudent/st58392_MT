from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import random
import string

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Open the homepage
        driver.get("http://max/")
        
        # Step 2: Navigate to the "Search" page and look for a product using the query "book".
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".top-menu.notmobile > li:nth-child(3) > a"))).click()
        search_input = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#q")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-button")
        search_button.click()
        
        # Step 3: Add the first result to the cart using a product tile button.
        first_product_add_to_cart = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".product-box-add-to-cart-button")
            )
        )
        first_product_add_to_cart.click()
        
        # Step 4: From the success notification, click the "shopping cart" link.
        shopping_cart_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        shopping_cart_link.click()
        
        # Step 5: Check the "Terms of service" checkbox and click the "Checkout" button.
        terms_of_service_checkbox = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#termsofservice"))
        )
        terms_of_service_checkbox.click()
        checkout_button = driver.find_element(By.CSS_SELECTOR, ".button-1.checkout-button")
        checkout_button.click()
        
        # Step 6: Choose "Checkout as Guest".
        checkout_as_guest_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()
        
        # Step 7: Fill out the full billing form
        first_name = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#BillingNewAddress_FirstName"))
        )
        first_name.send_keys("Test")
        
        last_name = driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_LastName")
        last_name.send_keys("User")
        
        email_input = driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_Email")
        random_email = f"user_{''.join(random.choices(string.ascii_lowercase + string.digits, k=6))}@test.com"
        email_input.send_keys(random_email)
        
        address_input = driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_Address1")
        address_input.send_keys("Street 1")
        
        city_input = driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_City")
        city_input.send_keys("Riga")
        
        country_dropdown = driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_CountryId")
        country_dropdown.send_keys("Latvia")
        
        zip_input = driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_ZipPostalCode")
        zip_input.send_keys("LV-1234")
        
        phone_input = driver.find_element(By.CSS_SELECTOR, "#BillingNewAddress_PhoneNumber")
        phone_input.send_keys("12345678")
        
        # Step 8: Proceed through the stages
        driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button").click()
        
        # Shipping method step
        shipping_method_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))
        )
        shipping_method_btn.click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()
        
        # Payment method step
        payment_method_btn = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))
        )
        payment_method_btn.click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()
        
        # Payment info step
        cardholder_name = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#CardholderName"))
        )
        cardholder_name.send_keys("Test User")
        
        card_number = driver.find_element(By.CSS_SELECTOR, "#CardNumber")
        card_number.send_keys("4111111111111111")
        
        expire_month = driver.find_element(By.CSS_SELECTOR, "#ExpireMonth")
        expire_month.send_keys("04")
        
        expire_year = driver.find_element(By.CSS_SELECTOR, "#ExpireYear")
        expire_year.send_keys("2027")
        
        card_code = driver.find_element(By.CSS_SELECTOR, "#CardCode")
        card_code.send_keys("123")
        
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()
        
        # Step 9: Confirm the order
        confirm_order_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button"))
        )
        confirm_order_btn.click()
        
        # Step 10: Confirm order completion
        thank_you_message = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".page.title h1"))
        )
        
        self.assertEqual(thank_you_message.text, "Thank you", "Order completion message not found.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()