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
            account_button = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
        except Exception as e:
            self.fail(f"Could not find or click account button: {e}")

        try:
            login_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/login']")))
            login_link.click()
        except Exception as e:
            self.fail(f"Could not find or click login link: {e}")

        try:
            username_field = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_field = self.wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Login')]")))

            username_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_button.click()

        except Exception as e:
            self.fail(f"Could not find or interact with login elements: {e}")

        # 3. Navigate back to the home page.
        try:
            home_link = self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/']")))
            home_link.click()
        except Exception as e:
            self.fail(f"Could not find or click home link: {e}")

        # 4. Hover over the first product.
        try:
            product_element = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]")))
            actions = ActionChains(self.driver)
            actions.move_to_element(product_element).perform()
        except Exception as e:
            self.fail(f"Could not find or hover over product: {e}")

        # 5. Click the revealed "Add to cart" button.
        try:
            add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click add to cart button: {e}")

        # 6. Click the cart icon to open the popup cart.
        try:
            cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
            cart_icon.click()
        except Exception as e:
            self.fail(f"Could not find or click cart icon: {e}")

        # 7. Click "View cart" button inside the popup.
        try:
            view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Could not find or click view cart button: {e}")

        # 8. On the cart page, click the "Proceed to Checkout" button.
        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except Exception as e:
            self.fail(f"Could not find or click checkout button: {e}")

        # 9. Fill out the billing form:
        try:
            company_field = self.wait.until(EC.presence_of_element_located((By.NAME, "company")))
            address_field = self.wait.until(EC.presence_of_element_located((By.NAME, "address")))
            city_field = self.wait.until(EC.presence_of_element_located((By.NAME, "city")))
            postal_code_field = self.wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
            phone_field = self.wait.until(EC.presence_of_element_located((By.NAME, "phone")))

            company_field.send_keys("Comp1")
            address_field.send_keys("Street1")
            city_field.send_keys("Quebec")
            postal_code_field.send_keys("1234")
            phone_field.send_keys("1234567891")

            # Select region/state from dropdown (use label-based matching)
            state_select = Select(self.wait.until(EC.presence_of_element_located((By.XPATH, "//select[@name='stateProvince']"))))
            state_select.select_by_visible_text("Quebec")

            # Accept terms checkbox
            terms_checkbox = self.wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='isAgree']")))
            terms_checkbox.click()

        except Exception as e:
            self.fail(f"Could not find or interact with billing form elements: {e}")

        # 10. Confirm success if form is filled.
        self.assertEqual(company_field.get_attribute("value"), "Comp1")
        self.assertEqual(address_field.get_attribute("value"), "Street1")
        self.assertEqual(city_field.get_attribute("value"), "Quebec")
        self.assertEqual(postal_code_field.get_attribute("value"), "1234")
        self.assertEqual(phone_field.get_attribute("value"), "1234567891")

if __name__ == "__main__":
    unittest.main()