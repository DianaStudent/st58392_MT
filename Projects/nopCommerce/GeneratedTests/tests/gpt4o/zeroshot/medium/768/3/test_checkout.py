import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://max/')

    def test_user_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Click on the "Search" link
        search_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Search")))
        search_link.click()

        # Step 2: Search for a product ("book")
        search_box = wait.until(EC.presence_of_element_located((By.ID, "small-searchterms")))
        search_box.send_keys("book")
        search_box.send_keys(Keys.RETURN)

        # Step 3: Click the "Add to cart" for the first item
        add_to_cart_buttons = wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".button-2.product-box-add-to-cart-button")))
        if not add_to_cart_buttons:
            self.fail("Add to cart buttons not found")
        add_to_cart_buttons[0].click()

        # Step 4: Open the shopping cart via the success notification popup
        success_notification = wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".bar-notification.success .content a")))
        success_notification.click()

        # Step 5: Accept terms and click "Checkout"
        terms_checkbox = wait.until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_checkbox.click()

        checkout_button = wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # Step 7: Fill in the billing address
        wait.until(EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))).send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")

        billing_continue_button = driver.find_element(
            By.CSS_SELECTOR, ".new-address-next-step-button")
        billing_continue_button.click()

        # Step 8: Select shipping method
        shipping_option = wait.until(EC.presence_of_element_located((By.ID, "shippingoption_1")))
        shipping_option.click()
        shipping_continue_button = driver.find_element(
            By.CSS_SELECTOR, ".shipping-method-next-step-button")
        shipping_continue_button.click()

        # Step 9: Select payment method and enter details
        payment_method = wait.until(EC.presence_of_element_located((By.ID, "paymentmethod_1")))
        payment_method.click()

        payment_continue_button = driver.find_element(
            By.CSS_SELECTOR, ".payment-method-next-step-button")
        payment_continue_button.click()

        wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        payment_info_continue_button = driver.find_element(
            By.CSS_SELECTOR, ".payment-info-next-step-button")
        payment_info_continue_button.click()

        # Step 10: Confirm the order
        confirm_order_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()

        # Step 11: Validate success message
        success_message = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, ".order-completed .title")))
        self.assertTrue("Your order has been successfully processed!" in success_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()