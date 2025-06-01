import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.top-menu.notmobile > li > a[href='/']")))

        # 2. Click on the "Search" link and search for a product (e.g. "book")
        search_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ul.top-menu.notmobile > li > a[href='/search']")))
        search_link.click()

        search_box = wait.until(EC.presence_of_element_located((By.ID, "q")))
        search_box.send_keys("book", Keys.ENTER)

        # 3. Click the "Add to cart" button for the first item in the search results
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button")))
        add_to_cart_btn.click()

        # 4. Open the shopping cart via the success notification popup
        success_notification = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification.success")))
        cart_link = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".bar-notification.success a[href='/cart']")))
        cart_link.click()

        # 5. Accept terms of service and click the "Checkout" button
        terms_of_service_checkbox = wait.until(EC.element_to_be_clickable((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()

        checkout_button = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
        checkout_button.click()

        # 6. Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button")))
        checkout_as_guest_button.click()

        # 7. Fill in the billing address
        driver.find_element(By.ID, "BillingNewAddress_FirstName").send_keys("Test")
        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_StateProvinceId").send_keys("Other")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        billing_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".new-address-next-step-button")))
        billing_continue_button.click()

        # 8. Select shipping and payment methods
        shipping_option = wait.until(EC.element_to_be_clickable((By.ID, "shippingoption_1")))
        shipping_option.click()

        shipping_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".shipping-method-next-step-button")))
        shipping_continue_button.click()

        payment_method = wait.until(EC.element_to_be_clickable((By.ID, "paymentmethod_1")))
        payment_method.click()

        payment_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-method-next-step-button")))
        payment_continue_button.click()

        # 9. Enter credit card details
        wait.until(EC.presence_of_element_located((By.ID, "CardholderName"))).send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("4")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        payment_info_continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".payment-info-next-step-button")))
        payment_info_continue_button.click()

        # 10. Confirm the order
        confirm_order_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button")))
        confirm_order_button.click()

        # 11. Validate that the confirmation message or success section is visible
        confirmation_message = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".order-completed-page .title")))

        if not confirmation_message:
            self.fail("Confirmation message not visible")

if __name__ == "__main__":
    unittest.main()