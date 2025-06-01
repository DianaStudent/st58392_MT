from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            pass

        # Login
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        try:
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.send_keys("test22@user.com")
        except:
            self.fail("Username field not found")

        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            password_field.send_keys("test**11")
        except:
            self.fail("Password field not found")

        try:
            login_submit_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )
            login_submit_button.click()
        except:
            self.fail("Login submit button not found")

        # Add product to cart
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following::button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Add to cart button not found")

        # Go to cart page
        try:
            cart_icon = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found")

        try:
            view_cart_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except:
            self.fail("View Cart button not found")

        # Proceed to checkout
        try:
            checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Proceed to Checkout button not found")

        # Fill billing form
        try:
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys("Test")
        except:
            self.fail("First name field not found")

        try:
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys("User")
        except:
            self.fail("Last name field not found")

        try:
            address_field = wait.until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            address_field.send_keys("123 Main St")
        except:
            self.fail("Address field not found")

        try:
            city_field = wait.until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            city_field.send_keys("Anytown")
        except:
            self.fail("City field not found")

        try:
            postal_code_field = wait.until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            postal_code_field.send_keys("H2H2H2")
        except:
            self.fail("Postal code field not found")

        try:
            phone_field = wait.until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            phone_field.send_keys("8888888888")
        except:
            self.fail("Phone field not found")

        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys("test@user.com")
        except:
            self.fail("Email field not found")

        # Select country
        try:
            country_select = Select(wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a country']/.."))
            ))
            country_select.select_by_visible_text("Canada")
        except:
            self.fail("Country select not found")

        # Select state
        try:
            state_select = Select(wait.until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/.."))
            ))
            state_select.select_by_visible_text("Quebec")
        except:
            self.fail("State select not found")

        # Accept terms and place order
        try:
            terms_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            terms_checkbox.click()
        except:
            self.fail("Terms checkbox not found")

        # Verify that the billing form is filled
        try:
            first_name_value = first_name_field.get_attribute("value")
            last_name_value = last_name_field.get_attribute("value")
            address_value = address_field.get_attribute("value")
            city_value = city_field.get_attribute("value")
            postal_code_value = postal_code_field.get_attribute("value")
            phone_value = phone_field.get_attribute("value")
            email_value = email_field.get_attribute("value")

            self.assertTrue(first_name_value != "", "First name is empty")
            self.assertTrue(last_name_value != "", "Last name is empty")
            self.assertTrue(address_value != "", "Address is empty")
            self.assertTrue(city_value != "", "City is empty")
            self.assertTrue(postal_code_value != "", "Postal code is empty")
            self.assertTrue(phone_value != "", "Phone is empty")
            self.assertTrue(email_value != "", "Email is empty")

        except:
            self.fail("Could not verify that the billing form is filled")


if __name__ == "__main__":
    unittest.main()