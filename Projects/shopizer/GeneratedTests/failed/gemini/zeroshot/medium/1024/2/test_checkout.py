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
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Login
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()

            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )

            username_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_button.click()
        except Exception as e:
            self.fail(f"Login failed: {e}")

        # Add product to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following::button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {e}")

        # Add chair to cart
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/chair']/following::button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {e}")

        # Go to cart page
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Navigating to cart failed: {e}")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Navigating to checkout failed: {e}")

        # Fill billing form
        try:
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            address_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            postal_code_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )

            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            address_field.send_keys("123 Street")
            city_field.send_keys("My city")
            postal_code_field.send_keys("H2H2H2")
            phone_field.send_keys("1234567890")
            email_field.send_keys("test@user.com")

            # Select country
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-lg-12']/div[@class='billing-select mb-20']/select"))
            )
            country = Select(country_select)
            country.select_by_value("CA")

            # Select state
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-lg-6 col-md-6']/div[@class='billing-select mb-20']/select"))
            )
            state = Select(state_select)
            state.select_by_value("QC")

        except Exception as e:
            self.fail(f"Filling billing form failed: {e}")

        # Accept terms and place order
        try:
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            terms_checkbox.click()
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']"))
            )
            # Check if billing form is filled
            self.assertNotEqual(first_name_field.get_attribute("value"), "", "First name is empty")
            self.assertNotEqual(last_name_field.get_attribute("value"), "", "Last name is empty")
            self.assertNotEqual(address_field.get_attribute("value"), "", "Address is empty")
            self.assertNotEqual(city_field.get_attribute("value"), "", "City is empty")
            self.assertNotEqual(postal_code_field.get_attribute("value"), "", "Postal code is empty")
            self.assertNotEqual(phone_field.get_attribute("value"), "", "Phone is empty")
            self.assertNotEqual(email_field.get_attribute("value"), "", "Email is empty")

            # place_order_button.click() # Commented out to prevent placing actual order
        except Exception as e:
            self.fail(f"Placing order failed: {e}")

if __name__ == "__main__":
    unittest.main()