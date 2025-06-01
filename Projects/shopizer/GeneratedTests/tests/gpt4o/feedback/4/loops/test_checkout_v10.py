import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

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

        # Accept cookies
        try:
            accept_button = wait.until(EC.presence_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception:
            pass

        # Log in
        account_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active")))
        account_button.click()

        login_link = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Login")))
        login_link.click()

        username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
        login_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[span='Login']")))

        username_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # Navigate back to home
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "user-profile")))
        driver.get("http://localhost/")

        # Add first product to cart
        product = wait.until(EC.presence_of_element_located(
            (By.XPATH, "(//div[contains(@class, 'product-wrap-2')])[1]")
        ))
        driver.execute_script("arguments[0].scrollIntoView();", product)
        add_to_cart_button = product.find_element(By.XPATH, ".//button[@title='Add to cart']")
        driver.execute_script("arguments[0].click();", add_to_cart_button)

        # Open cart popup and view cart
        cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # Proceed to checkout
        proceed_to_checkout_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # Fill billing form
        billing_details = {
            "firstName": "Test",
            "lastName": "User",
            "company": "Comp1",
            "address": "Street1",
            "city": "Quebec",
            "postalCode": "1234",
            "phone": "1234567891"
        }

        for name, value in billing_details.items():
            input_element = wait.until(EC.presence_of_element_located((By.NAME, name)))
            input_element.clear()
            input_element.send_keys(value)

        # Select state/province
        state_select = wait.until(EC.presence_of_element_located((By.XPATH, "//select[option[@value='QC']]")))
        state_select.click()
        driver.find_element(By.XPATH, "//option[@value='QC']").click()

        # Agree to terms
        agree_checkbox = wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))
        agree_checkbox.click()

        # Confirm success if form can be filled
        place_order_button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[text()='Place your order']")))
        self.assertIsNotNone(place_order_button, "Place order button should be present after form fill")

if __name__ == "__main__":
    unittest.main()