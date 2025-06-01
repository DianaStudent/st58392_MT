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
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
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
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Login')]"))
            )

            username_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_button.click()

        except:
            self.fail("Login form not found or could not be filled")

        # Navigate back to home page
        driver.get("http://localhost/")

        # Add to cart
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']"))
            )
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
            )

            action = ActionChains(driver)
            action.move_to_element(first_product).perform()
            add_to_cart_button.click()

        except:
            self.fail("Could not add product to cart")

        # Add second product to cart
        try:
            second_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//div[@class='product-wrap-2 mb-25']"))
            )
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][2]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
            )

            action = ActionChains(driver)
            action.move_to_element(second_product).perform()
            add_to_cart_button.click()

        except:
            self.fail("Could not add second product to cart")

        # Open cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found")

        # View cart
        try:
            view_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/cart' and contains(text(),'View Cart')]"))
            )
            view_cart_button.click()
        except:
            self.fail("View Cart button not found")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/checkout' and contains(text(),'Proceed to Checkout')]"))
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
            state_select = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'State')]/following-sibling::select"))
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

            select = Select(state_select)
            select.select_by_value("QC")

            postal_code_field.send_keys("1234")
            phone_field.send_keys("1234567891")
            terms_checkbox.click()
        except:
            self.fail("Billing form not found or could not be filled")

        # Verify form is filled
        try:
            self.assertEqual(company_field.get_attribute("value"), "Comp1")
            self.assertEqual(address_field.get_attribute("value"), "Street1")
            self.assertEqual(city_field.get_attribute("value"), "Quebec")
            self.assertEqual(postal_code_field.get_attribute("value"), "1234")
            self.assertEqual(phone_field.get_attribute("value"), "1234567891")
            self.assertTrue(terms_checkbox.is_selected())
        except:
            self.fail("Billing form was not filled correctly")

if __name__ == "__main__":
    unittest.main()