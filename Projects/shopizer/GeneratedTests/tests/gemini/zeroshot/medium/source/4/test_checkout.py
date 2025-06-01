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

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "user-name"))
            )
        except Exception as e:
            self.fail(f"Login failed: {e}")

        # Add product to cart
        try:
            product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/img"))
            )
            product.click()

            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "active"))
            )
            add_to_cart_button.click()

            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "count-style"))
            )
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
            self.fail(f"Failed to navigate to cart page: {e}")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to proceed to checkout: {e}")

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
            address_field.send_keys("Street 1")
            city_field.send_keys("Quebec")
            postal_code_field.send_keys("H2H2H2")
            phone_field.send_keys("1234567890")
            email_field.send_keys("test22@user.com")

            country_select = Select(WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Canada']/.."))
            ))
            country_select.select_by_visible_text("Canada")

            state_select = Select(WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Quebec']/.."))
            ))
            state_select.select_by_visible_text("Quebec")

            is_agree_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "isAgree"))
            )
            is_agree_checkbox.click()

            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']"))
            )

            # Verify that the billing form is filled
            self.assertEqual(first_name_field.get_attribute("value"), "Test")
            self.assertEqual(last_name_field.get_attribute("value"), "User")
            self.assertEqual(address_field.get_attribute("value"), "Street 1")
            self.assertEqual(city_field.get_attribute("value"), "Quebec")
            self.assertEqual(postal_code_field.get_attribute("value"), "H2H2H2")
            self.assertEqual(phone_field.get_attribute("value"), "1234567890")
            self.assertEqual(email_field.get_attribute("value"), "test22@user.com")

        except Exception as e:
            self.fail(f"Filling billing form failed: {e}")


if __name__ == "__main__":
    unittest.main()