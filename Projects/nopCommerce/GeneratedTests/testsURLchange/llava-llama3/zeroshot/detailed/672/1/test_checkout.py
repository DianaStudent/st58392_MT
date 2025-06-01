import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alerts import Alert

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        # Set up Chrome webdriver using webdriver-manager
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser window
        self.driver.quit()

    def test_checkout(self):
        try:
            # Step 1: Open the homepage
            self.assertTrue("Representative" in self.driver.title)

            # Step 2: Search for a product (e.g. "book") and add it to cart
            search_input = self.driver.find_element_by_name('search')
            search_input.send_keys("book")
            search_input.send_keys(Keys.RETURN)
            cart_button = self.driver.find_element_by_css_selector(".product-tile__button")

            # Step 3: Click on the "shopping cart" link from the success popup
            success_popup = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            cart_link = self.driver.find_element_by_css_selector("a[title='Shopping Cart']")
            cart_link.click()

            # Step 4: Choose "Checkout as Guest"
            guest_checkout_button = self.driver.find_element_by_css_selector(".guest__button")
            guest_checkout_button.click()

            # Step 5: Fill out the full billing form
            first_name_input = self.driver.find_element_by_name('first_name')
            last_name_input = self.driver.find_element_by_name('last_name')
            email_input = self.driver.find_element_by_name('email')
            address1_input = self.driver.find_element_by_name('address_1')
            city_input = self.driver.find_element_by_name('city')
            country_id_select = Select(self.driver.find_element_by_name('country'))
            zip_code_input = self.driver.find_element_by_name('zip')

            # Step 6: Proceed through the following: Shipping method step
            shipping_method_button = self.driver.find_element_by_css_selector(".shipping-method__button")
            shipping_method_button.click()

            # Step 7: Payment method step
            payment_method_button = self.driver.find_element_by_css_selector(".payment-method__button")
            payment_method_button.click()

            # Step 8: Payment info step (fill in credit card details if necessary)
            cardholder_name_input = self.driver.find_element_by_name('cardholder_name')
            card_number_input = self.driver.find_element_by_name('card_number')
            expire_month_input = self.driver.find_element_by_name('expire_month')
            expire_year_input = self.driver.find_element_by_name('expire_year')
            card_code_input = self.driver.find_element_by_name('card_code')

            # Step 9: Confirm the order completion by checking for a success message
            success_message = WebDriverWait(self.driver, 20).until(EC.alert_is_present())
            self.assertTrue("Thank you" in success_message.text)

        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == '__main__':
    unittest.main()