from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.elemen tlocators import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

class TestEcomTest(unittest.TestCase):
def setUp(self):
self.driver = ChromeDriverManager().get_chrome_driver()

# test case 1
def test_search_and_add_to_cart(self):
search_input = self.driver.find_element(by=By.XPATH, value="//input[contains(@name,'SearchInput')]")
search_input.send_keys("book")
search_button = self.driver.find_element(by=By.XPATH, value="//button[contains(@class,'btn btn-primary search-button')]")
self.wait_for_clickable(search_button)
search_button.click()

# test case 2
def test_shopping_cart_and_checkout(self):
success_message = self.driver.find_element(by=By.XPATH, value="//p[contains(text,'your order has been successfully processed!')]")
self.wait_for_clickable(success_message)

# test case 3

def test_buy_product_as_guest(self):
select_billing_address_button = self.driver.find_element(by=By.XPATH, value="//button[contains(@class,'btn btn-primary select-billing-address')]")
self.wait_for_clickable(select_billing_address_button)
select_billing_address_button.click()

# test case 4
def test_fill_in_credentials(self):
first_name_input = self.driver.find_element(by=By.XPATH, value=f "//input[contains(@name,'FirstName')]")
last_name_input = self.driver.find_element(by=By.XPATH, value=f "//input[contains(@name,'LastName')']")
email_input = self.driver.find_element(by=By.XPATH, value=f "//input[contains(@name,'Email')]")
city_input = self.driver.find_element(by=By.XPATH, value=f "//input[contains(@name,'City')]")
address1_input = self.driver.find_element(by=By.XPATH, value=f "//input[contains(@name,'Address1')")]
zipcode_input = self.driver.find_element(by=By.XPATH, value=f "//input[contains(@name,'ZipPostalCode')]")
phoneNumber_input = self.driver.find_element(by=By.XPATH, value=f "//input[contains(@name,'PhoneNumber')']")
countryId_input = self.driver.find_element(by=By.XPATH, value=f "//select[contains(@id,'CountryId')]/option[0]")

# test case 5
def test_select_payment_method(self):
payment_method_list = self.driver.find_elements(by=By.XPATH, value=f "//select[contains(@name,'PaymentMethodOptionsList')]/option")
for option in payment_method_list:
if option.get_attribute('id') == "paymentmethod_1":
select_payment_method_button = self.wait_for_clickable(f "//button[contains(@class,'btn btn-primary select-payment-method-button')]")
self.wait_for_clickable(select_payment_method_button)
select_payment_method_button.click()

# test case 6
def test_fill_in_credit_card_details(self):
card_type_input = self.driver.find_element(by=By.XPATH, value=f "//select[contains(@id,'CreditCardTypesList')]/option")
if card_type_input.get_attribute('value') == "visa":
card_number_input = self.wait_for_clickable(f "//input[contains(@name,'CreditCardNumber')]")
self.wait_for_clickable(card_number_input)

# test case 7
def test_confirm_order(self):
order_status_message = self.driver.find_element(by=By.XPATH, value=f "//p[contains(text,'your order has been successfully processed!')]")
self.wait_for_clickable(order_status_message)

if __name__ == '__main__':
unittest.main()

Note: This is an example code snippet for demonstration purposes. It may require some modifications to work correctly with the given HTML structure.