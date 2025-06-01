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
        self.driver.get("http://localhost/")  # Assuming this is the URL

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Accept cookies
            accept_cookies = wait.until(
                EC.element_to_be_clickable((By.ID, 'rcc-confirm-button'))
            )
            accept_cookies.click()

            # Go to login page
            login_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_button.click()

            # Fill in login form
            username_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")
            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")

            # Submit login form
            submit_login = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            submit_login.click()

            # Add a product to cart (e.g., Olive Table)
            olive_table_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/product/olive-table'] + div button[title='Add to cart']"))
            )
            olive_table_button.click()

            # Navigate to the cart page
            view_cart_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='/cart']"))
            )
            view_cart_button.click()

            # Click on 'Proceed to Checkout'
            proceed_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            proceed_to_checkout_button.click()

            # Fill in the billing form
            first_name_input = wait.until(
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
            address_input.send_keys("123 Testing St")
            city_input.send_keys("Testville")
            postal_code_input.send_keys("12345")
            phone_input.send_keys("8888888888")
            email_input.send_keys("test22@user.com")

            # Confirm billing form is filled
            self.assertTrue(first_name_input.get_attribute("value"), "Test")
            self.assertTrue(last_name_input.get_attribute("value"), "User")

        except Exception as e:
            self.fail(f"Test failed due to: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()