import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_checkout_process(self):
        driver = self.driver
        
        # Navigate to the "Search" page
        search_link = self.wait.until(presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Search for a product using the query "book"
        search_input = self.wait.until(presence_of_element_located((By.CLASS_NAME, "search-box-text")))
        search_input.send_keys("book")
        search_button = self.wait.until(presence_of_element_located((By.CLASS_NAME, "search-box-button")))
        search_button.click()

        # Add the first result to the cart
        add_to_cart_button = self.wait.until(presence_of_element_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Click "shopping cart" from the success notification
        success_notification = self.wait.until(presence_of_element_located((By.CLASS_NAME, "bar-notification")))
        shopping_cart_link = self.wait.until(presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        shopping_cart_link.click()

        # Check the "Terms of service" and click "Checkout"
        terms_of_service_checkbox = self.wait.until(presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()
        checkout_button = self.wait.until(presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

        # Choose "Checkout as Guest"
        checkout_as_guest_button = self.wait.until(presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill out the billing form
        fname_input = self.wait.until(presence_of_element_located((By.ID, "BillingNewAddress_FirstName")))
        lname_input = driver.find_element(By.ID, "BillingNewAddress_LastName")
        email_input = driver.find_element(By.ID, "BillingNewAddress_Email")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        state_select = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        city_input = driver.find_element(By.ID, "BillingNewAddress_City")
        address_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
        zip_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        phone_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")

        fname_input.send_keys("Test")
        lname_input.send_keys("User")
        email_input.send_keys("random_email")
        wait.until(visibility_of_element_located((By.CSS_SELECTOR, "option[value='124']"))).click()  # Country: Latvia
        wait.until(visibility_of_element_located((By.CSS_SELECTOR, "option[value='0']"))).click()   # State/Province: Other
        city_input.send_keys("Riga")
        address_input.send_keys("Street 1")
        zip_input.send_keys("LV-1234")
        phone_input.send_keys("12345678")
        
        billing_continue_button = driver.find_element(By.CSS_SELECTOR, "#billing-buttons-container .button-1")
        billing_continue_button.click()

        # Shipping method step
        shipping_continue_button = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "#shipping-method-buttons-container .button-1")))
        shipping_continue_button.click()

        # Payment method step
        payment_method_option = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))).click()
        payment_continue_button = driver.find_element(By.CSS_SELECTOR, "#payment-method-buttons-container .button-1")
        payment_continue_button.click()

        # Payment info step
        cardholder_input = self.wait.until(presence_of_element_located((By.ID, "CardholderName")))
        cardnumber_input = driver.find_element(By.ID, "CardNumber")
        expiremonth_select = driver.find_element(By.ID, "ExpireMonth")
        expireyear_select = driver.find_element(By.ID, "ExpireYear")
        cardcode_input = driver.find_element(By.ID, "CardCode")

        cardholder_input.send_keys("Test User")
        cardnumber_input.send_keys("4111111111111111")
        expiremonth_select.find_element(By.CSS_SELECTOR, "option[value='4']").click()
        expireyear_select.find_element(By.CSS_SELECTOR, "option[value='2027']").click()
        cardcode_input.send_keys("123")

        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, "#payment-info-buttons-container .button-1")
        payment_info_continue_button.click()

        # Confirm order step
        confirm_button = self.wait.until(presence_of_element_located((By.CSS_SELECTOR, "#confirm-order-buttons-container .button-1")))
        confirm_button.click()

        # Assertion: Confirm that the order has been completed
        confirmation_message = self.wait.until(presence_of_element_located((By.TAG_NAME, "h1")))
        self.assertTrue("Thank you" in confirmation_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()