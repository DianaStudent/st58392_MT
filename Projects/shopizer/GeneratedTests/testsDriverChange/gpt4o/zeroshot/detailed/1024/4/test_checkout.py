import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        cookies_accept_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookies_accept_button.click()

        # Log in
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
        account_button.click()

        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))

        username_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")

        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()

        # Navigate back to home page
        logo = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".logo a")))
        logo.click()

        # Hover over the first product
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        ActionChains(driver).move_to_element(first_product).perform()

        # Click "Add to cart" button
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".fa-shopping-cart")))
        add_to_cart_button.click()

        # Open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Wait for popup to become visible
        popup_cart = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Click "View cart"
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Click "Proceed to Checkout"
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill out the billing form
        company_input = wait.until(EC.presence_of_element_located((By.NAME, "company")))
        address_input = wait.until(EC.presence_of_element_located((By.NAME, "address")))
        city_input = wait.until(EC.presence_of_element_located((By.NAME, "city")))
        postal_code_input = wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
        phone_input = wait.until(EC.presence_of_element_located((By.NAME, "phone")))

        company_input.send_keys("Comp1")
        address_input.send_keys("Street1")
        city_input.send_keys("Quebec")
        postal_code_input.send_keys("1234")
        phone_input.send_keys("1234567891")

        # Select region/state from the dropdown
        state_dropdown = wait.until(EC.element_to_be_clickable((By.NAME, "state")))
        state_dropdown.click()
        quebec_option = wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Quebec']")))
        quebec_option.click()

        # Accept terms checkbox
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.NAME, "isAgree")))
        terms_checkbox.click()

        # Wait for any maps popups or warnings and close them
        try:
            map_close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pac-item")))
            map_close_button.click()
        except:
            pass

        # Confirm success if form is filled
        for element in [company_input, address_input, city_input, postal_code_input, phone_input, terms_checkbox]:
            self.assertTrue(element.get_attribute('value'), "Form field not filled properly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()