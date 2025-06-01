from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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

    def test_checkout_process(self):
        driver = self.driver

        # Step 2: Click on the "Search" link and search for a product (e.g. "book").
        search_link = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Search"))
        )
        search_link.click()

        search_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "q"))
        )
        search_input.send_keys("book")

        search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-button")
        search_button.click()

        # Step 3: Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 4: Open the shopping cart via the success notification popup.
        success_notification = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".bar-notification-container"))
        )
        cart_link = success_notification.find_element(By.LINK_TEXT, "shopping cart")
        cart_link.click()

        # Ensure cart page loads
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".page-title h1"))
        )

        # Step 5: Accept terms of service and click the "Checkout" button.
        terms_checkbox = driver.find_element(By.ID, "termsofservice")
        driver.execute_script("arguments[0].click();", terms_checkbox)  # Checkbox sometimes requires JS click

        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest".
        checkout_as_guest_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 7: Fill in the billing address.
        fields = {
            "BillingNewAddress_FirstName": "Test",
            "BillingNewAddress_LastName": "User",
            "BillingNewAddress_Email": "random_email",
            "BillingNewAddress_CountryId": "124",
            "BillingNewAddress_City": "Riga",
            "BillingNewAddress_Address1": "Street 1",
            "BillingNewAddress_ZipPostalCode": "LV-1234",
            "BillingNewAddress_PhoneNumber": "12345678",
            "BillingNewAddress_StateProvinceId": "0"
        }

        for field, value in fields.items():
            input_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, field))
            )
            if input_element.tag_name == "select":
                webdriver.support.ui.Select(input_element).select_by_value(value)
            else:
                input_element.clear()
                input_element.send_keys(value)

        continue_button = driver.find_element(By.CSS_SELECTOR, ".new-address-next-step-button")
        continue_button.click()

        # Step 8: Select shipping and payment methods.
        shipping_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#shippingoption_1"))
        )
        shipping_option.click()

        driver.find_element(By.CSS_SELECTOR, ".shipping-method-next-step-button").click()

        payment_method_option = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#paymentmethod_1"))
        )
        payment_method_option.click()

        driver.find_element(By.CSS_SELECTOR, ".payment-method-next-step-button").click()

        # Step 9: Enter credit card details.
        credit_card_fields = {
            "CardholderName": "Test User",
            "CardNumber": "4111111111111111",
            "ExpireMonth": "4",
            "ExpireYear": "2027",
            "CardCode": "123"
        }
        
        for field, value in credit_card_fields.items():
            input_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, field))
            )
            input_element.clear()
            input_element.send_keys(value)
        
        driver.find_element(By.CSS_SELECTOR, ".payment-info-next-step-button").click()

        # Step 10: Confirm the order.
        confirm_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-order-next-step-button"))
        )
        confirm_button.click()

        # Step 11: Validate that the confirmation message or success section is visible.
        confirmation_message = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".order-completed-page .title"))
        )

        self.assertTrue("Your order has been successfully processed!" in confirmation_message.text)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()