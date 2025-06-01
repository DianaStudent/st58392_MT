from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestCheckoutFlow(unittest.TestCase):

    def setUp(self):
        # Set up test environment
        self.driver = webdriver.Chrome()
        self.driver.get("http://max/")

    def tearDown(self):
        # Clean up after each test run
        self.driver.quit()

    def test_checkout_flow(self):
        # Step 1: Search for a product and add it to cart
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='searchQuery']"))
        )
        search_input.send_keys("book")

        product_tile_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='product-tile-button']"))
        )
        product_tile_button.click()

        # Step 2: Add product to cart from success notification
        shopping_cart_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart']"))
        )
        shopping_cart_link.click()

        # Step 3: Proceed to checkout as guest
        terms_of_service_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='termsOfService']"))
        )
        terms_of_service_checkbox.click()
        checkout_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button']"))
        )
        checkout_button.click()

        # Step 4: Fill out billing form
        first_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='firstName']"))
        )
        first_name_input.send_keys("Test")

        last_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='lastName']"))
        )
        last_name_input.send_keys("User")

        email_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='email']"))
        )
        email_input.send_keys("random_email@example.com")

        address1_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='address1']"))
        )
        address1_input.send_keys("Street 1")

        city_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='city']"))
        )
        city_input.send_keys("Riga")

        country_id_select = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='countryId']"))
        )
        country_id_select.select_by_value("124")

        state_province_id_select = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='stateProvinceId']"))
        )
        state_province_id_select.select_by_index(0)

        zip_postal_code_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='zipPostalCode']"))
        )
        zip_postal_code_input.send_keys("LV-1234")

        phone_number_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='phoneNumber']"))
        )
        phone_number_input.send_keys("12345678")

        # Step 5: Proceed through shipping method and payment method steps
        shipping_option_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='shipping-option-button']"))
        )
        shipping_option_button.click()

        payment_method_option_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='payment-method-option-button']"))
        )
        payment_method_option_button.click()

        # Step 6: Fill out payment info
        credit_card_type_select = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='creditCardType']"))
        )
        credit_card_type_select.select_by_value("visa")

        cardholder_name_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='cardHolderName']"))
        )
        cardholder_name_input.send_keys("Test User")

        card_number_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='cardNumber']"))
        )
        card_number_input.send_keys("1234567890123456")

        expiration_date_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='expirationDate']"))
        )
        expiration_date_input.send_keys("12/2025")

        cvv_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@name='cvv']"))
        )
        cvv_input.send_keys("123")

        # Step 7: Place order
        place_order_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='place-order-button']"))
        )
        place_order_button.click()

        # Verify successful checkout
        self.assertEqual(self.driver.title, "Order Confirmation")

if __name__ == "__main__":
    unittest.main()