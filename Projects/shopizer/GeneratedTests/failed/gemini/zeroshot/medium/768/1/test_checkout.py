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
        self.driver.implicitly_wait(10)
        self.base_url = "http://localhost/"
        self.email = "test22@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Open the home page.
        self.assertEqual(driver.current_url, self.base_url)

        # 2. Log in using the provided credentials.
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Could not find account button: {e}")

        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Could not find login link: {e}")

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

            username_field.send_keys(self.email)
            password_field.send_keys(self.password)
            login_button.click()

        except Exception as e:
            self.fail(f"Could not find login elements: {e}")

        # Verify successful login
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "user-name"))
            )
        except Exception as e:
            self.fail(f"Login failed: {e}")

        # 3. Add product to the cart.
        try:
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following::button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find add to cart button: {e}")

        # 4. Open the cart and navigate to the cart page.
        try:
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Could not find cart button: {e}")

        try:
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find view cart button: {e}")

        # 5. Click "Proceed to Checkout".
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Could not find checkout button: {e}")

        # 6. Fill in the billing form.
        try:
            first_name_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            last_name_field = driver.find_element(By.NAME, "lastName")
            address_field = driver.find_element(By.NAME, "address")
            city_field = driver.find_element(By.NAME, "city")
            postal_code_field = driver.find_element(By.NAME, "postalCode")
            phone_field = driver.find_element(By.NAME, "phone")
            email_field = driver.find_element(By.NAME, "email")

            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            address_field.send_keys("123 Street")
            city_field.send_keys("My City")
            postal_code_field.send_keys("H2H2H2")
            phone_field.send_keys("1234567890")
            email_field.send_keys("test22@user.com")

            # Select country
            country_select = Select(driver.find_element(By.XPATH, "//select/option[text()='Select a country']/.."))
            country_select.select_by_visible_text("Canada")

            # Wait for state select to load and select state
            state_select = Select(WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']/.."))
            ))
            state_select.select_by_visible_text("Quebec")

        except Exception as e:
            self.fail(f"Could not find or fill billing form elements: {e}")

        # 7. Accept terms and proceed.
        try:
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            terms_checkbox.click()
        except Exception as e:
            self.fail(f"Could not find terms checkbox: {e}")

        # 8. Confirm success if form is filled.
        self.assertTrue(first_name_field.get_attribute("value") == "Test")
        self.assertTrue(last_name_field.get_attribute("value") == "User")
        self.assertTrue(address_field.get_attribute("value") == "123 Street")
        self.assertTrue(city_field.get_attribute("value") == "My City")
        self.assertTrue(postal_code_field.get_attribute("value") == "H2H2H2")
        self.assertTrue(phone_field.get_attribute("value") == "1234567890")
        self.assertTrue(email_field.get_attribute("value") == "test22@user.com")

if __name__ == "__main__":
    unittest.main()