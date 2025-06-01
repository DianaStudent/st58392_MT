import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")  # Replace with actual URL if different

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page and handle cookies
        try:
            accept_cookies_button = wait.until(EC.presence_of_element_located((
                By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found")

        # Step 2: Log in using credentials
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()

        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_field = driver.find_element(By.NAME, "loginPassword")
        login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")

        username_field.send_keys("test22@user.com")
        password_field.send_keys("test**11")
        login_button.click()

        # Step 3: Navigate back to the home page
        home_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Home")))
        home_button.click()

        # Step 4: Hover over the first product and add to cart
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-img a")))
        ActionChains(driver).move_to_element(first_product).perform()

        add_to_cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        add_to_cart_button.click()

        # Step 5: Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Step 6: Wait for the popup to become visible
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content")))

        # Step 7: Click "View cart" button inside the popup
        view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Step 8: On the cart page, click the "Proceed to Checkout" button
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Step 9: Fill out the billing form and accept terms
        company_field = wait.until(EC.presence_of_element_located((By.NAME, "company")))
        address_field = driver.find_element(By.NAME, "address")
        city_field = driver.find_element(By.NAME, "city")
        postal_code_field = driver.find_element(By.NAME, "postalCode")
        phone_field = driver.find_element(By.NAME, "phone")
        terms_checkbox = driver.find_element(By.NAME, "isAgree")

        company_field.send_keys("Comp1")
        address_field.send_keys("Street1")
        city_field.send_keys("Quebec")
        postal_code_field.send_keys("1234")
        phone_field.send_keys("1234567891")

        state_dropdown = driver.find_element(By.CSS_SELECTOR, ".billing-select select")
        for option in state_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == 'Quebec':
                option.click()
                break

        terms_checkbox.click()

        place_order_button = driver.find_element(By.XPATH, "//button[text()='Place your order']")

        # Validate that the form fields are filled
        self.assertTrue(company_field.get_attribute("value") == "Comp1", "Company name not set correctly")
        self.assertTrue(address_field.get_attribute("value") == "Street1", "Address not set correctly")
        self.assertTrue(city_field.get_attribute("value") == "Quebec", "City not set correctly")
        self.assertTrue(postal_code_field.get_attribute("value") == "1234", "Postal code not set correctly")
        self.assertTrue(phone_field.get_attribute("value") == "1234567891", "Phone not set correctly")

        # Step 10: Close any possible popups related to maps or warnings
        try:
            popup_close_button = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(@class, 'close') or @aria-label='Close']")))
            popup_close_button.click()
        except:
            print("No popups to close.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()