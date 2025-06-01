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
            accept_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
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
                EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        try:
            email_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Login')]"))
            )
            email_input.send_keys(self.email)
            password_input.send_keys(self.password)
            login_button.click()
        except:
            self.fail("Login form not found or could not be filled")

        # Navigate to home page
        driver.get(self.url)

        # Add product to cart
        try:
            first_product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']"))
            )
            actions = ActionChains(driver)
            actions.move_to_element(first_product).perform()
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except:
            self.fail("Could not add product to cart")

        # Open cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except:
            self.fail("Cart icon not found")

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
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'State')]/following-sibling::select"))
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

            select = Select(state_select)
            select.select_by_value("QC")

            postal_code_input.send_keys("1234")
            phone_input.send_keys("1234567891")
            terms_checkbox.click()

        except:
            self.fail("Billing form not found or could not be filled")

        # Verify form is filled
        try:
            self.assertEqual(company_input.get_attribute("value"), "Comp1")
            self.assertEqual(address_input.get_attribute("value"), "Street1")
            self.assertEqual(city_input.get_attribute("value"), "Quebec")
            self.assertEqual(postal_code_input.get_attribute("value"), "1234")
            self.assertEqual(phone_input.get_attribute("value"), "1234567891")
            self.assertTrue(terms_checkbox.is_selected())
        except:
            self.fail("Billing form was not filled correctly")

if __name__ == "__main__":
    unittest.main()