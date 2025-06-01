from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver

        try:
            # Accept Cookies
            WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            ).click()

            # Click Login
            account_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active"))
            )
            account_button.click()

            login_link = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            # Perform Login
            email_field = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "username"))
            )
            password_field = driver.find_element(By.NAME, "loginPassword")
            email_field.send_keys("test22@user.com")
            password_field.send_keys("test**11")

            login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
            login_button.click()

            # Add product to cart
            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "(//button[@title='Add to cart'])[1]"))
            )
            add_to_cart_button.click()

            # Go to cart page
            cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
            )
            cart_button.click()

            # Click 'Proceed to Checkout'
            checkout_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()

            # Fill in the billing form
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.NAME, "firstName"))
            ).send_keys("Test")
            driver.find_element(By.NAME, "lastName").send_keys("User")
            driver.find_element(By.NAME, "address").send_keys("123 Test St")
            driver.find_element(By.NAME, "city").send_keys("Test City")
            driver.find_element(By.NAME, "postalCode").send_keys("12345")
            driver.find_element(By.NAME, "phone").send_keys("1234567890")
            driver.find_element(By.NAME, "email").send_keys("test22@user.com")

            # Check if the form is filled
            country_select = driver.find_element(By.XPATH, "//select[@name='country']")
            if country_select.get_attribute("value") == "":
                self.fail("Country not selected in the form")

        except Exception as e:
            self.fail(f"Test failed with exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()