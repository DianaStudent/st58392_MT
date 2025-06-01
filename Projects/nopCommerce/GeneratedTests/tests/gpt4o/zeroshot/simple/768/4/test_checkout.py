from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Search for a product
        search_input = wait.until(
            EC.presence_of_element_located((By.ID, "small-searchterms"))
        )
        search_input.send_keys("book")
        
        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Step 2: Add the first book to the cart
        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-box-add-to-cart-button"))
        )
        add_to_cart_button.click()

        # Step 3: Click "shopping cart" from the success popup
        go_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "shopping cart"))
        )
        go_to_cart_button.click()

        # Step 4: Checkout as guest
        checkout_as_guest_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "checkout-as-guest-button"))
        )
        checkout_as_guest_button.click()

        # Step 5: Fill Billing details
        first_name_input = wait.until(
            EC.presence_of_element_located((By.ID, "BillingNewAddress_FirstName"))
        )
        last_name_input = driver.find_element(By.ID, "BillingNewAddress_LastName")
        email_input = driver.find_element(By.ID, "BillingNewAddress_Email")
        country_dropdown = driver.find_element(By.ID, "BillingNewAddress_CountryId")
        state_dropdown = driver.find_element(By.ID, "BillingNewAddress_StateProvinceId")
        city_input = driver.find_element(By.ID, "BillingNewAddress_City")
        address1_input = driver.find_element(By.ID, "BillingNewAddress_Address1")
        zip_input = driver.find_element(By.ID, "BillingNewAddress_ZipPostalCode")
        phone_input = driver.find_element(By.ID, "BillingNewAddress_PhoneNumber")

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("random_email")
        country_dropdown.send_keys(Keys.ARROW_DOWN)
        state_dropdown.send_keys("Other")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_input.send_keys("LV-1234")
        phone_input.send_keys("12345678")

        continue_button_1 = driver.find_element(By.NAME, "save")
        continue_button_1.click()

        # Step 6: Select shipping option
        next_day_air_option = wait.until(
            EC.element_to_be_clickable((By.ID, "shippingoption_1"))
        )
        next_day_air_option.click()

        continue_button_2 = driver.find_element(By.CLASS_NAME, "shipping-method-next-step-button")
        continue_button_2.click()

        # Step 7: Select payment method
        credit_card_option = wait.until(
            EC.element_to_be_clickable((By.ID, "paymentmethod_1"))
        )
        credit_card_option.click()

        continue_button_3 = driver.find_element(By.CLASS_NAME, "payment-method-next-step-button")
        continue_button_3.click()

        # Step 8: Enter payment information
        card_type_dropdown = wait.until(
            EC.presence_of_element_located((By.ID, "CreditCardType"))
        )
        cardholder_name_input = driver.find_element(By.ID, "CardholderName")
        card_number_input = driver.find_element(By.ID, "CardNumber")
        expire_month_dropdown = driver.find_element(By.ID, "ExpireMonth")
        expire_year_dropdown = driver.find_element(By.ID, "ExpireYear")
        card_code_input = driver.find_element(By.ID, "CardCode")

        card_type_dropdown.send_keys("Visa")
        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("4111111111111111")
        expire_month_dropdown.send_keys("04")
        expire_year_dropdown.send_keys("2027")
        card_code_input.send_keys("123")

        continue_button_4 = driver.find_element(By.CLASS_NAME, "payment-info-next-step-button")
        continue_button_4.click()

        # Step 9: Confirm the order
        confirm_order_button = wait.until(
            EC.element_to_be_clickable((By.CLASS_NAME, "confirm-order-next-step-button"))
        )
        confirm_order_button.click()

        # Step 10: Check for order completion message
        try:
            wait.until(
                EC.text_to_be_present_in_element((By.CLASS_NAME, "title"), "Your order has been successfully processed!")
            )
        except:
            self.fail("Order completion message not found")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()