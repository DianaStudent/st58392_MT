import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.set_window_size(1920, 1080)

    def test_checkout_process(self):
        driver = self.driver

        # Step 1: Navigate to Search and look for "book"
        search_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Search"))
        )
        search_link.click()

        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_input.send_keys("book")

        search_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.search-box-button"))
        )
        search_button.click()

        # Step 2: Add the first product to cart
        add_to_cart_buttons = WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.button-2.product-box-add-to-cart-button"))
        )
        if not add_to_cart_buttons:
            self.fail("Add to cart button not found!")
        add_to_cart_buttons[0].click()

        # Step 3: Navigate to shopping cart from the success notification
        cart_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        cart_link.click()

        # Step 4: Agree to terms and proceed to checkout
        terms_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_checkbox.click()

        checkout_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        # Step 5: Checkout as Guest
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 6: Fill billing information
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
        ).send_keys("Test")

        driver.find_element(By.ID, "BillingNewAddress_LastName").send_keys("User")
        driver.find_element(By.ID, "BillingNewAddress_Email").send_keys("random_email@test.com")
        driver.find_element(By.ID, "BillingNewAddress_CountryId").send_keys("Latvia")
        driver.find_element(By.ID, "BillingNewAddress_City").send_keys("Riga")
        driver.find_element(By.ID, "BillingNewAddress_Address1").send_keys("Street 1")
        driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode").send_keys("LV-1234")
        driver.find_element(By.ID, "BillingNewAddress_PhoneNumber").send_keys("12345678")

        billing_continue_button = driver.find_element(By.CSS_SELECTOR, "button.new-address-next-step-button")
        billing_continue_button.click()

        # Step 7: Continue through Shipping method
        shipping_continue_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.shipping-method-next-step-button"))
        )
        shipping_continue_button.click()

        # Step 8: Select Payment method
        payment_method_radio = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "paymentmethod_1"))
        )
        payment_method_radio.click()

        payment_method_continue_button = driver.find_element(By.CSS_SELECTOR, "button.payment-method-next-step-button")
        payment_method_continue_button.click()

        # Step 9: Fill Payment information
        card_type_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "CreditCardType"))
        )
        card_type_select.send_keys("Visa")

        driver.find_element(By.ID, "CardholderName").send_keys("Test User")
        driver.find_element(By.ID, "CardNumber").send_keys("4111111111111111")
        driver.find_element(By.ID, "ExpireMonth").send_keys("04")
        driver.find_element(By.ID, "ExpireYear").send_keys("2027")
        driver.find_element(By.ID, "CardCode").send_keys("123")

        payment_info_continue_button = driver.find_element(By.CSS_SELECTOR, "button.payment-info-next-step-button")
        payment_info_continue_button.click()

        # Step 10: Confirm Order
        confirm_order_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Check for order completion
        confirmation_text = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "page-title"))
        ).text
        self.assertEqual(confirmation_text, "Thank you")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()