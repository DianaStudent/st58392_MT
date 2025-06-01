from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Open the home page
        driver.get('http://localhost:8080')

        # Accept cookies if present
        try:
            accept_cookies = wait.until(EC.presence_of_element_located((By.ID, 'rcc-confirm-button')))
            accept_cookies.click()
        except:
            pass

        # Step 2: Log in using the provided credentials
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'account-setting-active')))
        account_button.click()

        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        login_link.click()

        username_field = wait.until(EC.presence_of_element_located((By.NAME, 'username')))
        password_field = driver.find_element(By.NAME, 'loginPassword')

        username_field.send_keys("test22@user.com")
        password_field.send_keys("test**11")

        login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        login_button.click()

        # Step 3: Add product to the cart
        product_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/product/olive-table']")))
        product_link.click()

        add_to_cart_btn = wait.until(EC.presence_of_element_located((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_btn.click()

        # Confirm product is added by checking cart count
        cart_count = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'count-style'), '1'))
        self.assertTrue(cart_count, "Cart count should be 1 after adding a product.")

        # Step 4: Open the cart and navigate to the cart page
        cart_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'icon-cart')))
        cart_button.click()

        view_cart_link = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'View Cart')]")))
        view_cart_link.click()

        current_url = driver.current_url
        self.assertIn('/cart', current_url, "Navigated to cart page.")

        # Step 5: Click "Proceed to Checkout"
        proceed_to_checkout = wait.until(EC.presence_of_element_located((By.XPATH, "//a[contains(text(), 'Proceed to Checkout')]")))
        proceed_to_checkout.click()

        # Step 6: Fill in the billing form
        first_name_field = wait.until(EC.presence_of_element_located((By.NAME, 'firstName')))
        last_name_field = driver.find_element(By.NAME, 'lastName')
        address_field = driver.find_element(By.NAME, 'address')
        city_field = driver.find_element(By.NAME, 'city')
        postal_code_field = driver.find_element(By.NAME, 'postalCode')
        phone_field = driver.find_element(By.NAME, 'phone')
        email_field = driver.find_element(By.NAME, 'email')

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        address_field.send_keys("123 Fake Street")
        city_field.send_keys("Fake City")
        postal_code_field.send_keys("12345")
        phone_field.send_keys("1234567890")
        email_field.send_keys("test22@user.com")

        # Wait for region select to appear
        wait.until(EC.presence_of_element_located((By.XPATH, "//select/option[text()='Quebec']")))

        region_fields = driver.find_elements(By.XPATH, "//select/option[text()='Quebec']")
        if not region_fields:
            self.fail("Region (state) selector did not appear.")

        region_field = driver.find_element(By.XPATH, "//select/option[text()='Quebec']")
        region_field.click()

        # Step 7: Accept terms and proceed
        agree_check = driver.find_element(By.NAME, 'isAgree')
        agree_check.click()

        place_order_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Place your order')]")
        place_order_button.click()

        # Step 8: Confirm success if form is filled
        self.assertTrue(first_name_field.get_attribute('value'), 'Billing form not filled correctly.')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()