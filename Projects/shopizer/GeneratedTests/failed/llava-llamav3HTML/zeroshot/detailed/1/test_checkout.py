from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import is_webdriver_manager_present, download_chrome_driver
from selenium.webdriver.chrome.service import Service as ChromeService

is_webdriver_manager_present()
download_chrome_driver()

class TestBillingForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_billing_form(self):
        # Open the home page
        driver = self.driver
        driver.get("http://localhost/")
        
        # Log in using credentials
        email_input = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'Email')]/following::input[1]"
        )
        password_input = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'Password')]/following::input[1]"
        )
        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")

        # Hover over the first product
        first_product = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'Olive Table')]/following::span[1]"
        )
        hover_style = driver.get_attribute(first_product.get_attribute("href"))
        driver.get(hover_style)

        # Click the revealed "Add to cart" button
        add_to_cart_button = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'ADD TO CART')]/following::button[1]"
        )
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'Cart')]/following::img[1]"
        )
        cart_icon.click()

        # Wait for the popup to become visible
        WebDriverWait(driver, 20)

        # Click "View cart" or similar button inside the popup
        view_cart_button = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'VIEW CART')]/following::button[1]"
        )
        view_cart_button.click()

        # Fill out the billing form:
        company_input = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'COMPANY')]/following::input[1]"
        )
        address_input = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'ADDRESS')]/following::input[1]"
        )
        company_input.send_keys("Comp1")
        address_input.send_keys("Street1")

        city_select = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'CITY')]/following::select[1]"
        )
        self.assertIn("Quebec", [option.text for option in city_select.options])

        postal_code_input = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'POSTAL CODE')]/following::input[1]"
        )
        postal_code_input.send_keys("1234")

        phone_number_input = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'PHONE NUMBER')]/following::input[1]"
        )
        phone_number_input.send_keys("1234567891")

        self.assertTrue(email_input.get_attribute("data-name") == "email")
        self.assertTrue(password_input.get_attribute("data-name") == "password")

        # Check terms checkbox
        checkbox = WebDriverWait(driver, 20).until(
            By.XPATH, "//*[contains(text(), 'ACCEPT TERMS')]/following::input[1]"
        )
        checkbox.click()

        # Wait for any maps popups or warnings and close them
        try:
            WebDriverWait(driver, 20)
        except WebDriverException:
            pass

        # Confirm success if form is filled
        self.assertTrue(company_input.get_attribute("data-name") == "company")
        self.assertTrue(address_input.get_attribute("data-name") == "address")
        self.assertTrue(postal_code_input.get_attribute("data-name") == "postal code")
        self.assertTrue(phone_number_input.get_attribute("data-name") == "phone number")

if __name__ == '__main__':
    unittest.main()