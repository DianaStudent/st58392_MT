from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Open the home page
        self.assertTrue(driver.title)

        # 2. Log in using the provided credentials
        driver.find_element(By.CSS_SELECTOR, ".pe-7s-user-female").click()
        driver.find_element(By.LINK_TEXT, "Login").click()

        username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        password_field = driver.find_element(By.NAME, "loginPassword")

        self.assertTrue(username_field)
        self.assertTrue(password_field)

        username_field.send_keys("test22@user.com")
        password_field.send_keys("test**11")
        driver.find_element(By.XPATH, "//button[span = 'Login']").click()

        # 3. Add product to the cart
        product_add_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Add to cart']")))
        self.assertTrue(product_add_button)
        product_add_button.click()

        # 4. Open the cart and navigate to the cart page
        cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".pe-7s-shopbag")))
        self.assertTrue(cart_icon)
        cart_icon.click()

        view_cart_button = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        self.assertTrue(view_cart_button)
        view_cart_button.click()

        # 5. Click "Proceed to Checkout"
        proceed_to_checkout = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        self.assertTrue(proceed_to_checkout)
        proceed_to_checkout.click()

        # 6. Fill in the billing form
        first_name_field = wait.until(EC.element_to_be_clickable((By.NAME, "firstName")))
        last_name_field = driver.find_element(By.NAME, "lastName")
        address_field = driver.find_element(By.NAME, "address")
        city_field = driver.find_element(By.NAME, "city")
        postal_code_field = driver.find_element(By.NAME, "postalCode")
        phone_field = driver.find_element(By.NAME, "phone")
        email_field = driver.find_element(By.NAME, "email")

        self.assertTrue(first_name_field)
        self.assertTrue(last_name_field)
        self.assertTrue(address_field)
        self.assertTrue(city_field)
        self.assertTrue(postal_code_field)
        self.assertTrue(phone_field)
        self.assertTrue(email_field)

        first_name_field.send_keys("Test")
        last_name_field.send_keys("User")
        address_field.send_keys("123 Test Street")
        city_field.send_keys("TestCity")
        postal_code_field.send_keys("12345")
        phone_field.send_keys("1234567890")
        email_field.send_keys("test22@user.com")

        # Wait for region (state) select to appear
        region_select = wait.until(EC.presence_of_element_located((By.NAME, "stateProvince")))
        self.assertTrue(region_select)

        # 7. Accept terms and proceed
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        order_button = driver.find_element(By.XPATH, "//button[text()='Place your order']")

        self.assertTrue(terms_checkbox)
        self.assertTrue(order_button)

        terms_checkbox.click()
        order_button.click()

        # 8. Confirm success if form is filled
        self.assertTrue(driver.current_url.endswith("checkout"))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()