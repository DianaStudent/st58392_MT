import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

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
            accept_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
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

        # Add second product to cart
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
            proceed_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            proceed_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Proceeding to checkout failed: {e}")

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
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']"))
            )
            city_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a state']"))
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
            address_field.send_keys("1234 Street")
            city_field.send_keys("My city")
            postal_code_field.send_keys("H2H2H2")
            phone_field.send_keys("1234567890")
            email_field.send_keys("test22@user.com")

            # Select country and state
            country_select_element = driver.find_element(By.XPATH, "//select/option[text()='Select a country']")
            country_select_element.click()
            canada_option = driver.find_element(By.XPATH, "//select/option[text()='Canada']")
            canada_option.click()

            state_select_element = driver.find_element(By.XPATH, "//select/option[text()='Select a state']")
            state_select_element.click()
            quebec_option = driver.find_element(By.XPATH, "//select/option[text()='Quebec']")
            quebec_option.click()

            # Accept terms and place order
            agree_terms_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            agree_terms_checkbox.click()
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']"))
            )
            
        except Exception as e:
            self.fail(f"Filling billing form failed: {e}")

        # Verify billing form is filled
        try:
            self.assertEqual(first_name_field.get_attribute("value"), "Test")
            self.assertEqual(last_name_field.get_attribute("value"), "User")
            self.assertEqual(address_field.get_attribute("value"), "1234 Street")
            self.assertEqual(city_field.get_attribute("value"), "My city")
            self.assertEqual(postal_code_field.get_attribute("value"), "H2H2H2")
            self.assertEqual(phone_field.get_attribute("value"), "1234567890")
            self.assertEqual(email_field.get_attribute("value"), "test22@user.com")
        except NoSuchElementException:
            self.fail("Billing form not filled correctly")

if __name__ == "__main__":
    unittest.main()