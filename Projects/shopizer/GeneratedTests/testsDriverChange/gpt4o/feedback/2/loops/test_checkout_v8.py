from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver

        # Accept cookies
        try:
            accept_cookies_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            accept_cookies_button.click()
        except Exception as e:
            self.fail(f"Accept cookies button not found: {str(e)}")

        # Log in
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Login"))
            )
            login_link.click()

            email_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            email_field.send_keys("test22@user.com")

            password_field = driver.find_element(By.NAME, "loginPassword")
            password_field.send_keys("test**11")

            login_button = driver.find_element(By.XPATH, "//button[contains(., 'Login')]")
            login_button.click()
        except Exception as e:
            self.fail(f"Login failed: {str(e)}")

        # Navigate back to home
        try:
            home_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Home"))
            )
            home_link.click()
        except Exception as e:
            self.fail(f"Navigation to home failed: {str(e)}")

        # Hover over the first product
        try:
            product_img = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2:nth-of-type(1) .product-img img"))
            )
            product = product_img.find_element(By.XPATH, "..")  # Get the parent containing the buttons
            ActionChains(driver).move_to_element(product).perform()

            add_to_cart_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']"))
            )
            add_to_cart_button.click()
        except Exception as e:
            self.fail(f"Adding to cart failed: {str(e)}")

        # Open cart popup and view cart
        try:
            cart_button = driver.find_element(By.CLASS_NAME, "icon-cart")
            cart_button.click()

            cart_popup = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content"))
            )

            view_cart_link = driver.find_element(By.LINK_TEXT, "View Cart")
            view_cart_link.click()
        except Exception as e:
            self.fail(f"Viewing cart failed: {str(e)}")

        # Proceed to Checkout
        try:
            proceed_to_checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))
            )
            proceed_to_checkout_button.click()
        except Exception as e:
            self.fail(f"Proceeding to checkout failed: {str(e)}")

        # Fill out the billing form
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            ).send_keys("Test")
            driver.find_element(By.NAME, "lastName").send_keys("User")
            driver.find_element(By.NAME, "company").send_keys("Comp1")
            driver.find_element(By.NAME, "address").send_keys("Street1")
            driver.find_element(By.NAME, "city").send_keys("Quebec")

            select_element = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//option[text()='Quebec']"))
            )
            select_element.click()

            driver.find_element(By.NAME, "postalCode").send_keys("1234")
            driver.find_element(By.NAME, "phone").send_keys("1234567891")

            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "isAgree"))
            )
            terms_checkbox.click()

            fields = driver.find_elements(By.TAG_NAME, "input")
            self.assertTrue(all(field.get_attribute('value') for field in fields if field.get_attribute('name')), "Form not filled properly")
        except Exception as e:
            self.fail(f"Filling billing details failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()