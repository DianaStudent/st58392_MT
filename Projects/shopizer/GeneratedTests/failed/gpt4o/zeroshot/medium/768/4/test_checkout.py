from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Accept cookies
        accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_button.click()

        # Step 2: Navigate to login page
        account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Step 3: Log in
        email_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        email_input.send_keys("test22@user.com")

        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys("test**11")

        login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        login_button.click()

        # Step 4: Add a product to the cart
        product_add_to_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        product_add_to_cart.click()

        # Step 5: Navigate to cart page
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Step 6: Proceed to checkout
        proceed_to_checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Step 7: Fill the billing form
        first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name.send_keys("John")

        last_name = driver.find_element(By.NAME, "lastName")
        last_name.send_keys("Doe")

        address = driver.find_element(By.NAME, "address")
        address.send_keys("1234 Elm Street")

        # Wait for state select to appear
        state_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='stateProvince']")))
        state_select.click()

        state_option = driver.find_element(By.XPATH, "//option[@value='CA']")
        state_option.click()

        city = driver.find_element(By.NAME, "city")
        city.send_keys("Sample City")

        postal_code = driver.find_element(By.NAME, "postalCode")
        postal_code.send_keys("123456")

        phone = driver.find_element(By.NAME, "phone")
        phone.send_keys("1234567890")

        email = driver.find_element(By.NAME, "email")
        email.send_keys("john.doe@example.com")

        # Step 8: Accept terms and place order
        agree_terms = driver.find_element(By.NAME, "isAgree")
        agree_terms.click()

        place_order_button = driver.find_element(By.XPATH, "//button[@type='button' and text()='Place your order']")
        place_order_button.click()

        # Step 9: Verify success
        try:
            success_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h3[text()='Your order']")))
            self.assertTrue(success_message.is_displayed(), "Checkout failed: Success message not found.")
        except:
            self.fail("Checkout failed: Success message not found or issue with checkout flow.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()