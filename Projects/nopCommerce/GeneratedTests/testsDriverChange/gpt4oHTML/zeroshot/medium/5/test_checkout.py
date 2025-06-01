import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get("http://max/")
        self.assertIn("Your store name", driver.page_source)

        # Step 2: Click on the "Search" link and search for a product (e.g. "book").
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search"))).click()
        
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.clear()
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Step 3: Click the "Add to cart" button for the first item in the search results.
        add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "product-box-add-to-cart-button")))
        if not add_to_cart_buttons:
            self.fail("Add to cart button not found or search yielded no results.")
        add_to_cart_buttons[0].click()

        # Step 4: Open the shopping cart via the success notification popup.
        cart_success_popup = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bar-notification.success .content a[href='/cart']")))
        cart_success_popup.click()

        # Step 5: Accept terms of service and click the "Checkout" button.
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        
        checkout_button = wait.until(EC.presence_of_element_located((By.NAME, "checkout")))
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest".
        checkout_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_guest_button.click()

        # Step 7: Fill in the billing address.
        wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        
        billing_continue_button = wait.until(EC.element_to_be_clickable((By.NAME, "save")))
        billing_continue_button.click()

        # Step 8: Select shipping and payment methods.
        shipping_option = wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_option.click()
        
        shipping_continue_button = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button")
        shipping_continue_button.click()

        payment_option = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_option.click()

        payment_continue_button = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button")
        payment_continue_button.click()

        # Step 9: Enter credit card details.
        wait.until(EC.presence_of_element_located((By.ID, "CreditCardType"))).send_keys("Visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        
        payment_info_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "payment-info-next-step-button")))
        payment_info_continue_button.click()

        # Step 10: Confirm the order.
        confirm_order_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-order-next-step-button")))
        confirm_order_button.click()
        
        # Step 11: Validate that the confirmation message or success section is visible.
        thank_you_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed-page .title strong")))
        self.assertIn("Your order has been successfully processed!", thank_you_message.text)
        self.assertTrue(thank_you_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()