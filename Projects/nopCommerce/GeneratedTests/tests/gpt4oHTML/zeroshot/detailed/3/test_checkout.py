import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.get("http://max")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the "Search" page
        search_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".header-menu a[href='/search']")))
        search_link.click()

        # Search for a product using the query "book"
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-button")
        search_input.send_keys("book")
        search_button.click()

        # Add the first search result to the cart
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # From the success notification, click the "shopping cart" link
        cart_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#bar-notification .content a[href='/cart']")))
        cart_link.click()

        # Check the "Terms of service" checkbox and click the "Checkout" button
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill out the billing form
        wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_StateProvinceId").send_keys("Other")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        # Click "Continue"
        billing_continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        billing_continue_button.click()

        # Select a shipping method and proceed
        shipping_option = wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_option.click()
        shipping_continue_button = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        shipping_continue_button.click()

        # Select a payment method and proceed
        payment_option = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_option.click()
        payment_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_button.click()

        # Fill in payment information
        credit_card_type = wait.until(EC.presence_of_element_located((By.ID, "CreditCardType")))
        credit_card_type.send_keys("Visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        # Click continue
        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue_button.click()

        # Confirm the order
        confirm_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_button.click()

        # Check for confirmation text "Thank you"
        thank_you_text = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed-page .page-title h1"))
        ).text
        if thank_you_text != "Thank you":
            self.fail("Order did not complete successfully. 'Thank you' message not found.") 


if __name__ == "__main__":
    unittest.main()