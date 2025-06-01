import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Step 2: Navigate to the "Search" page and search for a "book"
        driver.find_element(By.LINK_TEXT, "Search").click()
        
        search_box = self.wait.until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_box.send_keys("book")
        search_box.send_keys(Keys.ENTER)

        # Step 3: Add the first result to the cart
        add_to_cart_button = self.wait.until(
            EC.visibility_of_element_located((
                By.CSS_SELECTOR, ".product-box-add-to-cart-button"
            ))
        )
        add_to_cart_button.click()

        # Step 4: Click the "shopping cart" link from the success notification
        shopping_cart_link = self.wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        shopping_cart_link.click()

        # Step 5: Check the "Terms of service" checkbox and click "Checkout"
        terms_of_service_checkbox = self.wait.until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_of_service_checkbox.click()

        checkout_button = self.wait.until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = self.wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 7: Fill out the billing form
        self.wait.until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
        ).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("user_zz18872z@test.com")
        driver.find_element(By.ID, "BillingNewAddress_Company").send_keys("")
        driver.find_element(By.XPATH, "//select[@id='BillingNewAddress_CountryId']/option[@value='124']").click()
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        billing_continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        billing_continue_button.click()

        # Step 8: Proceed through following steps
        shipping_continue_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button"))
        )
        shipping_continue_button.click()

        payment_method_radio = self.wait.until(
            EC.presence_of_element_located((By.ID, "paymentmethod_1"))
        )
        payment_method_radio.click()

        payment_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_button.click()

        # Fill payment info details
        self.wait.until(
            EC.presence_of_element_located((By.ID, "CardholderName"))
        ).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.XPATH, "//select[@id='ExpireMonth']/option[@value='4']").click()
        driver.find_element(By.XPATH, "//select[@id='ExpireYear']/option[@value='2027']").click()
        driver.find_element(By.ID, "CardCode").send_keys("123")

        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue_button.click()

        # Step 9: Confirm the order
        confirm_order_button = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Step 10: Assert the order completion
        thank_you_message = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Thank you']"))
        )
        self.assertIn("Thank you", thank_you_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()