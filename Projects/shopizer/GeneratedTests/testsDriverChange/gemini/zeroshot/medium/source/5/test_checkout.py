```python
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
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()
        except:
            pass
        # Login
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.account-setting-active > i.pe-7s-user-female"))
            ).click()
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            ).click()
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
            product_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/img"))
            )
            ActionChains(driver).move_to_element(product_element).perform()
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following-sibling::div[@class='product-action-2']/button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {e}")
        
        # Add another product to cart
        try:
            product_element = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/chair']/img"))
            )
            ActionChains(driver).move_to_element(product_element).perform()
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/chair']/following-sibling::div[@class='product-action-2']/button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {e}")

        # Open cart and navigate to cart page
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.icon-cart > i.pe-7s-shopbag"))
            ).click()
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            ).click()
        except Exception as e:
            self.fail(f"Navigating to cart page failed: {e}")

        # Proceed to checkout
        try:
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            ).click()
        except Exception as e:
            self.fail(f"Proceeding to checkout failed: {e}")

        # Fill in billing form
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
            country_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='Select a country']/parent::select"))
            )
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//select/option[text()='']/parent::select"))
            )
            
            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            address_field.send_keys("123 Street")
            city_field.send_keys("My city")
            postal_code_field.send_keys("H2H-2H2")
            phone_field.send_keys("1234567890")
            email_field.send_keys("test22@user.com")

            select_country = Select(country_select)
            select_country.select_by_value("CA")
            
            select_state = Select(state_select)
            select_state.select_by_value("QC")

        except Exception as e:
            self.fail(f"Filling billing form failed: {e}")

        # Accept terms and place order
        try:
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            place_order_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']"))
            )

            terms_checkbox.click()
            place_order_button.click()

        except Exception as e:
            self.fail(f"Accepting terms and placing order failed: {e}")

        # Confirm success (verify form is filled)
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='firstName' and @value='Test']"))
            )
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='lastName' and @value='User']"))
            )
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='address' and @value='123 Street']"))
            )
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//input[@name='city' and @value='My city']"))
            )