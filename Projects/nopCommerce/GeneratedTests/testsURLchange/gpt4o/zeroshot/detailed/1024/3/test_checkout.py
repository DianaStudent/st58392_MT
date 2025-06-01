import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the homepage
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'master-wrapper-page')))

        # 2. Click the "Search" menu item
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Search')))
        search_link.click()

        # 3. Perform a search for "book"
        search_input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, 'button-1.search-button')
        search_button.click()

        # 4. Add the first result to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'product-box-add-to-cart-button')))
        add_to_cart_button.click()

        # 5. Click the "shopping cart" link in the success notification
        cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'shopping cart')))
        cart_link.click()

        # 6. Check the "Terms of service" checkbox and proceed to checkout
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, 'termsofservice')))
        terms_checkbox.click()
        checkout_button = driver.find_element(By.ID, 'checkout')
        checkout_button.click()

        # 7. Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'checkout-as-guest-button')))
        checkout_as_guest_button.click()

        # 8. Fill in the billing form with credentials
        wait.until(EC.presence_of_element_located((By.ID, 'opc-billing')))
        driver.find_element(By.ID, 'BillingNewAddress_FirstName').send_keys('Test')
        driver.find_element(By.ID, 'BillingNewAddress_LastName').send_keys('User')
        driver.find_element(By.ID, 'BillingNewAddress_Email').send_keys('random_email')
        driver.find_element(By.ID, 'BillingNewAddress_City').send_keys('Riga')
        driver.find_element(By.ID, 'BillingNewAddress_Address1').send_keys('Street 1')
        driver.find_element(By.ID, 'BillingNewAddress_ZipPostalCode').send_keys('LV-1234')
        driver.find_element(By.ID, 'BillingNewAddress_PhoneNumber').send_keys('12345678')

        country_dropdown = driver.find_element(By.ID, 'BillingNewAddress_CountryId')
        country_dropdown.find_element(By.CSS_SELECTOR, "[value='124']").click()

        driver.find_element(By.CLASS_NAME, 'new-address-next-step-button').click()

        # 9. Proceed through Shipping, Payment method, and Payment information steps
        shipping_method_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'shipping-method-next-step-button')))
        shipping_method_continue_button.click()

        payment_method_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'payment-method-next-step-button')))
        driver.find_element(By.CSS_SELECTOR, '#paymentmethod_1').click()
        payment_method_continue_button.click()

        payment_info_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'payment-info-next-step-button')))
        driver.find_element(By.ID, 'CardholderName').send_keys('Test User')
        driver.find_element(By.ID, 'CardNumber').send_keys('4111111111111111')
        driver.find_element(By.ID, 'CardCode').send_keys('123')

        driver.find_element(By.ID, 'ExpireMonth').find_element(By.CSS_SELECTOR, "[value='4']").click()
        driver.find_element(By.ID, 'ExpireYear').find_element(By.CSS_SELECTOR, "[value='2027']").click()
        payment_info_continue_button.click()

        # 10. Confirm the order and check for success
        confirm_order_continue_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'confirm-order-next-step-button')))
        confirm_order_continue_button.click()

        # 11. Confirm that the order has been completed
        confirmation_message = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))
        self.assertEqual(confirmation_message.text, "Thank you")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()