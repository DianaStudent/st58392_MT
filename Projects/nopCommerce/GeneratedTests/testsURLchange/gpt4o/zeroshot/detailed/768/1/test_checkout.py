import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_user_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the Search page
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search"))).click()

        # Enter search query and submit
        search_input = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".search-box-button")
        search_button.click()

        # Add first search result to the cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to shopping cart from success notification
        wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart"))).click()

        # Accept terms and proceed to checkout
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = driver.find_element(By.CSS_SELECTOR, ".checkout-button")
        checkout_button.click()

        # Checkout as guest
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button"))).click()

        # Fill billing form
        wait.until(EC.presence_of_element_located((By.ID, "co-billing-form")))
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("user_zz18872z@test.com")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")

        # Click "Continue"
        billing_continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        billing_continue_button.click()

        # Select shipping method and continue
        wait.until(EC.presence_of_element_located((By.ID, "opc-shipping_method")))
        driver.find_element(By.CSS_SELECTOR, "#shippingoption_1").click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()

        # Select payment method and continue
        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_method")))
        driver.find_element(By.CSS_SELECTOR, "#paymentmethod_1").click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()

        # Fill payment info and continue
        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_info")))
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Confirm the order
        wait.until(EC.presence_of_element_located((By.ID, "opc-confirm_order")))
        confirm_order_button = driver.find_element(By.CSS_SELECTOR, ".confirm-order-next-step-button")
        confirm_order_button.click()

        # Verify order is completed
        thank_you_text = wait.until(EC.presence_of_element_located((By.TAG_NAME, "h1"))).text
        if not thank_you_text or "Thank you" not in thank_you_text:
            self.fail("Order completion message not found")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()