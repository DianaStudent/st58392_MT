import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
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
            account_button = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            login_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()

            username_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Login')]"))
            )

            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()

        except NoSuchElementException as e:
            self.fail(f"Login failed: {e}")

        # 3. Navigate back to the home page.
        self.driver.get("http://localhost/")

        # 4. Hover over the first product.
        try:
            first_product = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]"))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(first_product).perform()

            # 5. Click the revealed "Add to cart" button.
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']"))
            )
            add_to_cart_button.click()

        except NoSuchElementException as e:
            self.fail(f"Could not add product to cart: {e}")

        # 6. Click the cart icon to open the popup cart.
        try:
            cart_icon = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()

            # 7. Wait for the popup to become visible.
            self.wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content.active"))
            )

            # 8. Click "View Cart" button inside the popup.
            view_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()

        except NoSuchElementException as e:
            self.fail(f"Could not navigate to cart: {e}")

        # 9. On the cart page, click the "Proceed to Checkout" button.
        try:
            checkout_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()

        except NoSuchElementException as e:
            self.fail(f"Could not navigate to checkout: {e}")

        # 10. Fill out the billing form:
        try:
            company_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "company"))
            )
            address_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            state_select = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select"))
            )
            postal_code_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            terms_checkbox = self.wait.until(
                EC.presence_of_element_located((By.NAME, "isAgree"))
            )

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
            terms_checkbox.click()

        except NoSuchElementException as e:
            self.fail(f"Could not fill billing form: {e}")

        # 11. Confirm success if form is filled.
        self.assertTrue(company_input.get_attribute("value") == "Comp1", "Company not filled")
        self.assertTrue(address_input.get_attribute("value") == "Street1", "Address not filled")
        self.assertTrue(city_input.get_attribute("value") == "Quebec", "City not filled")
        self.assertTrue(postal_code_input.get_attribute("value") == "1234", "Postal code not filled")
        self.assertTrue(phone_input.get_attribute("value") == "1234567891", "Phone not filled")
        self.assertTrue(terms_checkbox.is_selected(), "Terms not accepted")

if __name__ == "__main__":
    unittest.main()