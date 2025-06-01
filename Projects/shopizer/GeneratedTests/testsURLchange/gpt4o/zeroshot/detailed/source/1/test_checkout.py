import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost/")
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        try:
            accept_cookies_button = driver.find_element(By.ID, "rcc-confirm-button")
            if accept_cookies_button.is_displayed():
                accept_cookies_button.click()
        except:
            pass  # If not present, move on

        # Log in
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pe-7s-user-female")))
        account_button.click()

        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = driver.find_element(By.NAME, "loginPassword")
        login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        
        self.assertIsNotNone(username_field)
        self.assertIsNotNone(password_field)
        self.assertIsNotNone(login_button)

        username_field.send_keys("test22@user.com")
        password_field.send_keys("test**11")
        login_button.click()

        # Navigate back to the home page
        driver.get("http://localhost/")

        # Hover over the first product
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        self.assertIsNotNone(first_product)
        
        ActionChains(driver).move_to_element(first_product).perform()
        
        # Click "Add to cart"
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
        add_to_cart_button.click()
        
        # Open cart popup and wait
        cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        cart_button.click()

        cart_popup = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))
        self.assertIsNotNone(cart_popup)

        # Click "View Cart" or similar
        view_cart_button = cart_popup.find_element(By.LINK_TEXT, "View Cart")
        view_cart_button.click()

        # Click "Proceed to Checkout" on the cart page
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill out the billing form
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        company_field = driver.find_element(By.NAME, "company")
        address_field = driver.find_element(By.NAME, "address")
        city_field = driver.find_element(By.NAME, "city")
        postal_code_field = driver.find_element(By.NAME, "postalCode")
        phone_field = driver.find_element(By.NAME, "phone")
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        
        self.assertIsNotNone(first_name_field)
        self.assertIsNotNone(company_field)
        self.assertIsNotNone(address_field)
        self.assertIsNotNone(city_field)
        self.assertIsNotNone(postal_code_field)
        self.assertIsNotNone(phone_field)
        self.assertIsNotNone(terms_checkbox)

        first_name_field.send_keys("Test")
        company_field.send_keys("Comp1")
        address_field.send_keys("Street1")
        city_field.send_keys("Quebec")
        postal_code_field.send_keys("1234")
        phone_field.send_keys("1234567891")

        # Select region/state using visible text
        state_dropdown = driver.find_element(By.XPATH, "//select/option[. = 'Quebec']")
        state_dropdown.click()

        # Accept terms and conditions
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        # Ensure no interrupts like maps popups (handled implicitly by the test's nature)

        # Validate billing form fill completion
        filled_company = driver.find_element(By.NAME, "company").get_attribute("value")
        if filled_company != "Comp1":
            self.fail("Billing form not correctly filled.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()