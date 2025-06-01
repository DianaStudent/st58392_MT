from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 2: Navigate to the "Search" page
        search_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".top-menu.notmobile a[href='/search']")))
        search_link.click()

        # Step 3: Look for a product using the query "book"
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".button-1.search-box-button")
        search_button.click()

        # Step 4: Add the first result to the cart
        first_product_add_cart = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        first_product_add_cart.click()

        # Step 5: From the success notification, click the "shopping cart" link
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#bar-notification a[href='/cart']")))
        cart_link.click()

        # Step 6: Check the "Terms of service" checkbox and click the "Checkout" button
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 7: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 8: Fill out the billing form
        self.fill_billing_information()

        # Step 9: Proceed to shipping method
        continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".new-address-next-step-button")))
        continue_button.click()

        # Step 10: Select the shipping method and proceed
        shipping_method_radio = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_method_radio.click()
        continue_button = driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button")
        continue_button.click()

        # Step 11: Select the payment method and proceed
        payment_method_radio = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method_radio.click()
        continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        continue_button.click()

        # Step 12: Fill in payment info and proceed
        self.fill_payment_information()
        continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        continue_button.click()

        # Step 13: Confirm order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()

        # Step 14: Confirm that the order has been completed
        thank_you_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-title h1")))
        self.assertEqual(thank_you_message.text, "Thank you", "Order confirmation message not found or incorrect")

    def fill_billing_information(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email@example.com")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys(Keys.DOWN * 124)
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

    def fill_payment_information(self):
        driver = self.driver
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys(Keys.DOWN * 4)
        driver.find_element(By.ID, "ExpireYear").send_keys(Keys.DOWN * 7)
        driver.find_element(By.ID, "CardCode").send_keys("123")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()