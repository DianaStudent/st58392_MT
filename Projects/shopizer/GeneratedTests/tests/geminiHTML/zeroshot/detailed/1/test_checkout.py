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
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # 1. Open the home page.
        # Already done in setUp

        # 2. Log in using credentials.
        try:
            account_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            login_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/login']")))
            login_link.click()

            email_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Login')]")))

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except TimeoutException:
            self.fail("Login failed: Could not find login elements.")

        # 3. Navigate back to the home page.
        home_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/']")))
        home_link.click()

        # 4. Hover over the first product.
        try:
            first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]")))
            actions = ActionChains(self.driver)
            actions.move_to_element(first_product).perform()
        except TimeoutException:
            self.fail("Could not find the first product.")

        # 5. Click the revealed "Add to cart" button.
        try:
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Could not find or click the 'Add to cart' button.")

        # 6. Click the cart icon to open the popup cart.
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
            cart_icon.click()
        except TimeoutException:
            self.fail("Could not find or click the cart icon.")

        # 7. Wait for the popup to become visible.
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content.active")))

        # 8. Click "View cart" or similar button inside the popup.
        try:
            view_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View Cart')]")))
            view_cart_button.click()
        except TimeoutException:
            self.fail("Could not find or click the 'View Cart' button in the popup.")

        # 9. On the cart page, click the "Proceed to Checkout" button.
        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Proceed to Checkout')]")))
            checkout_button.click()
        except TimeoutException:
            self.fail("Could not find or click the 'Proceed to Checkout' button on the cart page.")

        # 10. Fill out the billing form:
        try:
            company_input = self.wait.until(EC.presence_of_element_located((By.NAME, "company")))
            address_input = self.wait.until(EC.presence_of_element_located((By.NAME, "address")))
            city_input = self.wait.until(EC.presence_of_element_located((By.NAME, "city")))
            state_select = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'State')]/following-sibling::select")))
            postal_code_input = self.wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
            phone_input = self.wait.until(EC.presence_of_element_located((By.NAME, "phone")))
            terms_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))

            company_input.send_keys("Comp1")
            address_input.send_keys("Street1")
            city_input.send_keys("Quebec")

            # Select Quebec from the state dropdown
            for option in state_select.find_elements(By.TAG_NAME, 'option'):
                if option.text == 'Quebec':
                    option.click()
                    break

            postal_code_input.send_keys("1234")
            phone_input.send_keys("1234567891")

            # Accept terms checkbox
            terms_checkbox.click()

        except TimeoutException:
            self.fail("Could not find billing form elements.")

        # 11. Wait for any maps popups or warnings and close them.
        # No maps or warnings to handle based on the provided HTML

        # 12. Confirm success if form is filled.
        self.assertEqual(company_input.get_attribute("value"), "Comp1", "Company not filled")
        self.assertEqual(address_input.get_attribute("value"), "Street1", "Address not filled")
        self.assertEqual(city_input.get_attribute("value"), "Quebec", "City not filled")
        self.assertEqual(postal_code_input.get_attribute("value"), "1234", "Postal code not filled")
        self.assertEqual(phone_input.get_attribute("value"), "1234567891", "Phone not filled")
        self.assertTrue(terms_checkbox.is_selected(), "Terms not accepted")

if __name__ == "__main__":
    unittest.main()