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
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        # Accept cookies
        try:
            accept_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            pass

        # Go to login page
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Could not navigate to login page: {e}")

        # Login
        try:
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
            self.fail(f"Could not add product to cart: {e}")

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
            self.fail(f"Could not navigate to cart page: {e}")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Could not proceed to checkout: {e}")

        # Fill billing form
        try:
            first_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            address = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            postal_code = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            email = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )

            first_name.send_keys("Test")
            last_name.send_keys("User")
            address.send_keys("123 Street")
            city.send_keys("My city")
            postal_code.send_keys("H2H2H2")
            phone.send_keys("1234567890")
            email.send_keys("test22@user.com")

            # Select country and state
            country_select = Select(WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select[preceding-sibling::label[text()='Country']]"))
            ))
            country_select.select_by_value("CA")

            state_select = Select(WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select[preceding-sibling::label[text()='State']]"))
            ))
            state_select.select_by_value("QC")

            # Accept terms and place order
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            terms_checkbox.click()
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']"))
            )
            #place_order_button.click() #Commented out to avoid placing an actual order

        except Exception as e:
            self.fail(f"Could not fill billing form: {e}")

        # Verify that the billing form is filled
        try:
            value_first_name = first_name.get_attribute('value')
            self.assertTrue(value_first_name == "Test", "First name is not filled")
            value_last_name = last_name.get_attribute('value')
            self.assertTrue(value_last_name == "User", "Last name is not filled")
            value_address = address.get_attribute('value')
            self.assertTrue(value_address == "123 Street", "Address is not filled")
            value_city = city.get_attribute('value')
            self.assertTrue(value_city == "My city", "City is not filled")
            value_postal_code = postal_code.get_attribute('value')
            self.assertTrue(value_postal_code == "H2H2H2", "Postal code is not filled")
            value_phone = phone.get_attribute('value')
            self.assertTrue(value_phone == "1234567890", "Phone is not filled")
            value_email = email.get_attribute('value')
            self.assertTrue(value_email == "test22@user.com", "Email is not filled")

        except Exception as e:
            self.fail(f"Verification failed: {e}")

if __name__ == "__main__":
    unittest.main()