from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Accept cookies
        try:
            accept_cookies_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except:
            self.fail("Failed to find the 'Accept cookies' button.")
        
        # Click on login in the dropdown
        try:
            account_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()

            login_link = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()
        except:
            self.fail("Failed to find login link.")
        
        # Fill login form and submit
        try:
            email_input = wait.until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            password_input = driver.find_element(By.NAME, "loginPassword")
            login_button = driver.find_element(By.XPATH, "//button/span[text()='Login']")

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except:
            self.fail("Failed to fill login form.")

        # Add products to cart
        try:
            add_to_cart_buttons = wait.until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".fa-shopping-cart"))
            )
            add_to_cart_buttons[0].click()
            add_to_cart_buttons[1].click()
        except:
            self.fail("Failed to add products to cart.")

        # Go to cart page
        try:
            cart_button = wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_button.click()
            
            proceed_to_checkout_button = wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            proceed_to_checkout_button.click()
        except:
            self.fail("Failed to navigate to cart page or checkout.")

        # Fill billing form
        try:
            first_name_input = wait.until(
                EC.visibility_of_element_located((By.NAME, "firstName"))
            )
            last_name_input = driver.find_element(By.NAME, "lastName")
            address_input = driver.find_element(By.NAME, "address")
            city_input = driver.find_element(By.NAME, "city")
            postal_code_input = driver.find_element(By.NAME, "postalCode")
            phone_input = driver.find_element(By.NAME, "phone")
            email_input = driver.find_element(By.NAME, "email")
            
            first_name_input.send_keys("Test")
            last_name_input.send_keys("User")
            address_input.send_keys("1234 Street address")
            city_input.send_keys("My city")
            postal_code_input.send_keys("H2H 2H2")
            phone_input.send_keys("8888888888")
            email_input.send_keys("test22@user.com")

            self.assertEqual(first_name_input.get_attribute("value"), "Test")
            self.assertEqual(last_name_input.get_attribute("value"), "User")
        except:
            self.fail("Failed to fill or verify billing form.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()