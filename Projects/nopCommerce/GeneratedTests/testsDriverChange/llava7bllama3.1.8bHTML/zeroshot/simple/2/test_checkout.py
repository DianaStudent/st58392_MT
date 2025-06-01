import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestOrderCompletion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_order_completion(self):
        # Navigate to the website
        self.driver.get("http://max/")

        # Search for a product (e.g. "book")
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-input")))
        search_input.send_keys("book")
        search_input.send_keys(Keys.RETURN)

        # Add the product to cart
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Add to Cart']")))
        add_to_cart_button.click()

        # Click "shopping cart" from the success popup
        shopping_cart_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "shopping-cart-button")))
        shopping_cart_button.click()

        # Use the "Checkout as Guest" option
        checkout_as_guest_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Checkout as Guest']")))
        checkout_as_guest_link.click()

        # Fill out guest information form
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "firstName")))
        first_name_input.send_keys("Test")
        
        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "lastName")))
        last_name_input.send_keys("User")

        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        email_input.send_keys("random_email")

        city_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "city")))
        city_input.send_keys("Riga")

        address1_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "address1")))
        address1_input.send_keys("Street 1")

        zip_postal_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "zipPostalCode")))
        zip_postal_code_input.send_keys("LV-1234")

        phone_number_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "phoneNumber")))
        phone_number_input.send_keys("12345678")

        country_id_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "countryId")))
        country_id_input.send_keys("124")

        state_province_id_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "stateProvinceId")))
        state_province_id_input.send_keys("0")

        # Select shipping option
        shipping_option_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@id='shippingOption']")))
        shipping_option_select.click()
        shipping_option_option = self.driver.find_element(By.XPATH, "//option[text()='Shipping Option 1']")
        shipping_option_option.click()

        # Select payment method
        payment_method_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@id='paymentMethodOption']")))
        payment_method_select.click()
        payment_method_option = self.driver.find_element(By.XPATH, "//option[text()='Payment Method Option 1']")
        payment_method_option.click()

        # Fill out credit card information
        credit_card_type_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "creditCardType")))
        credit_card_type_input.send_keys("visa")

        cardholder_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cardHolderName")))
        cardholder_name_input.send_keys("Test User")

        card_number_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cardNumber")))
        card_number_input.send_keys("4111111111111111")

        expire_month_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "expireMonth")))
        expire_month_input.send_keys("4")

        expire_year_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "expireYear")))
        expire_year_input.send_keys("2027")

        card_cvv_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cardCVV")))
        card_cvv_input.send_keys("123")

        # Place order
        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))
        place_order_button.click()

        # Check for order confirmation message
        order_confirmation_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[text()='Order Confirmation Message']")))
        self.assertTrue(order_confirmation_message.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()