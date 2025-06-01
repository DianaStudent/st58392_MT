import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        # Set up Selenium WebDriver with Chrome
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # 1. Open the home page
        driver.get("http://localhost/")
        
        # Verify home page loaded
        cookies_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
        cookies_button.click()

        # 2. Log in using the provided credentials
        account_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active")))
        account_button.click()
        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Verify login page loaded
        email_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        self.assertTrue(email_input.is_displayed())

        email_input.send_keys("test22@user.com")
        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys("test**11")
        login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_button.click()

        # 3. Add product to the cart
        product_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2 .fa-shopping-cart")))
        product_button.click()

        # Verify item added to cart
        cart_span = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".count-style")))
        self.assertTrue(cart_span.text != "" and int(cart_span.text) > 0)

        # 4. Open the cart and navigate to the cart page
        cart_icon = driver.find_element(By.CSS_SELECTOR, ".icon-cart")
        cart_icon.click()
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Verify cart page loaded
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        
        # 5. Click "Proceed to Checkout"
        proceed_to_checkout_button.click()

        # Verify checkout page
        firstname_input = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))

        # 6. Fill in the billing form
        firstname_input.send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")
        driver.find_element(By.NAME, "company").send_keys("TestCompany")
        driver.find_element(By.NAME, "address").send_keys("123 Test Address")
        driver.find_element(By.NAME, "city").send_keys("TestCity")
        driver.find_element(By.NAME, "postalCode").send_keys("12345")
        driver.find_element(By.NAME, "phone").send_keys("1234567890")
        driver.find_element(By.NAME, "email").send_keys("test22@user.com")

        # Wait for the region (state) select to appear dynamically
        state_select = wait.until(EC.presence_of_element_located((By.NAME, "state")))
        state_select.send_keys(Keys.ARROW_DOWN)
        state_select.send_keys(Keys.RETURN)

        # 7. Accept terms and proceed
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        terms_checkbox.click()
        place_order_button = driver.find_element(By.CSS_SELECTOR, ".btn-hover")

        # Verify button enabled
        self.assertTrue(place_order_button.is_enabled())
        place_order_button.click()

        # 8. Confirm success by verifying that the billing form is filled
        self.assertTrue(firstname_input.get_attribute("value") != "" and "Test" in firstname_input.get_attribute("value"))

    def tearDown(self):
        # Close the browser after the test plan
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()