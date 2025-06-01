import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):
    URL = "http://localhost/"
    EMAIL = "test22@user.com"
    PASSWORD = "test**11"

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get(self.URL)
        self.driver.set_window_size(1920, 1080)

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies if present
        try:
            cookie_accept_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_accept_btn.click()
        except Exception:
            print("Cookies notification not present or clickable")

        # Log in
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        login_btn = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_btn.click()

        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))

        username_input.send_keys(self.EMAIL)
        password_input.send_keys(self.PASSWORD)

        login_submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button")))
        login_submit_btn.click()

        # Navigate back to home
        driver.get(self.URL)

        # Hover over the first product and add to cart
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        ActionChains(driver).move_to_element(first_product).perform()

        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button")))
        add_to_cart_btn.click()

        # Click cart icon
        cart_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        # Wait for cart popup to become visible
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content")))

        # Click "View Cart"
        view_cart_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_btn.click()

        # On the cart page, click "Proceed to Checkout"
        proceed_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_btn.click()

        # Fill billing form
        wait.until(EC.presence_of_element_located((By.NAME, "firstName"))).send_keys("FirstName")
        wait.until(EC.presence_of_element_located((By.NAME, "lastName"))).send_keys("LastName")
        wait.until(EC.presence_of_element_located((By.NAME, "company"))).send_keys("Comp1")
        wait.until(EC.presence_of_element_located((By.NAME, "address"))).send_keys("Street1")
        wait.until(EC.presence_of_element_located((By.NAME, "city"))).send_keys("Quebec")

        country_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".billing-select select")))
        country_select.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Canada']"))).click()
        
        state_select = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".billing-select select")))
        state_select.click()
        wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Quebec']"))).click()

        wait.until(EC.presence_of_element_located((By.NAME, "postalCode"))).send_keys("1234")
        wait.until(EC.presence_of_element_located((By.NAME, "phone"))).send_keys("1234567891")

        # Agree to terms
        agree_terms_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))
        if not agree_terms_checkbox.is_selected():
            agree_terms_checkbox.click()

        # Verify billing form is filled
        if not driver.find_element(By.NAME, "firstName").get_attribute("value"):
            self.fail("Billing form is not filled properly")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()