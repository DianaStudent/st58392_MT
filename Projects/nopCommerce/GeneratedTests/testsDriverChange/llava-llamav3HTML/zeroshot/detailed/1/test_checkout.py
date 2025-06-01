import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_keys import ActionKeys
from selenium.webdriver.common.alerts import Alert
from selenium.webdriver.common.exceptions import NoSuchElementException
from selenium.webdriver.common.locators import By

class TestOrderCompletion(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)
        
    def tearDown(self):
        self.driver.quit()
    
    def test_order_completion(self):
        # Open the homepage
        self.driver.get("http://max/")
        
        # Navigate to the "Search" page and look for a product using the query "book"
        search_box = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'q')]"
        )
        search_box.send_keys("book")
        self.wait.until(
            By.XPATH,
            "//button[contains(text(), 'Search')]"),
            timeout=20
        ).click()
        
        # Add the first result to the cart using a product tile button
        product_tile = self.wait.until(
            By.XPATH,
            "//div[contains(@class, 'product-tile')]/a",
            timeout=20
        )
        product_tile.click()
        
        # Check the success popup and click the "shopping cart" link
        success_popup = self.wait.until(
            By.XPATH,
            "//div[contains(text(), 'Success')]"],
            timeout=10
        )
        shopping_cart_link = success_popup.find_element_by_css_selector("a")
        shopping_cart_link.click()
        
        # Use the "Checkout as Guest" option
        checkout_as_guest_button = self.wait.until(
            By.XPATH,
            "//button[contains(@id, 'guest-cart-button')]"],
            timeout=20
        )
        checkout_as_guest_button.click()
        
        # Fill out the full billing form (from credentials):
        first_name_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'first_name')]"],
            timeout=10
        )
        last_name_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'last_name')]"],
            timeout=10
        )
        email_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'email')]"],
            timeout=10
        )
        address1_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'address_1')]"],
            timeout=10
        )
        city_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'city')]"],
            timeout=10
        )
        country_id_input = self.wait.until(
            By.XPATH,
            "//select[contains(@id, 'country_id')]"],
            timeout=10
        )
        state_province_id_input = self.wait.until(
            By.XPATH,
            "//select[contains(@id, 'state_province_id')]"],
            timeout=10
        )
        shipping_method_step_button = self.wait.until(
            By.XPATH,
            "//button[contains(@id, 'step_4-button')]"],
            timeout=20
        )
        
        # Payment method step
        payment_method_step_button = self.wait.until(
            By.XPATH,
            "//button[contains(@id, 'step_5-button')}"],
            timeout=20
        )
        
        # Payment info step (fill in credit card details from credentials)
        card_type_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'card_type')]"],
            timeout=10
        )
        cardholder_name_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'cardholder_name')}"],
            timeout=10
        )
        card_number_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'card_number')]"],
            timeout=10
        )
        expire_month_input = self.wait.until(
            By.XPATH,
            "//select[contains(@id, 'expire_month')}"],
            timeout=10
        )
        expire_year_input = self.wait.until(
            By.XPATH,
            "//select[contains(@id, 'expire_year')}"],
            timeout=10
        )
        card_code_input = self.wait.until(
            By.XPATH,
            "//input[contains(@name, 'card_code')}"],
            timeout=10
        )
        
        # Confirm step (click "Confirm" and wait for success message)
        confirm_button = self.wait.until(
            By.XPATH,
            "//button[contains(@id, 'step_7-button')}"],
            timeout=20
        )
        confirm_button.click()
        success_message = self.wait.until(
            By.XPATH,
            "//div[contains(text(), 'Thank you')]"],
            timeout=10
        )
        self.assertEqual("Thank you", success_message)
        
        # Confirm that the order has been completed by checking the "Success" message
        self.assertTrue(success_message, "Order completion failed")
    
if __name__ == "__main__":
    unittest.main()