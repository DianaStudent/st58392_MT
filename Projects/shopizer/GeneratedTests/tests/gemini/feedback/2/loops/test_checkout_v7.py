import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

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
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            ).click()
        except TimeoutException:
            pass

        # Login
        try:
            account_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
            login_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            email_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']"))
            )

            email_input.send_keys(self.email)
            password_input.send_keys(self.password)
            login_button.click()
        except TimeoutException:
            self.fail("Login failed: Could not find login elements.")

        # Navigate back to home page
        try:
            home_link = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Home"))
            )
            home_link.click()
        except TimeoutException:
            self.fail("Could not navigate back to home page.")

        # Add product to cart
        try:
            first_product = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2"))
            )
            actions = ActionChains(driver)
            actions.move_to_element(first_product).perform()

            add_to_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
            )
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Could not add product to cart.")

        # Open cart popup
        try:
            cart_icon = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()

            # View cart
            view_cart_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except TimeoutException:
            self.fail("Could not open cart popup and view cart.")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except TimeoutException:
            self.fail("Could not proceed to checkout.")

        # Fill billing form
        try:
            company_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "company"))
            )
            address_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            state_select = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select"))
            )
            postal_code_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            terms_checkbox = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.NAME, "isAgree"))
            )

            company_input.send_keys("Comp1")
            address_input.send_keys("Street1")
            city_input.send_keys("Quebec")

            # Select Quebec from the state dropdown
            state_select.click()
            state_option = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[text()='State']/following-sibling::select/option[@value='QC']"))
            )
            state_option.click()

            postal_code_input.send_keys("1234")
            phone_input.send_keys("1234567891")
            terms_checkbox.click()
        except TimeoutException:
            self.fail("Could not fill billing form.")

        # Verify form is filled
        try:
            self.assertIsNotNone(company_input)
            self.assertEqual(company_input.get_attribute("value"), "Comp1")
        except AssertionError:
            self.fail("Company verification failed.")
        try:
            self.assertIsNotNone(address_input)
            self.assertEqual(address_input.get_attribute("value"), "Street1")
        except AssertionError:
            self.fail("Address verification failed.")
        try:
            self.assertIsNotNone(city_input)
            self.assertEqual(city_input.get_attribute("value"), "Quebec")
        except AssertionError:
            self.fail("City verification failed.")
        try:
            self.assertIsNotNone(postal_code_input)
            self.assertEqual(postal_code_input.get_attribute("value"), "1234")
        except AssertionError:
            self.fail("Postal code verification failed.")
        try:
            self.assertIsNotNone(phone_input)
            self.assertEqual(phone_input.get_attribute("value"), "1234567891")
        except AssertionError:
            self.fail("Phone verification failed.")
        try:
            self.assertIsNotNone(terms_checkbox)
            self.assertTrue(terms_checkbox.is_selected())
        except AssertionError:
            self.fail("Terms verification failed.")

if __name__ == "__main__":
    unittest.main()