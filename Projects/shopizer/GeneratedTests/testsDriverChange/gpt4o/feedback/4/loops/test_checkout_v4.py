import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver: WebDriver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Handle cookies acceptance
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception as e:
            self.fail(f"Failed to find the accept cookies button: {str(e)}")

        # Navigate to login
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        # Perform login
        try:
            username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        except Exception as e:
            self.fail(f"Login elements are not all present: {str(e)}")

        username_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # Navigate back to home
        home_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Home")))
        home_link.click()

        # Add first product to cart
        try:
            first_product_add_to_cart_button = wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, "//div[contains(@class, 'product-wrap-2')]//button[@title='Add to cart']")
                )
            )
            first_product_add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Failed to add product to cart: {str(e)}")

        # Open and navigate cart popup
        cart_icon = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        view_cart_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Proceed to checkout
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill billing form
        billing_details = {
            "company": "Comp1",
            "address": "Street1",
            "city": "Quebec",
            "postalCode": "1234",
            "phone": "1234567891"
        }

        for name, value in billing_details.items():
            input_element = wait.until(EC.presence_of_element_located((By.NAME, name)))
            input_element.send_keys(value)

        # Select state/province
        state_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[text()='Select a state']]")))
        state_select.send_keys("Quebec")

        # Agree to terms and place order
        agree_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))
        agree_checkbox.click()

        # Confirm success if form can be filled (without submission in the final step for this test)
        try:
            place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Place your order']")))
        except Exception as e:
            self.fail(f"Place order button is not present after form fill: {str(e)}")

if __name__ == "__main__":
    unittest.main()