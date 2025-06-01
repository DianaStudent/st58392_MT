from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
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
            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()
        except:
            pass

        # Login
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()

            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )

            email_input.send_keys(self.email)
            password_input.send_keys(self.password)
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
            
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']"))
            )

            ActionChains(driver).move_to_element(first_product).perform()
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {e}")

        # Open cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except Exception as e:
            self.fail(f"Opening cart popup failed: {e}")

        # View cart
        try:
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Viewing cart failed: {e}")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except Exception as e:
            self.fail(f"Proceeding to checkout failed: {e}")

        # Fill billing form
        try:
            company_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "company"))
            )
            address_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select"))
            )
            postal_code_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "isAgree"))
            )

            company_input.send_keys("Comp1")
            address_input.send_keys("Street1")
            city_input.send_keys("Quebec")
            Select(state_select).select_by_value("QC")
            postal_code_input.send_keys("1234")
            phone_input.send_keys("1234567891")
            terms_checkbox.click()
        except Exception as e:
            self.fail(f"Filling billing form failed: {e}")

        # Verify form is filled
        try:
            self.assertEqual(company_input.get_attribute("value"), "Comp1")
            self.assertEqual(address_input.get_attribute("value"), "Street1")
            self.assertEqual(city_input.get_attribute("value"), "Quebec")
            self.assertEqual(postal_code_input.get_attribute("value"), "1234")
            self.assertEqual(phone_input.get_attribute("value"), "1234567891")
        except Exception as e:
            self.fail(f"Verifying billing form failed: {e}")

if __name__ == "__main__":
    unittest.main()