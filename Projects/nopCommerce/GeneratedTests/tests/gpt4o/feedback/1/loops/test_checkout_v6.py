import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Navigate to search page
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Search for a product
        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Add the first result to the cart
        add_to_cart_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "button.product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Go to the shopping cart from the success notification
        cart_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "shopping cart")))
        cart_link.click()

        # Proceed to checkout
        terms_of_service_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        if not terms_of_service_checkbox.is_selected():
            terms_of_service_checkbox.click()
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Checkout as Guest
        checkout_as_guest_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Fill out billing form
        wait.until(EC.presence_of_element_located((By.ID, "opc-billing")))
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email@example.com")
        country_select = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        country_select.click()
        country_select.find_element(By.XPATH, "//option[@value='237']").click()
        state_select = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        state_select.click()
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        next_step_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        next_step_button.click()

        # Shipping method
        wait.until(EC.presence_of_element_located((By.ID, "opc-shipping_method")))
        shipping_option = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input#shippingoption_1")))
        if not shipping_option.is_selected():
            shipping_option.click()
        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()

        # Payment method
        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_method")))
        payment_option = driver.find_element(By.CSS_SELECTOR, "input#paymentmethod_1")
        if not payment_option.is_selected():
            payment_option.click()
        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()

        # Payment information
        wait.until(EC.presence_of_element_located((By.ID, "opc-payment_info")))
        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Confirm order
        wait.until(EC.presence_of_element_located((By.ID, "opc-confirm_order")))
        confirm_button = driver.find_element(By.CSS_SELECTOR, ".confirm-order-next-step-button")
        confirm_button.click()

        # Verify order completion
        thank_you_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Thank you']")))
        self.assertTrue(thank_you_message.is_displayed(), "Order completion message not found.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()