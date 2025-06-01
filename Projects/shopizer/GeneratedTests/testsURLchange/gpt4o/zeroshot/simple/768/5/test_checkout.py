import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://localhost/"

    def test_checkout_process(self):
        driver = self.driver

        # Go to home page
        driver.get(self.base_url)

        # Accept cookies
        try:
            cookie_button = self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            cookie_button.click()
        except Exception:
            self.fail("Cookie consent button not found.")

        # Go to login page
        try:
            login_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
            login_button.click()
        except Exception:
            self.fail("Login link not found.")

        # Perform login
        try:
            email_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "username")))
            password_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "loginPassword")))
            login_submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[span[text()='Login']]")))

            email_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")
            login_submit_button.click()
        except Exception:
            self.fail("Login not successful due to missing fields.")

        # Add products to cart
        try:
            add_table_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']//following-sibling::div/button[@title='Add to cart']")))
            add_chair_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/chair']//following-sibling::div/button[@title='Add to cart']")))

            add_table_button.click()
            add_chair_button.click()
        except Exception:
            self.fail("Failed to add products to cart.")

        # Go to cart page
        try:
            cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='icon-cart']")))
            cart_button.click()
        except Exception:
            self.fail("Cart button not found.")

        # Proceed to checkout
        try:
            checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except Exception:
            self.fail("Checkout button not found.")

        # Fill billing form
        try:
            first_name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
            last_name_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "lastName")))
            address_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "address")))
            city_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "city")))
            postal_code_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "postalCode")))
            phone_field = self.wait.until(EC.visibility_of_element_located((By.NAME, "phone")))

            first_name_field.send_keys("Test")
            last_name_field.send_keys("User")
            address_field.send_keys("1234 Street")
            city_field.send_keys("My City")
            postal_code_field.send_keys("H2H-2H2")
            phone_field.send_keys("8888888888")
        except Exception:
            self.fail("Billing form fields are missing.")

        # Confirm success by verifying billing form is filled
        self.assertTrue(first_name_field.get_attribute('value') == "Test")
        self.assertTrue(last_name_field.get_attribute('value') == "User")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()