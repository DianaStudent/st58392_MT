from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.base_url = "http://localhost/"
        self.wait = WebDriverWait(self.driver, 20)
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies
        try:
            cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookies_button.click()
        except Exception as e:
            self.fail(f"Cannot find or click the cookies accept button: {str(e)}")

        # Go to login page
        try:
            login_link = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except Exception as e:
            self.fail(f"Cannot find or click the login link: {str(e)}")

        # Login
        try:
            email_input = wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            email_input.send_keys("test22@user.com")

            password_input = driver.find_element(By.NAME, "loginPassword")
            password_input.send_keys("test**11")

            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")
            login_button.click()
        except Exception as e:
            self.fail(f"Cannot perform login: {str(e)}")

        # Add Olive Table to cart
        try:
            olive_table_add_to_cart = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following-sibling::div/button"))
            )
            olive_table_add_to_cart.click()
        except Exception as e:
            self.fail(f"Cannot add Olive Table to the cart: {str(e)}")

        # Go to Cart page
        try:
            cart_menu_button = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
            )
            cart_menu_button.click()

            view_cart_button = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='View Cart']"))
            )
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Cannot navigate to Cart page: {str(e)}")

        # Proceed to Checkout
        try:
            proceed_to_checkout = wait.until(
                EC.element_to_be_clickable((By.XPATH, "//a[text()='Proceed to Checkout']"))
            )
            proceed_to_checkout.click()
        except Exception as e:
            self.fail(f"Cannot proceed to checkout: {str(e)}")

        # Fill billing details
        try:
            first_name_input = wait.until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )
            first_name_input.send_keys("FirstNameTest")

            last_name_input = driver.find_element(By.NAME, "lastName")
            last_name_input.send_keys("LastNameTest")

            address_input = driver.find_element(By.NAME, "address")
            address_input.send_keys("123 Test St.")

            city_input = driver.find_element(By.NAME, "city")
            city_input.send_keys("Test City")

            postal_code_input = driver.find_element(By.NAME, "postalCode")
            postal_code_input.send_keys("H2H-2H2")

            phone_input = driver.find_element(By.NAME, "phone")
            phone_input.send_keys("8888888888")

            email_input = driver.find_element(By.NAME, "email")
            email_input.send_keys("test22@user.com")
        except Exception as e:
            self.fail(f"Cannot fill the billing details: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()