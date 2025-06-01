import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")  # Run Chrome in headless mode
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page.
        self.assertEqual(driver.current_url, "http://localhost/")

        # 2. Log in using credentials.
        try:
            account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            login_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[text()='Login']")))
            login_link.click()

            email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
            login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Login')]")))

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except Exception as e:
            self.fail(f"Login failed: {e}")

        # 3. Navigate back to the home page.
        driver.get("http://localhost/")
        self.assertEqual(driver.current_url, "http://localhost/")

        # 4. Hover over the first product.
        try:
            first_product = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]")))
            actions = ActionChains(driver)
            actions.move_to_element(first_product).perform()

            # 5. Click the revealed "Add to cart" button.
            add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']")))
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {e}")
        
        # 6. Click the cart icon to open the popup cart.
        try:
            cart_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "icon-cart")))
            cart_icon.click()
        except Exception as e:
            self.fail(f"Failed to click cart icon: {e}")

        # 7. Wait for the popup to become visible.
        try:
            wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content.active")))
        except Exception as e:
            self.fail(f"Cart popup did not become visible: {e}")

        # 8. Click "View Cart" button inside the popup.
        try:
            view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to click 'View Cart' button: {e}")

        # 9. On the cart page, click the "Proceed to Checkout" button.
        try:
            checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except Exception as e:
            self.fail(f"Failed to click 'Proceed to Checkout' button: {e}")

        # 10. Fill out the billing form:
        try:
            company_input = wait.until(EC.presence_of_element_located((By.NAME, "company")))
            address_input = wait.until(EC.presence_of_element_located((By.NAME, "address")))
            city_input = wait.until(EC.presence_of_element_located((By.NAME, "city")))
            state_select = wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select")))
            postal_code_input = wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
            phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))
            terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))

            company_input.send_keys("Comp1")
            address_input.send_keys("Street1")
            city_input.send_keys("Quebec")
            
            # Select region/state from dropdown (use label-based matching)
            for option in state_select.find_elements(By.TAG_NAME, 'option'):
                if option.text == 'Quebec':
                    option.click()
                    break
            
            postal_code_input.send_keys("1234")
            phone_input.send_keys("1234567891")
            terms_checkbox.click()
        except Exception as e:
            self.fail(f"Failed to fill out billing form: {e}")

        # 11. Confirm success if form is filled.
        self.assertEqual(company_input.get_attribute("value"), "Comp1")
        self.assertEqual(address_input.get_attribute("value"), "Street1")
        self.assertEqual(city_input.get_attribute("value"), "Quebec")
        self.assertEqual(postal_code_input.get_attribute("value"), "1234")
        self.assertEqual(phone_input.get_attribute("value"), "1234567891")
        self.assertTrue(terms_checkbox.is_selected())

if __name__ == "__main__":
    unittest.main()