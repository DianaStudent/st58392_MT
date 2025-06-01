from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Accept Cookies
        cookies_button = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookies_button.click()

        # 2. Open login page
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
        account_button.click()
        login_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_button.click()

        # 3. Log in
        email_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        password_input = driver.find_element(By.NAME, "loginPassword")
        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_submit.click()

        # Confirm successful login
        account_dropdown = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".user-profile .user-name")))
        self.assertTrue("Welcome Test User" in account_dropdown.text)
        
        # 4. Add product to the cart
        add_to_cart_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # 5. Open the cart page
        cart_icon = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()
        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # 6. Click "Proceed to Checkout"
        checkout_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        checkout_button.click()

        # 7. Fill in the billing form
        first_name = wait.until(EC.presence_of_element_located((By.NAME, "firstName")))
        first_name.send_keys("Test")
        last_name = driver.find_element(By.NAME, "lastName")
        last_name.send_keys("User")
        address = driver.find_element(By.NAME, "address")
        address.send_keys("123 Test Street")
        city = driver.find_element(By.NAME, "city")
        city.send_keys("Test City")
        postal_code = driver.find_element(By.NAME, "postalCode")
        postal_code.send_keys("H2H 2H2")
        phone = driver.find_element(By.NAME, "phone")
        phone.send_keys("888-888-8888")
        email = driver.find_element(By.NAME, "email")
        email.send_keys("test22@user.com")

        # Wait and select state
        state_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@name='state']")))
        state_select.send_keys("Quebec")

        # 8. Accept terms and proceed
        agree_terms = driver.find_element(By.NAME, "isAgree")
        agree_terms.click()
        place_order_button = driver.find_element(By.XPATH, "//button[text()='Place your order']")
        place_order_button.click()

        # 9. Confirm success by verifying form is filled
        filled_email = wait.until(EC.presence_of_element_located((By.NAME, "email")))
        self.assertTrue(filled_email.get_attribute("value") == "test22@user.com", "Email input is correctly filled")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()