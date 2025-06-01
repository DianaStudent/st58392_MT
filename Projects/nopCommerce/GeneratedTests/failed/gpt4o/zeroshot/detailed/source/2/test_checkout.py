from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to "Search" page
        search_menu = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Search")))
        search_menu.click()

        # Search for "book"
        search_input = wait.until(EC.element_to_be_clickable((By.ID, "q")))
        search_input.send_keys("book")
        search_btn = driver.find_element(By.CLASS_NAME, "search-button")
        search_btn.click()

        # Add the first result to the cart
        add_to_cart_btn = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_btn.click()

        # Click "shopping cart" link in the success notification
        cart_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Accept terms and conditions and proceed to checkout
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_btn = driver.find_element(By.ID, "checkout")
        checkout_btn.click()

        # Choose "Checkout as Guest"
        checkout_as_guest_btn = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "checkout-as-guest-button")))
        checkout_as_guest_btn.click()

        # Fill out billing form
        wait.until(EC.element_to_be_clickable((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("user_zz18872z@test.com")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.find_element(By.CSS_SELECTOR, "option[value='124']").click()

        # Continue to shipping method
        billing_continue_btn = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        billing_continue_btn.click()

        # Continue from shipping method page
        shipping_continue_btn = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".shipping-method-next-step-button")))
        shipping_continue_btn.click()

        # Choose payment method and continue
        payment_method_radiobtn = wait.until(EC.presence_of_element_located(
            (By.ID, "paymentmethod_1")))
        payment_method_radiobtn.click()
        payment_continue_btn = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_btn.click()

        # Fill payment info, if required
        wait.until(EC.element_to_be_clickable((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").find_element(By.CSS_SELECTOR, "option[value='4']").click()
        driver.find_element(By.ID, "ExpireYear").find_element(By.CSS_SELECTOR, "option[value='2027']").click()
        driver.find_element(By.ID, "CardCode").send_keys("123")

        # Continue to confirm order
        payment_info_continue_btn = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue_btn.click()

        # Confirm order
        confirm_btn = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_btn.click()

        # Check for order completion message
        thank_you_msg = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='page-title']/h1")))
        self.assertEqual(thank_you_msg.text, "Thank you", "Order was not completed successfully.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()