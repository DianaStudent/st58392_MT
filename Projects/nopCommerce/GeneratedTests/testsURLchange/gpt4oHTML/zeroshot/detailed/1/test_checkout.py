from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest
import time

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # Assume the server is hosted locally

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Step 1: Open the homepage
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "master-wrapper-page")))
        
        # Step 2: Navigate to the "Search" page
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Wait for the search page to load
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "search-page")))

        # Search for a product using the query "book"
        search_box = driver.find_element(By.ID, "q")
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 3: Add the first result to the cart
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "products-container")))
        add_to_cart_button = driver.find_elements(By.CLASS_NAME, "product-box-add-to-cart-button")[0]
        add_to_cart_button.click()

        # Step 4: From the success notification, click the "shopping cart" link
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Check if cart is correctly opened
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-page")))

        # Step 5: Check the "Terms of service" checkbox and click the "Checkout" button
        terms_of_service_checkbox = driver.find_element(By.ID, "termsofservice")
        if not terms_of_service_checkbox.is_selected():
            terms_of_service_checkbox.click()

        checkout_button = driver.find_element(By.NAME, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 7: Fill out the full billing form with credentials
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "opc-billing")))

        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email@test.com")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.send_keys(Keys.DOWN)  # Assumes the desired country is first in the list after default

        state_select = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        state_select.send_keys(Keys.DOWN)  # Assumes the desired state/province is first in the list after default

        billing_continue_button = driver.find_element(By.NAME, "save")
        billing_continue_button.click()

        # Step 8: Proceed with the shipping method
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "opc-shipping_method")))
        driver.find_element(By.ID, "shippingoption_1").click()  # Select Next Day Air

        shipping_method_continue_button = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button")
        shipping_method_continue_button.click()

        # Proceed with the payment method
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "opc-payment_method")))
        driver.find_element(By.ID, "paymentmethod_1").click()  # Select Credit Card

        payment_method_continue_button = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button")
        payment_method_continue_button.click()

        # Fill in the payment info
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "opc-payment_info")))
        driver.find_element(By.ID, "CreditCardType").send_keys("Visa")
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        payment_info_continue_button = driver.find_element(By.CLASS_NAME, "payment-info-next-step-button")
        payment_info_continue_button.click()

        # Step 9: Confirm order
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "opc-confirm_order")))

        confirm_order_button = driver.find_element(By.CLASS_NAME, "confirm-order-next-step-button")
        confirm_order_button.click()

        # Step 10: Confirm the order completion
        thank_you_header = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "page-title")))
        thank_you_text = thank_you_header.text
        self.assertEqual(thank_you_text, "Thank you")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()