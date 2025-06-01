import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")  # Assuming this is the homepage URL
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Click on "Search" link
        search_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 3: Search for a product
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book", Keys.RETURN)

        # Step 4: Add the first item to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Step 5: Open the cart from the success notification
        go_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bar-notification.success a[href='/cart']")))
        go_to_cart_button.click()

        # Step 6: Agree to terms and proceed to checkout
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # Step 7: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-1.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 8: Fill in the billing address
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys(Keys.END)
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        billing_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".new-address-next-step-button")))
        billing_continue_button.click()

        # Step 9: Select shipping method
        shipping_method_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1")))
        shipping_method_radio.click()
        shipping_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button")))
        shipping_continue_button.click()

        # Step 10: Select payment method
        payment_method_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1")))
        payment_method_radio.click()
        payment_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method-next-step-button")))
        payment_continue_button.click()

        # Step 11: Enter credit card details
        wait.until(EC.presence_of_element_located((By.ID, "CreditCardType"))).send_keys("Visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        payment_info_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-info-next-step-button")))
        payment_info_continue_button.click()

        # Step 12: Confirm the order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()

        # Step 13: Validate success message
        success_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed-page .title strong")))
        self.assertTrue("successfully processed" in success_message.text)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()