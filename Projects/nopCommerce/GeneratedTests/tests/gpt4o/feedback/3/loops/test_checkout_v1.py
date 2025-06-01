import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        # Setup the Selenium WebDriver with Chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the homepage
        driver.get("http://max/")
        
        # Step 2: Navigate to the "Search" page and look for a product using the query "book"
        search_box = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#small-searchterms")))
        search_box.send_keys("book")
        search_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
        search_button.click()
        
        # Step 3: Add the first result to the cart using a product tile button
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 4: From the success notification, click the "shopping cart" link
        cart_link = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "div.bar-notification a[href='/cart']"))
        )
        cart_link.click()
        
        # Step 5: Check "Terms of service" checkbox and click "Checkout" button
        terms_of_service_checkbox = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input#termsofservice"))
        )
        terms_of_service_checkbox.click()
        checkout_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button#checkout"))
        )
        checkout_button.click()
        
        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()
        
        # Step 7: Fill out the full billing form
        first_name = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input#BillingNewAddress_FirstName"))
        )
        first_name.send_keys("Test")
        
        last_name = driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_LastName")
        last_name.send_keys("User")
        
        email = driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_Email")
        email.send_keys("random_email@test.com")
        
        city = driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_City")
        city.send_keys("Riga")
        
        address1 = driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_Address1")
        address1.send_keys("Street 1")
        
        zip_code = driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_ZipPostalCode")
        zip_code.send_keys("LV-1234")
        
        phone_number = driver.find_element(By.CSS_SELECTOR, "input#BillingNewAddress_PhoneNumber")
        phone_number.send_keys("12345678")
        
        country_select = driver.find_element(By.CSS_SELECTOR, "select#BillingNewAddress_CountryId")
        country_select.send_keys("Latvia")
        
        continue_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.new-address-next-step-button"))
        )
        continue_button.click()
        
        # Step 8: Proceed through the following
        # Shipping method step
        shipping_method_continue = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.shipping-method-next-step-button"))
        )
        shipping_method_continue.click()

        # Payment method step
        payment_method_option = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input#paymentmethod_1"))
        )
        payment_method_option.click()
        
        payment_method_continue = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.payment-method-next-step-button"))
        )
        payment_method_continue.click()

        # Payment info step
        credit_card_type = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "select#CreditCardType"))
        )
        credit_card_type.send_keys("Visa")
        
        cardholder_name = driver.find_element(By.CSS_SELECTOR, "input#CardholderName")
        cardholder_name.send_keys("Test User")
        
        card_number = driver.find_element(By.CSS_SELECTOR, "input#CardNumber")
        card_number.send_keys("4111111111111111")
        
        exp_month = driver.find_element(By.CSS_SELECTOR, "select#ExpireMonth")
        exp_month.send_keys("04")
        
        exp_year = driver.find_element(By.CSS_SELECTOR, "select#ExpireYear")
        exp_year.send_keys("2027")
        
        card_code = driver.find_element(By.CSS_SELECTOR, "input#CardCode")
        card_code.send_keys("123")
        
        payment_info_continue = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.payment-info-next-step-button"))
        )
        payment_info_continue.click()
        
        # Step 9: On the confirm step, click “Confirm” and wait for the success message
        confirm_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.confirm-order-next-step-button"))
        )
        confirm_button.click()
        
        # Step 10: Confirm that the order has been completed by checking the confirmation text "Thank you" appears
        thank_you_text = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Thank you']"))
        )
        self.assertTrue(thank_you_text, "Order completion message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()