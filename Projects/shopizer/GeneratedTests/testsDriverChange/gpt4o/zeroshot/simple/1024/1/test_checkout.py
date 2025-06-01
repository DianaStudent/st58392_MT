import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_user_checkout(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except:
            self.fail("Accept cookies button not found.")

        # Navigate to Login
        try:
            account_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active")))
            account_button.click()
            login_link = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//li/a[@href='/login']")))
            login_link.click()
        except:
            self.fail("Login navigation elements not found.")

        # Log in
        try:
            email_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_input = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Login elements not found or could not log in.")

        # Add product to cart
        try:
            add_to_cart_buttons = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[@title='Add to cart']")))
            add_to_cart_buttons[0].click()  # Add first product
        except:
            self.fail("Product elements not found or could not add to cart.")

        # Open cart popup and view cart
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
            cart_button.click()
            view_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='default-btn' and text()='View Cart']")))
            view_cart_button.click()
        except:
            self.fail("Cart elements not found or could not view cart.")

        # Proceed to Checkout
        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Proceed to Checkout']")))
            checkout_button.click()
        except:
            self.fail("Checkout button not found or could not proceed to checkout.")

        # Verify Billing Form presence
        try:
            self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            self.wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        except:
            self.fail("Billing form not loaded properly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()