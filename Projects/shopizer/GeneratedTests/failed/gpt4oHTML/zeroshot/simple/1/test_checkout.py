from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Navigate to the home page
        driver.get("http://localhost/")

        # Accept cookies
        try:
            accept_cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Cookie acceptance failed: {str(e)}")

        # Navigate to login page
        try:
            login_link = driver.find_element(By.LINK_TEXT, "Login")
            login_link.click()
        except Exception as e:
            self.fail(f"Login link not found: {str(e)}")

        # Login
        try:
            username_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
            password_input = driver.find_element(By.NAME, "loginPassword")
            username_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button = driver.find_element(By.CSS_SELECTOR, "div.button-box button[type='submit']")
            login_button.click()
        except Exception as e:
            self.fail(f"Login failed: {str(e)}")

        # Select a product and add to cart
        try:
            product_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/product/olive-table']/following-sibling::div/button[@title='Add to cart']")))
            product_add_button.click()
        except Exception as e:
            self.fail(f"Adding product to cart failed: {str(e)}")

        # Go to cart page
        try:
            cart_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
            cart_button.click()
            view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
            view_cart_button.click()
        except Exception as e:
            self.fail(f"Navigation to cart failed: {str(e)}")

        # Proceed to checkout
        try:
            checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
            checkout_button.click()
        except Exception as e:
            self.fail(f"Proceed to checkout failed: {str(e)}")

        # Fill in the billing form
        try:
            wait.until(EC.element_to_be_clickable((By.NAME, "firstName"))).send_keys("Test")
            driver.find_element(By.NAME, "lastName").send_keys("User")
            driver.find_element(By.NAME, "address").send_keys("1234 Elm Street")
            driver.find_element(By.NAME, "city").send_keys("TestCity")
            driver.find_element(By.NAME, "postalCode").send_keys("H2H-2H2")
            driver.find_element(By.NAME, "phone").send_keys("1234567890")
            driver.find_element(By.NAME, "email").send_keys("test22@user.com")
        except Exception as e:
            self.fail(f"Filling billing form failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()