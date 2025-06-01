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

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to Search page
        search_menu = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_menu.click()

        # Search for the "book"
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book")
        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # Add first product to cart
        add_to_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".item-box .button-2.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Click on "shopping cart" link in success notification
        shopping_cart_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "shopping cart")))
        shopping_cart_link.click()

        # Check 'Terms of service' and proceed to checkout
        terms_of_service = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Checkout as Guest
        checkout_as_guest_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.button-1.checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill out Billing form
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email@test.com")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='124']").click()
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        billing_continue_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.new-address-next-step-button")
        billing_continue_button.click()

        # Shipping method
        shipping_method_continue = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.button-1.shipping-method-next-step-button")))
        shipping_method_continue.click()

        # Payment method
        payment_method_option = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method_option.click()
        payment_method_continue = driver.find_element(By.CSS_SELECTOR, "button.button-1.payment-method-next-step-button")
        payment_method_continue.click()

        # Payment info
        driver.find_element(By.ID, "CreditCardType").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='visa']").click()
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='4']").click()
        driver.find_element(By.ID, "ExpireYear").click()
        driver.find_element(By.CSS_SELECTOR, "option[value='2027']").click()
        driver.find_element(By.ID, "CardCode").send_keys("123")
        payment_info_continue = driver.find_element(By.CSS_SELECTOR, "button.button-1.payment-info-next-step-button")
        payment_info_continue.click()

        # Confirm order
        confirm_order_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button.button-1.confirm-order-next-step-button")))
        confirm_order_button.click()

        # Verify order completion
        thank_you_text = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "page-title")))
        self.assertTrue("Thank you" in thank_you_text.text, "Order completion failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()