from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest
from selenium.webdriver.chrome.service import Service as ChromeService


class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver

        # Accept Cookies
        self.wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))).click()

        # Navigate to login
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login"))).click()

        # Enter credentials and login
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("test22@user.com")
        driver.find_element(By.NAME, "loginPassword").send_keys("test**11")
        driver.find_element(By.XPATH, "//button[text()='Login']").click()

        # Add the first product to the cart
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']"))).click()

        # Verify the cart popup and open cart
        cart_button = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_button.click()
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))).click()

        # Proceed to checkout
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))).click()

        # Fill in billing details
        self.fill_billing_details()

        # Accept terms and place order
        self.wait.until(EC.element_to_be_clickable((By.NAME, "isAgree"))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place your order']"))).click()

        # Confirm billing form is filled
        self.confirm_billing_form()

    def fill_billing_details(self):
        driver = self.driver

        self.wait.until(EC.visibility_of_element_located((By.NAME, "firstName"))).send_keys("Test")
        driver.find_element(By.NAME, "lastName").send_keys("User")
        driver.find_element(By.NAME, "company").send_keys("Company")
        driver.find_element(By.NAME, "address").send_keys("1234 Street address")
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Canada']"))).click()

        # Wait for region field to appear and select
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "//option[text()='Quebec']"))).click()

        driver.find_element(By.NAME, "city").send_keys("My City")
        driver.find_element(By.NAME, "postalCode").send_keys("H2H-2H2")
        driver.find_element(By.NAME, "phone").send_keys("8888888888")
        driver.find_element(By.NAME, "email").send_keys("test22@user.com")

    def confirm_billing_form(self):
        driver = self.driver

        form_filled = driver.find_element(By.NAME, "firstName").get_attribute("value") == "Test"
        if not form_filled:
            self.fail("Billing form was not filled correctly.")
        else:
            print("Billing form is filled successfully.")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()