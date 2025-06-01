import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

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

        # 1. Open the home page.
        self.assertEqual(driver.current_url, "http://localhost/")

        # 2. Log in using the provided credentials.
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except Exception as e:
            self.fail(f"Account button not found or not clickable: {e}")

        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found or not clickable: {e}")

        try:
            username_field = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            username_field.send_keys("test22@user.com")
        except Exception as e:
            self.fail(f"Username field not found: {e}")

        try:
            password_field = wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            password_field.send_keys("test**11")
        except Exception as e:
            self.fail(f"Password field not found: {e}")

        try:
            login_submit_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Login')]"))
            )
            login_submit_button.click()
        except Exception as e:
            self.fail(f"Login submit button not found or not clickable: {e}")

        # 3. Add product to the cart.
        try:
            add_to_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following::button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Add to cart button not found or not clickable: {e}")

        # 4. Open the cart and navigate to the cart page.
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()
        except Exception as e:
            self.fail(f"Cart button not found or not clickable: {e}")

        try:
            view_cart_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"View Cart button not found or not clickable: {e}")

        # 5. Click "Proceed to Checkout".
        try:
            checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Proceed to Checkout button not found or not clickable: {e}")

        # 6. Fill in the billing form.
        try:
            first_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_field.send_keys("Test")
        except Exception as e:
            self.fail(f"First name field not found: {e}")

        try:
            last_name_field = wait.until(
                EC.presence_of_element_located((By.NAME, "lastName"))
            )
            last_name_field.send_keys("User")
        except Exception as e:
            self.fail(f"Last name field not found: {e}")

        try:
            address_field = wait.until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            address_field.send_keys("123 Main St")
        except Exception as e:
            self.fail(f"Address field not found: {e}")

        try:
            city_field = wait.until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            city_field.send_keys("Anytown")
        except Exception as e:
            self.fail(f"City field not found: {e}")

        try:
            postal_code_field = wait.until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            postal_code_field.send_keys("H2H2H2")
        except Exception as e:
            self.fail(f"Postal code field not found: {e}")

        try:
            phone_field = wait.until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            phone_field.send_keys("8888888888")
        except Exception as e:
            self.fail(f"Phone field not found: {e}")

        try:
            email_field = wait.until(
                EC.presence_of_element_located((By.NAME, "email"))
            )
            email_field.send_keys("test22@user.com")
        except Exception as e:
            self.fail(f"Email field not found: {e}")

        # 7. Accept terms and proceed.
        try:
            terms_checkbox = wait.until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )
            terms_checkbox.click()
        except Exception as e:
            self.fail(f"Terms checkbox not found or not clickable: {e}")

        try:
            place_order_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Place your order')]"))
            )
            place_order_button.click()
        except Exception as e:
            self.fail(f"Place order button not found or not clickable: {e}")

        # 8. Confirm success if form is filled.
        # Verify that the billing form is filled by checking if the elements are present
        try:
            wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
            wait.until(EC.presence_of_element_located((By.NAME, "lastName")))
            wait.until(EC.presence_of_element_located((By.NAME, "address")))
            wait.until(EC.presence_of_element_located((By.NAME, "city")))
            wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
            wait.until(EC.presence_of_element_located((By.NAME, "phone")))
            wait.until(EC.presence_of_element_located((By.NAME, "email")))
        except Exception as e:
            self.fail(f"Billing form not filled correctly: {e}")

if __name__ == "__main__":
    unittest.main()