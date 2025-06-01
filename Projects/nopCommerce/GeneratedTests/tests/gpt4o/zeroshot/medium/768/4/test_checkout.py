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
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_checkout_process(self):
        driver = self.driver

        # Click on "Search" link
        search_link = self.wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Search for a product
        search_input = self.wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.send_keys("book")
        search_input.send_keys(Keys.RETURN)

        # Add the first product to cart
        add_to_cart_button = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Open the shopping cart from the success notification
        success_popup = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        cart_link = success_popup.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Accept terms of service and proceed to checkout
        self.wait.until(EC.presence_of_element_located((By.ID, "termsofservice"))).click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Checkout as Guest
        checkout_as_guest_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing address
        self.wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        # Continue to shipping method
        billing_continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        billing_continue_button.click()

        # Select shipping method
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))).click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()

        # Select payment method
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1"))).click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()

        # Enter payment information
        self.wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")

        # Continue to confirm order
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Confirm order
        confirm_order_button = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()

        # Validate order completion
        thank_you_message = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed-page .title")))
        self.assertTrue("Your order has been successfully processed!" in thank_you_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()