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
        self.assertEqual(self.driver.current_url, "http://localhost/")

        # 2. Log in using credentials.
        try:
            account_button = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            login_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
            )
            login_link.click()

            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Login')]"))
            )

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except NoSuchElementException as e:
            self.fail(f"Login failed: {e}")

        # 3. Navigate back to the home page.
        home_link = self.wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/']"))
        )
        home_link.click()

        # 4. Hover over the first product.
        try:
            first_product = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]"))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(first_product).perform()
        except NoSuchElementException as e:
            self.fail(f"Could not hover over the first product: {e}")

        # 5. Click the revealed "Add to cart" button.
        try:
            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except NoSuchElementException as e:
            self.fail(f"Add to cart button not found: {e}")

        # 6. Click the cart icon to open the popup cart.
        try:
            cart_icon = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except NoSuchElementException as e:
            self.fail(f"Cart icon not found: {e}")

        # 7. Wait for the popup to become visible.
        self.wait.until(
            EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content.active"))
        )

        # 8. Click "View Cart" button inside the popup.
        try:
            view_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'View Cart')]"))
            )
            view_cart_button.click()
        except NoSuchElementException as e:
            self.fail(f"View Cart button not found: {e}")

        # 9. On the cart page, click the "Proceed to Checkout" button.
        try:
            checkout_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Proceed to Checkout')]"))
            )
            checkout_button.click()
        except NoSuchElementException as e:
            self.fail(f"Proceed to Checkout button not found: {e}")

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
                EC.presence_of_element_located((By.XPATH, "//label[contains(text(), 'State')]/following-sibling::select"))
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

            for option in state_select.find_elements(By.TAG_NAME, 'option'):
                if option.text == 'Quebec':
                    option.click()
                    break

            postal_code_input.send_keys("1234")
            phone_input.send_keys("1234567891")

            terms_checkbox.click()

            # 11. Confirm success if form is filled.
            self.assertEqual(company_input.get_attribute("value"), "Comp1")
            self.assertEqual(address_input.get_attribute("value"), "Street1")
            self.assertEqual(city_input.get_attribute("value"), "Quebec")
            self.assertTrue(terms_checkbox.is_selected())

        except NoSuchElementException as e:
            self.fail(f"Could not fill out the billing form: {e}")

if __name__ == "__main__":
    unittest.main()