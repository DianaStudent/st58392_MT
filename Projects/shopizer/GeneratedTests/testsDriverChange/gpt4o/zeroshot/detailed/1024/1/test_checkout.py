import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestCheckoutProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        actions = ActionChains(driver)

        # Accept cookies if the button is present
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception:
            self.fail("Failed to locate or click Accept cookies button.")

        # Navigate to login page
        account_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female"))
        )
        account_button.click()
        
        login_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        # Login
        username_field = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = driver.find_element(By.CLASS_NAME, "user-password")
        
        username_field.send_keys("test22@user.com")
        password_field.send_keys("test**11")
        
        login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        login_button.click()

        # Navigate back to Home Page
        logo = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".logo a"))
        )
        logo.click()

        # Hover over the first product to reveal "Add to cart" button
        first_product = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        actions.move_to_element(first_product).perform()

        add_to_cart_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']"))
        )
        add_to_cart_button.click()

        # Click cart icon to open the popup cart
        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_icon.click()

        # Wait for the cart popup to become visible
        popup_cart = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
        )

        view_cart_button = popup_cart.find_element(By.LINK_TEXT, "View Cart")
        view_cart_button.click()

        # On the cart page, proceed to checkout
        proceed_to_checkout_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
        )
        proceed_to_checkout_button.click()

        # Fill out the billing form
        company_field = wait.until(
            EC.presence_of_element_located((By.NAME, "company"))
        )
        company_field.send_keys("Comp1")

        address_field = driver.find_element(By.NAME, "address")
        address_field.send_keys("Street1")

        city_field = driver.find_element(By.NAME, "city")
        city_field.send_keys("Quebec")

        # Select region/state
        state_dropdown = driver.find_element(By.XPATH, "//select[option[text()='Select a state']]")
        state_dropdown.click()
        quebec_option = state_dropdown.find_element(By.XPATH, "//option[@value='QC']")
        quebec_option.click()

        postal_code_field = driver.find_element(By.NAME, "postalCode")
        postal_code_field.send_keys("1234")

        phone_field = driver.find_element(By.NAME, "phone")
        phone_field.send_keys("1234567891")

        # Accept terms and conditions checkbox
        accept_terms_checkbox = driver.find_element(By.NAME, "isAgree")
        accept_terms_checkbox.click()

        # Confirm success if the form is filled
        self.assertTrue(company_field.get_attribute('value'), "Comp1")
        self.assertTrue(address_field.get_attribute('value'), "Street1")
        self.assertTrue(city_field.get_attribute('value'), "Quebec")
        self.assertTrue(postal_code_field.get_attribute('value'), "1234")
        self.assertTrue(phone_field.get_attribute('value'), "1234567891")
        self.assertTrue(accept_terms_checkbox.is_selected(), "Accept terms checkbox is not selected.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()