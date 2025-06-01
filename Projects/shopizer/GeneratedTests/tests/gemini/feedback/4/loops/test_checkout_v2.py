import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.url = "http://localhost/"
        self.email = "test22@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.url)

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
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

            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
            )

            email_field.send_keys(self.email)
            password_field.send_keys(self.password)
            login_button.click()
        except Exception as e:
            self.fail(f"Login failed: {e}")

        # Navigate back to home page
        driver.get(self.url)

        # Add product to cart
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]"))
            )

            add_to_cart_button = WebDriverWait(first_product, 20).until(
                EC.presence_of_element_located((By.XPATH, ".//button[@title='Add to cart']"))
            )

            action = ActionChains(driver)
            action.move_to_element(first_product).perform()

            WebDriverWait(driver, 20).until(EC.element_to_be_clickable(add_to_cart_button))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {e}")

        # Open cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()

            view_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Opening cart popup or navigating to cart page failed: {e}")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Proceeding to checkout failed: {e}")

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
            state_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-lg-6 col-md-6']/div[@class='billing-select mb-20']/select"))
            )
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

            # Select state from dropdown
            for option in state_dropdown.find_elements(By.TAG_NAME, 'option'):
                if option.text == 'Quebec':
                    option.click()
                    break

            postal_code_field.send_keys("1234")
            phone_field.send_keys("1234567891")

            # Scroll to the checkbox
            driver.execute_script("arguments[0].scrollIntoView();", terms_checkbox)
            terms_checkbox.click()

        except Exception as e:
            self.fail(f"Filling billing form failed: {e}")

        # Verify that the billing form is filled
        try:
            self.assertEqual(company_field.get_attribute("value"), "Comp1")
            self.assertEqual(address_field.get_attribute("value"), "Street1")
            self.assertEqual(city_field.get_attribute("value"), "Quebec")
            self.assertEqual(postal_code_field.get_attribute("value"), "1234")
            self.assertEqual(phone_field.get_attribute("value"), "1234567891")
            self.assertTrue(terms_checkbox.is_selected())
        except Exception as e:
            self.fail(f"Verification failed: {e}")

if __name__ == "__main__":
    unittest.main()