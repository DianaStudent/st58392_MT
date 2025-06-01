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
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_flow(self):
        # Step 1: Open the homepage
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))

        # Step 2: Navigate to the "Search" page and look for a product using the query "book"
        search_input = self.driver.find_element(By.NAME, "search_query")
        search_input.send_keys("book")
        search_button = self.driver.find_element(By.NAME, "submit_search")
        search_button.click()

        # Step 3: Add the first result to the cart
        product_tile = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ul[@id='results-0-list']//li[1]")))
        add_to_cart_button = product_tile.find_element(By.TAG_NAME, "a")
        add_to_cart_button.click()

        # Step 4: From the success notification, click the "shopping cart" link
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-notification']//ul//li[2]")))
        shopping_cart_link = self.driver.find_element(By.XPATH, "//div[@class='cart-notification']//ul//li[2]")
        shopping_cart_link.click()

        # Step 5: Check the "Terms of service" checkbox and click the "Checkout" button
        terms_of_service_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "termsofservice")))
        terms_of_service_checkbox.click()
        checkout_button = self.driver.find_element(By.NAME, "processAddress")
        checkout_button.click()

        # Step 6: Choose "Checkout as Guest"
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "guestCheckoutButton")))
        guest_checkout_button = self.driver.find_element(By.ID, "guestCheckoutButton")
        guest_checkout_button.click()

        # Step 7: Fill out the full billing form (from credentials):
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "BillingAddress_FirstName")))
        first_name_input.send_keys("Test")

        last_name_input = self.driver.find_element(By.NAME, "BillingAddress_LastName")
        last_name_input.send_keys("User")

        email_input = self.driver.find_element(By.NAME, "BillingAddress_Email")
        email_input.send_keys("random_email@max.com")

        address1_input = self.driver.find_element(By.NAME, "BillingAddress_Address1")
        address1_input.send_keys("Street 1")

        city_input = self.driver.find_element(By.NAME, "BillingAddress_City")
        city_input.send_keys("Riga")

        zip_postal_code_input = self.driver.find_element(By.NAME, "BillingAddress_ZipPostalCode")
        zip_postal_code_input.send_keys("LV-1234")

        phone_number_input = self.driver.find_element(By.NAME, "BillingAddress_PhoneNumber")
        phone_number_input.send_keys("12345678")

        country_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_CountryId")))
        country_option = country_select.find_elements_by_tag_name('option')[1]
        country_option.click()

        state_province_select = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "BillingAddress_StateProvinceId")))
        state_province_option = state_province_select.find_elements_by_tag_name('option')[0]
        state_province_option.click()

        shipping_method_step = self.driver.find_element(By.NAME, "processShipping")
        shipping_method_step.click()

        payment_method_step = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "paymentMethodId")))
        payment_method_option = payment_method_step.find_elements_by_tag_name('option')[1]
        payment_method_option.click()

        payment_info_step = self.driver.find_element(By.NAME, "processPayment")
        payment_info_step.click()

        credit_card_type_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "CreditCardType")))
        credit_card_type_input.send_keys("visa")

        cardholder_name_input = self.driver.find_element(By.NAME, "CardHolderName")
        cardholder_name_input.send_keys("Test User")

        card_number_input = self.driver.find_element(By.NAME, "CardNumber")
        card_number_input.send_keys("1234567890123456")

        expiration_date_input = self.driver.find_element(By.NAME, "ExpirationDate")
        expiration_date_input.send_keys("12/2025")

        cvv_input = self.driver.find_element(By.NAME, "CVV")
        cvv_input.send_keys("123")

        # Step 8: Place order
        place_order_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "placeOrder")))
        place_order_button.click()

        # Step 9: Verify that the order was placed successfully
        order_confirmation_text = self.driver.find_element(By.XPATH, "//div[@class='order-confirmation']//p")
        self.assertEqual(order_confirmation_text.text, "Thank you for shopping at Max!")

if __name__ == "__main__":
    unittest.main()