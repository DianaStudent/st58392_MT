import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost") # Update with your home page URL
        self.driver.implicitly_wait(20)
    
    def test_checkout_process(self):
        driver = self.driver
        
        # Accept cookies if present
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except Exception as e:
            self.fail("Cookie consent button not found or issue in clicking it.")
        
        # Log in
        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_button.click()
        
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()
        
        email_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = driver.find_element(By.NAME, "loginPassword")
        login_button = driver.find_element(By.CSS_SELECTOR, ".button-box button[type='submit']")
        
        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()
        
        # Add product to cart
        product_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@title='Add to cart']"))
        )
        product_button.click()

        # Open cart
        cart_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
        )
        cart_icon.click()
        
        view_cart_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "View Cart"))
        )
        view_cart_link.click()
        
        # Proceed to checkout
        proceed_to_checkout_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))
        )
        proceed_to_checkout_link.click()
        
        # Fill in the billing form
        first_name_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "firstName"))
        )
        last_name_input = driver.find_element(By.NAME, "lastName")
        address_input = driver.find_element(By.NAME, "address")
        city_input = driver.find_element(By.NAME, "city")
        postal_code_input = driver.find_element(By.NAME, "postalCode")
        phone_input = driver.find_element(By.NAME, "phone")
        email_input = driver.find_element(By.NAME, "email")
        
        first_name_input.send_keys("Test")
        last_name_input.send_keys("User")
        address_input.send_keys("123 Test Street")
        city_input.send_keys("Test City")
        postal_code_input.send_keys("12345")
        phone_input.send_keys("1234567890")
        email_input.send_keys("test22@user.com")
        
        # Wait for region select to appear and choose the first option
        region_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "select[name='state']"))
        )
        region_select.click()  # Click to open dropdown
        region_option = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//option[@value='QC']"))
        )
        region_option.click()

        # Accept terms and place order
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        place_order_button = driver.find_element(By.CSS_SELECTOR, ".place-order button[type='button']")
        
        terms_checkbox.click()
        place_order_button.click()
        
        # Verify the success of form submission by checking input fields are filled
        self.assertTrue(first_name_input.get_attribute("value"), "First name is not filled.")
        self.assertTrue(last_name_input.get_attribute("value"), "Last name is not filled.")
        self.assertTrue(address_input.get_attribute("value"), "Address is not filled.")
        self.assertTrue(city_input.get_attribute("value"), "City is not filled.")
        self.assertTrue(postal_code_input.get_attribute("value"), "Postal code is not filled.")
        self.assertTrue(phone_input.get_attribute("value"), "Phone is not filled.")
        self.assertTrue(email_input.get_attribute("value"), "Email is not filled.")
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()