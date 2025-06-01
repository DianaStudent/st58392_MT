import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShoppingCart(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_shopping_cart(self):
        # Step 1: Open the home page.
        self.driver.get("http://max/")
        
        # Step 2: Click on the "Search" link and search for a product (e.g. "book").
        search_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@class='search-link']")))
        search_link.click()
        search_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'search-input')))
        search_input.send_keys("book")
        
        # Step 3: Click the "Add to cart" button for the first item in the search results.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='add-to-cart']")))
        add_to_cart_button.click()
        
        # Step 4: Open the shopping cart via the success notification popup.
        shopping_cart_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='shopping-cart-link']")))
        shopping_cart_link.click()
        
        # Step 5: Accept terms of service and click the "Checkout" button.
        terms_checkbox = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'terms-checkbox')))
        terms_checkbox.click()
        checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='checkout-button']")))
        checkout_button.click()
        
        # Step 6: Choose "Checkout as Guest".
        guest_checkout_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'guest-checkout')))
        guest_checkout_button.click()
        
        # Step 7: Fill in the billing address.
        first_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'first-name')))
        last_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'last-name')))
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'email')))
        city_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'city')))
        address1_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'address1')))
        zip_postal_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'zip-postal-code')))
        phone_number_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'phone-number')))
        
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        email_input.send_keys("random_email")
        city_input.send_keys("Riga")
        address1_input.send_keys("Street 1")
        zip_postal_code_input.send_keys("LV-1234")
        phone_number_input.send_keys("12345678")
        
        # Step 8: Select shipping and payment methods.
        shipping_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'shippingoption_1')))
        shipping_option.click()
        payment_method_option = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, 'paymentmethod_1')))
        payment_method_option.click()
        
        # Step 9: Enter credit card details.
        credit_card_type_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'credit-card-type')))
        cardholder_name_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'card-holder-name')))
        card_number_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'card-number')))
        expire_month_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'expire-month')))
        expire_year_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'expire-year')))
        card_code_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'card-code')))
        
        credit_card_type_input.send_keys("visa")
        cardholder_name_input.send_keys("Test User")
        card_number_input.send_keys("1234567890123456")
        expire_month_input.send_keys("12")
        expire_year_input.send_keys("2025")
        card_code_input.send_keys("123")
        
        # Step 10: Click the "Place Order" button.
        place_order_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='place-order-button']")))
        place_order_button.click()
        
        # Step 11: Verify that the order was placed successfully.
        order_received_message = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'order-received-message')))
        self.assertEqual(order_received_message.text, "Order received successfully")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()