import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.driver.maximize_window()

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        cookies_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        cookies_btn.click()

        # Click login
        account_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='account-setting-active']")))
        account_btn.click()

        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        # Perform login
        username = wait.until(EC.visibility_of_element_located((By.NAME, "username")))
        password = driver.find_element(By.NAME, "loginPassword")

        username.send_keys('test22@user.com')
        password.send_keys('test**11')
        password.send_keys(Keys.RETURN)

        # Add product to cart
        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        add_to_cart_btn.click()

        # Open cart
        cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@class='icon-cart']")))
        cart_btn.click()

        # Go to cart page
        view_cart_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='default-btn' and text()='View Cart']")))
        view_cart_btn.click()

        # Proceed to checkout
        proceed_to_checkout_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_btn.click()

        # Fill billing form
        first_name = wait.until(EC.visibility_of_element_located((By.NAME, "firstName")))
        last_name = driver.find_element(By.NAME, "lastName")
        address = driver.find_element(By.NAME, "address")
        city = driver.find_element(By.NAME, "city")
        postal_code = driver.find_element(By.NAME, "postalCode")
        phone = driver.find_element(By.NAME, "phone")
        email = driver.find_element(By.NAME, "email")

        first_name.send_keys("Test")
        last_name.send_keys("User")
        address.send_keys("1234 Street")
        city.send_keys("My City")
        postal_code.send_keys("H2H-2H2")
        phone.send_keys("8888888888")
        email.send_keys("test22@user.com")

        # Wait for state select to appear
        state_select = wait.until(EC.element_to_be_clickable((By.XPATH, "//select[@class='billing-select mb-20']/option[text()='Quebec']")))
        state_select.click()

        # Accept terms and proceed
        agree_checkbox = driver.find_element(By.NAME, "isAgree")
        agree_checkbox.click()

        place_order_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']")))
        place_order_btn.click()

        # Verify that the billing form is filled
        filled_email = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
        self.assertTrue(filled_email.get_attribute('value'), "Billing form not filled!")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()