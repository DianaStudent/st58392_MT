import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutFlow(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")  # replace with your homepage URL

    def test_checkout_flow(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='q']")))
        search_box = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='q']")))
        search_box.send_keys("book")
        search_button = self.driver.find_element(By.CSS_SELECTOR, "#searchsubmit")
        search_button.click()

        # Add first product to cart
        product_tile_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-tile-button")))
        product_tile_buttons[0].click()

        # Click shopping cart from success popup
        shopping_cart_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Shopping Cart")))
        shopping_cart_link.click()

        # Check out as guest
        checkout_as_guest_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#checkout-as-guest")))
        checkout_as_guest_button.click()

        # Fill full billing form
        first_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "firstName")))
        last_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "lastName")))
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        address_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "address1")))
        city_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "city")))
        country_id_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#countryId option[value='124']")))
        state_province_id_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#stateProvinceId option[value='0']")))
        zip_postal_code_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "zipPostalCode")))
        phone_number_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "phoneNumber")))

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        email_field.send_keys("random_email")
        address_field.send_keys("Street 1")
        city_field.send_keys("Riga")
        country_id_select.click()
        state_province_id_select.click()
        zip_postal_code_field.send_keys("LV-1234")
        phone_number_field.send_keys("12345678")

        # Proceed through shipping and payment steps
        continue_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".continue-button")))
        continue_button.click()

        continue_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".continue-button")))
        continue_button.click()

        # Fill in credit card details
        payment_method_option = self.driver.find_element(By.CSS_SELECTOR, "#paymentmethod_1")
        payment_method_option.click()
        cardholder_name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cardHolderName")))
        card_number_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cardNumber")))
        expire_month_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "expireMonth")))
        expire_year_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "expireYear")))
        card_code_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "cardCode")))

        cardholder_name_field.send_keys("Test User")
        card_number_field.send_keys("4111111111111111")
        expire_month_field.send_keys("4")
        expire_year_field.send_keys("2027")
        card_code_field.send_keys("123")

        # Confirm order
        confirm_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".confirm-button")))
        confirm_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()