import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_checkout(self):
        # Open the home page.
        self.driver.get("http://localhost/")
        login_email = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='email']")))
        login_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Login')]"))))

        # Add a product to the cart.
        product_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost/product']"))))
        self.driver.get("http://localhost/product")
        add_product_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Add to Cart')]")))
        self.driver.execute_script(f"document.querySelector('#product-form > input[name='quantity']').value=1;")

        # Go to the cart page.
        cart_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost/cart']"))))
        self.driver.get("http://localhost/cart")

        # Click "Proceed to Checkout".
        proceed_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Proceed to Checkout')]"))))

        # Fill in the billing form.
        name_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='name']")))
        address1_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='address1']")))
        city_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='city']")))
        state_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//select[@id='state']/option[1]")))
        zip_code_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='zipCode']")))
        phone_number_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='phoneNum']")))
        email_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='email']")))
        password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='password']")))
        confirm_password_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='confirmPassword']"))))

        # Accept terms and proceed.
        accept_terms_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'I agree with the terms & conditions']}"))))
        self.driver.execute_script(f"document.querySelector('#terms-accept').checked=true;")

        # Confirm success by verifying that the billing form is filled.
        billing_form = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//form[@id='billing-form']"))))
        if name_field.get_attribute("value") != "" and address1_field.get_attribute("value").strip() == "1234" and city_field.get_attribute("value").strip() == "My City" and state_field.get_attribute("value").strip() == "State" and zip_code_field.get_attribute("value").strip() == "12345":
            self.assertTrue(True)
        else:
            self.fail("Billing form not filled correctly")

if __name__ == '__main__':
    unittest.main()