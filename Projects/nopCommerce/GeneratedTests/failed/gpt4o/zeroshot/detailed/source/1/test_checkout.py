from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Navigate to the "Search" page
        search_menu = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_menu.click()

        # Step 2: Search for a product
        search_input = wait.until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_input.send_keys("book")
        search_button = driver.find_element(By.CLASS_NAME, "search-button")
        search_button.click()

        # Step 3: Add the first result to the cart
        first_product_add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "product-box-add-to-cart-button"))
        )
        first_product_add_to_cart_button.click()

        # Step 4: Click "shopping cart" in success notification
        shopping_cart_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        shopping_cart_link.click()

        # Step 5: Agree to the terms and proceed to checkout
        terms_of_service_checkbox = wait.until(
            EC.presence_of_element_located((By.ID, "termsofservice"))
        )
        terms_of_service_checkbox.click()

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        checkout_as_guest_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 7: Fill out the billing form
        self.fill_billing_form(wait)

        # Step 8: Proceed through shipping and payment methods
        self.proceed_through_shopping_steps(wait)

        # Step 9: Confirm the order
        confirm_order_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Step 10: Confirm order completion
        thank_you_text = wait.until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Thank you']"))
        )
        self.assertTrue(thank_you_text.is_displayed(), "Order completion message not found.")

    def fill_billing_form(self, wait):
        driver = self.driver

        self.fill_input_field(wait, "BillingNewAddress_FirstName", "Test")
        self.fill_input_field(wait, "BillingNewAddress_LastName", "User")
        self.fill_input_field(wait, "BillingNewAddress_Email", "random_email@test.com")
        self.fill_input_field(wait, "BillingNewAddress_City", "Riga")
        self.fill_input_field(wait, "BillingNewAddress_Address1", "Street 1")
        self.fill_input_field(wait, "BillingNewAddress_ZipPostalCode", "LV-1234")
        self.fill_input_field(wait, "BillingNewAddress_PhoneNumber", "12345678")

        self.select_dropdown_option(wait, "BillingNewAddress_CountryId", "124")
        self.select_dropdown_option(wait, "BillingNewAddress_StateProvinceId", "0")

        continue_button = driver.find_element(By.NAME, "save")
        continue_button.click()

    def proceed_through_shopping_steps(self, wait):
        driver = self.driver

        # Shipping method
        shipping_option = wait.until(
            EC.element_to_be_clickable((By.ID, "shippingoption_1"))
        )
        shipping_option.click()
        shipping_continue_button = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button")
        shipping_continue_button.click()

        # Payment method
        payment_option = wait.until(
            EC.presence_of_element_located((By.ID, "paymentmethod_1"))
        )
        payment_option.click()
        payment_continue_button = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button")
        payment_continue_button.click()

        # Payment information
        self.fill_input_field(wait, "CardholderName", "Test User")
        self.fill_input_field(wait, "CardNumber", "4111111111111111")
        self.select_dropdown_option(wait, "ExpireMonth", "4")
        self.select_dropdown_option(wait, "ExpireYear", "2027")
        self.fill_input_field(wait, "CardCode", "123")

        payment_info_continue_button = driver.find_element(By.CLASS_NAME, "payment-info-next-step-button")
        payment_info_continue_button.click()

    def fill_input_field(self, wait, field_id, value):
        element = wait.until(
            EC.presence_of_element_located((By.ID, field_id))
        )
        element.clear()
        element.send_keys(value)

    def select_dropdown_option(self, wait, select_id, value):
        element = wait.until(
            EC.presence_of_element_located((By.ID, select_id))
        )
        for option in element.find_elements(By.TAG_NAME, "option"):
            if option.get_attribute("value") == value:
                option.click()
                break

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()