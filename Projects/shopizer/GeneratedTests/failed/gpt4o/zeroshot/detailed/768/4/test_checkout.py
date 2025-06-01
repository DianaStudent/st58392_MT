from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        
        # Accept cookies if present
        try:
            accept_cookies = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies.click()
        except:
            pass  # If not present, proceed

        # Log in
        account_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_button.click()
        login_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()
        
        username_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        username_input.send_keys("test22@user.com")
        
        password_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
        password_input.send_keys("test**11")
        
        login_button = driver.find_element(By.XPATH, "//button[span='Login']")
        login_button.click()

        # Navigate back to the home page
        home_link = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_link.click()

        # Hover over the first product and click "Add to cart"
        product_image = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-img")))
        
        ActionChains(driver).move_to_element(product_image).perform()
        
        add_to_cart_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()
        
        # Wait for the popup to become visible
        cart_popup = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content")))
        
        # Click "View cart"
        view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()
        
        # On the cart page, click the "Proceed to Checkout" button
        proceed_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()
        
        # Fill out the billing form
        company_input = self.wait.until(EC.element_to_be_clickable((By.NAME, "company")))
        company_input.send_keys("Comp1")

        address_input = driver.find_element(By.NAME, "address")
        address_input.send_keys("Street1")

        city_input = driver.find_element(By.NAME, "city")
        city_input.send_keys("Quebec")

        region_dropdown = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//select/option[text()='Select a state']")))
        region_dropdown.click()
        
        region_option = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Quebec']")))
        region_option.click()

        postal_code_input = driver.find_element(By.NAME, "postalCode")
        postal_code_input.send_keys("1234")

        phone_input = driver.find_element(By.NAME, "phone")
        phone_input.send_keys("1234567891")

        terms_checkbox = self.wait.until(EC.element_to_be_clickable((By.NAME, "isAgree")))
        terms_checkbox.click()

        # Confirm success
        self.assertTrue(company_input.is_displayed(), "Billing form is not filled properly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()