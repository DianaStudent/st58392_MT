from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Navigate to the "Search" page and look for a product using the query "book"
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, ".search-button")
        search_button.click()

        # Step 3: Add the first result to the cart using a product tile button
        add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Step 4: From the success notification, click the "shopping cart" link
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Step 5: Check the "Terms of service" checkbox and click the "Checkout" button
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        guest_checkout_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        guest_checkout_button.click()

        # Step 7: Fill out the full billing form
        def fill_billing_form(field_id, value):
            element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            element.clear()
            element.send_keys(value)

        fill_billing_form("BillingNewAddress_FirstName", "Test")
        fill_billing_form("BillingNewAddress_LastName", "User")
        fill_billing_form("BillingNewAddress_Email", "random_email@test.com")
        fill_billing_form("BillingNewAddress_City", "Riga")
        fill_billing_form("BillingNewAddress_Address1", "Street 1")
        fill_billing_form("BillingNewAddress_ZipPostalCode", "LV-1234")
        fill_billing_form("BillingNewAddress_PhoneNumber", "12345678")

        country_element = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_element.send_keys("Latvia")

        state_element = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        state_element.send_keys("Other")

        billing_continue = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".new-address-next-step-button")))
        billing_continue.click()

        # Step 8: Proceed through shipping, payment method, payment information
        shipping_continue = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".shipping-method-next-step-button")))
        shipping_continue.click()

        payment_method = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method.click()
        payment_method_continue = driver.find_element(By.NAME, "save")
        payment_method_continue.click()

        def fill_payment_info(field_id, value):
            element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            element.clear()
            element.send_keys(value)

        fill_payment_info("CardholderName", "Test User")
        fill_payment_info("CardNumber", "4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        fill_payment_info("CardCode", "123")

        payment_info_continue = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".payment-info-next-step-button")))
        payment_info_continue.click()

        # Step 9: On the confirm step, click "Confirm" and wait for the success message
        confirm_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_button.click()

        # Step 10: Confirm that the order has been completed by checking
        thank_you_text = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1")))
        self.assertEqual(thank_you_text.text, "Thank you")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()