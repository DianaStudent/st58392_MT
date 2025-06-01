from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestOrderCompletion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_order_completion(self):
        # 1. Search for a product and add it to cart
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search-input"))
        )
        search_input.send_keys("book")
        search_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()
        product_tile_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "(//a[@class='product-tile'])[1]"))
        )
        product_tile_button.click()

        # 2. From the success notification, click the "shopping cart" link
        shopping_cart_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/cart']"))
        )
        shopping_cart_link.click()

        # 3. Check the "Terms of service" checkbox and click the "Checkout" button
        terms_checkbox = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "terms-checkbox"))
        )
        terms_checkbox.click()
        checkout_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        checkout_button.click()

        # 4. Choose "Checkout as Guest"
        guest_checkout_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "guest-checkout-link"))
        )
        guest_checkout_link.click()

        # 5. Fill out the full billing form
        first_name_input = self.driver.find_element(By.XPATH, "//input[@name='firstName']")
        last_name_input = self.driver.find_element(By.XPATH, "//input[@name='lastName']")
        email_input = self.driver.find_element(By.XPATH, "//input[@name='email']")
        address_input = self.driver.find_element(By.XPATH, "//input[@name='address1']")
        city_input = self.driver.find_element(By.XPATH, "//input[@name='city']")
        country_select = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "country-select"))
        )
        state_province_select = self.driver.find_element(By.XPATH, "//select[@id='stateProvinceSelect']")
        zip_postal_code_input = self.driver.find_element(By.XPATH, "//input[@name='zipPostalCode']")
        phone_input = self.driver.find_element(By.XPATH, "//input[@name='phoneNumber']")

        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("random_email@example.com")
        address_input.send_keys("Street 1")
        city_input.send_keys("Riga")
        country_select.send_keys("124")  # Select country by ID
        state_province_select.send_keys("0")  # Select state/province by ID
        zip_postal_code_input.send_keys("LV-1234")
        phone_input.send_keys("12345678")

        # 6. Proceed through the following steps: Shipping method, Payment method, Payment info
        shipping_option_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@id='shippingoption_1']"))
        )
        shipping_option_button.click()
        payment_method_option_button = self.driver.find_element(By.XPATH, "//button[@id='paymentmethod_1']")
        payment_method_option_button.click()

        # 7. Fill in credit card details
        cardholder_name_input = self.driver.find_element(By.XPATH, "//input[@name='cardholderName']")
        card_number_input = self.driver.find_element(By.XPATH, "//input[@name='cardNumber']")
        expire_month_input = self.driver.find_element(By.XPATH, "//input[@name='expireMonth']")
        expire_year_input = self.driver.find_element(By.XPATH, "//input[@name='expireYear']")
        card_code_input = self.driver.find_element(By.XPATH, "//input[@name='cardCode']")

        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("4111111111111111")
        expire_month_input.send_keys("4")
        expire_year_input.send_keys("2027")
        card_code_input.send_keys("123")

        # 8. Confirm the order
        confirm_button = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='confirm-button']"))
        )
        confirm_button.click()

        # 9. Verify that the order is complete
        order_completion_message = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='order-completion-message']"))
        )
        self.assertEqual(order_completion_message.text, "Order completed successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()