import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from webdriver_manager import ChromeDriverManager
from webdriver_manager.chrome import ChromeDriver

class TestPurchaseFlow(unittest.TestCase):
    def setUp(self):
        driver = ChromeDriver()
        self.driver = driver
        self.driver.get('http://max/')
        sleep(2)  # wait for the page to load

    def tearDown(self):
        self.driver.quit()

    def test_purchase_flow(self):
        sleep(5)  # wait for some time
        
        # Step 1: Search for a product (e.g. "book")
        search_box = self.driver.find_element_by_name('search')
        self.driver.execute_script(f'arguments[0].value="{Keys.RETURN}";return false', search_box)
        sleep(5)  # wait for the page to load
        
        # Step 2: Add to cart
        item = self.driver.find_element_by_css_selector('product-item')  # find a product item
        self.driver.execute_script(f'arguments[0].value="{Keys.RETURN}";return false', item)
        
        # Step 3: Open shopping cart
        sleep(5)  # wait for the page to load
        
        # Step 4: Choose "Checkout as Guest"
        guest_button = self.wait_for_element_by_id('guest-btn')
        guest_button.click()
        
        # Step 5: Fill in billing address
        first_name_input = self.wait_for_element_by_name('first-name-input')
        last_name_input = self.wait_for_element_by_name('last-name-input')
        email_input = self.wait_for_element_by_name('email-input')
        city_input = self.wait_for_element_by_name('city-input')
        address1_input = self.wait_for_element_by_name('address1-input')
        zip_postal_code_input = self.wait_for_element_by_name('zip-postal-code-input')
        phone_number_input = self.wait_for_element_by_name('phone-number-input')
        country_id_input = self.wait_for_element_by_name('country-id-input')
        state_province_id_input = self.wait_for_element_by_name('state-province-id-input')
        
        # Step 6: Select shipping and payment methods
        self.wait_for_element_by_id('shipping-option-1').click()
        self.wait_for_element_by_id('payment-method-1').click()
        
        # Step 7: Enter credit card details
        credit_card_type_input = self.wait_for_element_by_name('credit-card-type-input')
        cardholder_name_input = self.wait_for_element_by_name('cardholder-name-input')
        card_number_input = self.wait_for_element_by_name('card-number-input')
        expire_month_input = self.wait_for_element_by_name('expire-month-input')
        expire_year_input = self.wait_for_element_by_name('expire-year-input')
        card_code_input = self.wait_for_element_by_name('card-code-input')
        
        # Step 8: Confirm the order
        confirmation_message = self.wait_for_text('order-confirmation-message')
        if not confirmation_message:
            self.fail("Order confirmation message is not visible")
        
def wait_for_element(self, element_id):
    return WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, element_id)))
    
def wait_for_text(self, text):
    return WebDriverWait(self.driver, 10).until(EC.text_to_become_visble(text))

if __name__ == '__main__':
    unittest.main()