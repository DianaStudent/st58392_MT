from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Accept cookies if present
        try:
            accept_cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            print("No cookies prompt found.", str(e))
        
        # Log in
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()
        
        login_form = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='username']")))
        login_form.send_keys("test22@user.com")
        password_form = driver.find_element(By.CSS_SELECTOR, "input[name='loginPassword']")
        password_form.send_keys("test**11")
        login_button = driver.find_element(By.XPATH, "//button/span[contains(text(),'Login')]")
        login_button.click()

        # Confirm login by checking user profile presence
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-profile")))
        
        # Navigate back to the home page
        driver.get("http://localhost/")

        # Hover over the first product and add to cart
        product_card = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product-wrap-2")))
        actions = ActionChains(driver)
        actions.move_to_element(product_card).perform()
        
        add_to_cart_button = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//div[contains(@class, 'product-action-2')]/button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        # Wait for the popup to become visible and click "View cart"
        view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # On the cart page, click the "Proceed to Checkout" button
        proceed_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_checkout_button.click()

        # Fill out the billing form
        company_input = wait.until(EC.presence_of_element_located((By.NAME, "company")))
        company_input.send_keys("Comp1")
        
        address_input = driver.find_element(By.ID, "autocomplete")
        address_input.send_keys("Street1")
        
        city_input = driver.find_element(By.NAME, "city")
        city_input.send_keys("Quebec")
        
        state_dropdown = driver.find_element(By.NAME, "billing-select")
        state_dropdown.select_by_visible_text("Quebec")
        
        postal_code_input = driver.find_element(By.NAME, "postalCode")
        postal_code_input.send_keys("1234")
        
        phone_input = driver.find_element(By.NAME, "phone")
        phone_input.send_keys("1234567891")
        
        # Accept terms
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        terms_checkbox.click()
        
        # Confirm form is filled
        self.assertNotEqual(company_input.get_attribute("value"), "", "Company input is not filled!")
        self.assertNotEqual(address_input.get_attribute("value"), "", "Address input is not filled!")
        self.assertNotEqual(city_input.get_attribute("value"), "", "City input is not filled!")
        self.assertNotEqual(postal_code_input.get_attribute("value"), "", "Postal Code input is not filled!")
        
        # Map warning or popups handling
        try:
            map_popup_close = driver.find_element(By.CLASS_NAME, "close-class-or-selector")
            map_popup_close.click()
        except Exception as e:
            pass # No popup found

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()