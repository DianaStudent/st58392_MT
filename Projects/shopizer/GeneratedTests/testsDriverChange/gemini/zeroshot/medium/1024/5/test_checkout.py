import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
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
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
            )
            login_link.click()

            username_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))
            )

            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()

        except Exception as e:
            self.fail(f"Login failed: {e}")

        # Add product to cart
        try:
            product = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/img"))
            )
            product.click()
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Add to cart')]"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {e}")
        
        # Go to cart page
        try:
            icon_cart = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            icon_cart.click()
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Go to cart page failed: {e}")

        # Proceed to checkout
        try:
            proceed_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            proceed_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Proceed to checkout failed: {e}")

        # Fill in billing form
        try:
            first_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            address_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            postal_code_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[contains(text(),'Select a country')]"))
            )
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[contains(text(),'Select a state')]"))
            )
            
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            address_input.send_keys("1234 Street")
            city_input.send_keys("My city")
            postal_code_input.send_keys("H2H-2H2")
            phone_input.send_keys("1234567890")
            email_input.send_keys("test22@user.com")
            
            country_select_element = driver.find_element(By.XPATH, "//select")
            country_select_obj = Select(country_select_element)
            country_select_obj.select_by_value("CA")

            state_select_element = driver.find_elements(By.XPATH, "//select")[1]
            state_select_obj = Select(state_select_element)
            state_select_obj.select_by_value("QC")
            
            is_agree_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            is_agree_checkbox.click()
            
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Place your order')]"))
            )
            
        except Exception as e:
            self.fail(f"Filling billing form failed: {e}")
            
        # Confirm success
        try:
            self.assertTrue(first_name_input.get_attribute("value") == "Test", "First name not filled")
            self.assertTrue(last_name_input.get_attribute("value") == "User", "Last name not filled")
            self.assertTrue(address_input.get_attribute("value") == "1234 Street", "Address not filled")
            self.assertTrue(city_input.get_attribute("value") == "My city", "City not filled")
            self.assertTrue(postal_code_input.get_attribute("value") == "H2H-2H2", "Postal code not filled")
            self.assertTrue(phone_input.get_attribute("value") == "1234567890", "Phone not filled")
            self.assertTrue(email_input.get_attribute("value") == "test22@user.com", "Email not filled")
        except Exception as e:
            self.fail(f"Confirmation failed: {e}")

if __name__ == "__main__":
    unittest.main()