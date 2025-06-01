import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page
        try:
            search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        except:
            self.fail("Search link not found on the home page.")

        # 2. Click on the "Search" link and search for a product (e.g. "book")
        search_link.click()
        try:
            search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        except:
            self.fail("Search box or button not found on the search page.")

        search_box.send_keys("book")
        search_button.click()

        # 3. Click the "Add to cart" button for the first item in the search results
        try:
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button")))
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found.")

        # 4. Open the shopping cart via the success notification popup
        try:
            success_popup = wait.until(EC.visibility_of_element_located((By.ID, "bar-notification")))
            cart_link = success_popup.find_element(By.LINK_TEXT, "shopping cart")
            cart_link.click()
        except:
            self.fail("Success notification popup or cart link not found.")

        # 5. Accept terms of service and click the "Checkout" button
        try:
            terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
            checkout_button = driver.find_element(By.ID, "checkout")
        except:
            self.fail("Terms and conditions checkbox or checkout button not found in the cart.")

        terms_checkbox.click()
        checkout_button.click()

        # 6. Choose "Checkout as Guest"
        try:
            guest_checkout_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.checkout-as-guest-button")))
            guest_checkout_button.click()
        except:
            self.fail("Checkout as Guest button not found.")

        # 7. Fill in the billing address
        try:
            driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
            driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
            driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
            driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
            driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
            driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
            driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
            driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
            billing_continue_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.new-address-next-step-button")
            billing_continue_button.click()
        except:
            self.fail("Billing address form elements not found or not interactable.")

        # 8. Select shipping and payment methods
        try:
            shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
            shipping_option.click()
            shipping_continue_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.shipping-method-next-step-button")
            shipping_continue_button.click()
        except:
            self.fail("Shipping method selection failed.")

        try:
            payment_option = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
            payment_option.click()
            payment_continue_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.payment-method-next-step-button")
            payment_continue_button.click()
        except:
            self.fail("Payment method selection failed.")

        # 9. Enter credit card details
        try:
            driver.find_element(By.ID, "CardholderName").send_keys("Test User")
            driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
            driver.find_element(By.ID, "ExpireMonth").send_keys("4")
            driver.find_element(By.ID, "ExpireYear").send_keys("2027")
            driver.find_element(By.ID, "CardCode").send_keys("123")
            payment_info_continue = driver.find_element(By.CSS_SELECTOR, "button.button-1.payment-info-next-step-button")
            payment_info_continue.click()
        except:
            self.fail("Entering payment information failed.")

        # 10. Confirm the order
        try:
            confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.button-1.confirm-order-next-step-button")))
            confirm_order_button.click()
        except:
            self.fail("Confirm order button not found.")

        # 11. Validate that the confirmation message or success section is visible
        try:
            confirmation_message = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-completed .title strong")))
            self.assertTrue(confirmation_message.is_displayed(), "Order confirmation message not displayed.")
        except:
            self.fail("Order confirmation message not found or not displayed.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()