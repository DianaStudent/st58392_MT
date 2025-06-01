import unittest
import time
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
        self.driver.maximize_window()
        self.url = "http://localhost/"
        self.credentials = {"email": "test22@user.com", "password": "test**11"}

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.url)

        # Accept cookies
        try:
            cookie_accept_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_accept_button.click()
        except:
            pass

        # Login
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            # Wait for the dropdown to be visible and the link to be clickable
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(login_link)).click()
        except:
            self.fail("Login link not found or not clickable")

        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Login')]"))
            )

            username_field.send_keys(self.credentials["email"])
            password_field.send_keys(self.credentials["password"])
            login_button.click()

        except:
            self.fail("Login form not found or fields missing")

        # Navigate back to home page
        driver.get(self.url)

        # Add product to cart
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
            )

            add_to_cart_button = first_product.find_element(By.CLASS_NAME, "active")
            ActionChains(driver).move_to_element(first_product).perform()
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button)).click()
        except:
            self.fail("Could not add product to cart")

        # Open cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(cart_icon))
            cart_icon.click()
        except Exception as e:
            self.fail(f"Cart icon not found or not clickable: {e}")

        # View cart
        try:
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except:
            self.fail("View Cart button not found")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Proceed to Checkout button not found")

        # Fill billing form
        try:
            company_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "company"))
            )
            address_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            state_select_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select"))
            )
            state_select = Select(state_select_element)
            postal_code_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "isAgree"))
            )

            company_field.send_keys("Comp1")
            address_field.send_keys("Street1")
            city_field.send_keys("Quebec")
            state_select.select_by_visible_text("Quebec")
            postal_code_field.send_keys("1234")
            phone_field.send_keys("1234567891")
            terms_checkbox.click()

        except:
            self.fail("Billing form not found or fields missing")

        # Verify form is filled
        try:
            self.assertEqual(company_field.get_attribute("value"), "Comp1")
            self.assertEqual(address_field.get_attribute("value"), "Street1")
            self.assertEqual(city_field.get_attribute("value"), "Quebec")
            self.assertEqual(state_select.first_selected_option.text, "Quebec")
            self.assertEqual(postal_code_field.get_attribute("value"), "1234")
            self.assertEqual(phone_field.get_attribute("value"), "1234567891")
            self.assertTrue(terms_checkbox.is_selected())

        except:
            self.fail("Billing form verification failed")

if __name__ == "__main__":
    unittest.main()