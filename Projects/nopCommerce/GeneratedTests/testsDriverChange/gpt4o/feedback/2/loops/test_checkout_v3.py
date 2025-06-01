import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_checkout(self):
        driver = self.driver
        wait = self.wait

        # Navigate to the "Search" page
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Use search box to search for "book"
        search_input = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_input.send_keys("book" + Keys.ENTER)

        # Add first product to cart
        add_to_cart_button = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".product-item button.product-box-add-to-cart-button")))
        add_to_cart_button.click()

        # Go to cart via success notification
        cart_link = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".bar-notification a[href='/cart']")))
        cart_link.click()

        # Agree to terms and proceed to checkout
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()
        checkout_button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

        # Checkout as guest
        checkout_as_guest_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Fill billing form
        wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("user_zz18872z@test.com")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        # Select country and state
        country_dropdown = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_CountryId")))
        country_dropdown.find_element(By.CSS_SELECTOR, "option[value='124']").click()
        region_dropdown = wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_StateProvinceId")))
        region_dropdown.find_element(By.CSS_SELECTOR, "option[value='0']").click()

        # Continue to shipping method
        driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button").click()

        # Select shipping method
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#shippingoption_1"))).click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()

        # Select payment method
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#paymentmethod_1"))).click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()

        # Enter payment information
        wait.until(EC.presence_of_element_located((By.ID, "CreditCardType"))).find_element(By.CSS_SELECTOR, "option[value='visa']").click()
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").find_element(By.CSS_SELECTOR, "option[value='4']").click()
        driver.find_element(By.ID, "ExpireYear").find_element(By.CSS_SELECTOR, "option[value='2027']").click()
        driver.find_element(By.ID, "CardCode").send_keys("123")

        # Continue to order confirmation
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Confirm order
        confirm_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_button.click()

        # Verify order completion
        thank_you_text = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Thank you']")))
        if not thank_you_text:
            self.fail("Order completion was not confirmed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()