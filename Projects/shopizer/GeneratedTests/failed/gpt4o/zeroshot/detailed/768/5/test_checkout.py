from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))).click()

        # Go to login page
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
        account_button.click()
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Log in using credentials
        email_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        email_input.send_keys("test22@user.com")
        password_input = wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
        password_input.send_keys("test**11")
        login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
        login_button.click()

        # Navigate back to the home page
        logo = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".logo a")))
        logo.click()

        # Hover over the first product
        first_product = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".product-wrap-2")))[0]
        ActionChains(driver).move_to_element(first_product).perform()

        # Click the revealed "Add to cart" button
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, ".fa-shopping-cart")
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        # Wait for the popup to become visible
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content")))

        # Click "View cart" or similar button inside the popup
        view_cart_button = driver.find_element(By.LINK_TEXT, "View Cart")
        view_cart_button.click()

        # On the cart page, click the "Proceed to Checkout" button
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill out the billing form
        wait.until(EC.element_to_be_clickable((By.NAME, "company"))).send_keys("Comp1")
        wait.until(EC.element_to_be_clickable((By.NAME, "address"))).send_keys("Street1")
        wait.until(EC.element_to_be_clickable((By.NAME, "city"))).send_keys("Quebec")
        state_select = wait.until(EC.presence_of_element_located((By.NAME, "stateProvince")))
        for option in state_select.find_elements(By.TAG_NAME, 'option'):
            if "Quebec" in option.text:
                option.click()
                break
        wait.until(EC.element_to_be_clickable((By.NAME, "postalCode"))).send_keys("1234")
        wait.until(EC.element_to_be_clickable((By.NAME, "phone"))).send_keys("1234567891")
        terms_checkbox = wait.until(EC.element_to_be_clickable((By.NAME, "isAgree")))
        terms_checkbox.click()

        # Check assertion for successful form completion
        company_value = driver.find_element(By.NAME, "company").get_attribute("value")
        if not company_value or company_value != "Comp1":
            self.fail("Billing form is not properly filled.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()