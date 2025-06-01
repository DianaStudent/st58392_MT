import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import SelectElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import SelectElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import SelectElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import SelectElement
from selenium.webdriver.support.ui import Select

# Set up the webdriver and provide it with the path to the ChromeDriver executable
webdriver_manager = webdriver.Chrome()
driver = webdriver_manager.chromedriver()

# Define a function that performs login, adds products to the cart, goes to the cart page, clicks  "Proceed to Checkout", and fills in the billing form
def test_checkout_process():
    # Log in using credentials
    email_input = driver.find_element_by_name('email')
    password_input = driver.find_element_by_name('password')
    email_input.send_keys('test22@user.com')
    password_input.send_keys('test**11')
    driver.find_element_by_name('login').click()

    # Hover over the first product and click the  "Add to cart" button
    product_image = driver.find_element_by_css_selector('.product img')
    add_to_cart_button = driver.find_element_by_css_selector('.product .add-to-cart')
    ActionChains(driver).move_to_element(product_image).perform()
    add_to_cart_button.click()

    # Go to the cart page
    cart_icon = driver.find_element_by_css_selector('.cart-icon')
    WebDriverWait(driver, 20).until(cart_icon.enabled)
    cart_icon.click()

    # Click the "Proceed to Checkout" button
    proceed_to_checkout_button = driver.find_element_by_css_selector('.proceed-to-checkout-button')
    WebDriverWait(driver, 20).until(proceed_to_checkout_button.enabled)
    proceed_to_checkout_button.click()

    # Fill out the billing form: 
    company_input = driver.find_element_by_name('company')
    address_input = driver.find_element_by_name('address')
    city_input = driver.find_element_by_name('city')
    select_region = SelectElement(driver.find_element_by_name('select'))
    postal_code_input = driver.find_element_by_name('postal-code')
    phone_number_input = driver.find_element_by_name('phone-number')
    accept_terms_checkbox = driver.find_element_by_name('accept-terms')

    # Verify that the billing form is filled
    company_field = driver.find_element_by_name('company').get_attribute('data-name')
    if 'Comp1' != company_field:
        self.fail("The company field is not filled correctly")
    address_field = driver.find_element_by_name('address').get_attribute('data-name')
    if 'Street1' != address_field:
        self.fail("The address field is not filled correctly")
    city_field = driver.find_element_by_name('city').get_attribute('data-name')
    if 'Quebec' != city_field:
        self.fail("The city field is not filled correctly")
    postal_code_field = driver.find_element_by_name('postal-code').get_attribute('data-name')
    if '1234' != postal_code_field:
        self.fail("The postal code field is not filled correctly")
    phone_number_field = driver.find_element_by_name('phone-number').get_attribute('data-name')
    if '1234567891' != phone_number_field:
        self.fail("The phone number field is not filled correctly")
    accept_terms_checkbox_status = accept_terms_checkbox.get_attribute('checked')

    # Confirm success by verifying that the billing form is filled
    if accept_terms_checkbox_status == True:
        print("Billing form filled successfully")
    else:
        print("Billing form failed to be filled")

# Run the test case
test_checkout_process()