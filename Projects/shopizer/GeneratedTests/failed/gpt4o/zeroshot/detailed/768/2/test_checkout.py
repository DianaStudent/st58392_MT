from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Accept cookies
        accept_cookies_btn = wait.until(EC.element_to_be_clickable((By.ID, "rcc-confirm-button")))
        accept_cookies_btn.click()

        # Click on login
        account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pe-7s-user-female")))
        account_button.click()
        login_button = wait.until(lambda d: d.find_element(By.LINK_TEXT, "Login"))
        login_button.click()

        # Perform login
        username_field = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        username_field.send_keys("test22@user.com")

        password_field = wait.until(EC.element_to_be_clickable((By.NAME, "loginPassword")))
        password_field.send_keys("test**11")

        login_submit_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".button-box button[type='submit']")))
        login_submit_btn.click()

        # Navigate back to the home page
        home_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Home")))
        home_link.click()

        # Hover over and add the first product to the cart
        first_product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-img a")))
        driver.execute_script("arguments[0].scrollIntoView(true);", first_product)

        add_to_cart_btn = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".product-action-2 button[title='Add to cart']")))
        add_to_cart_btn.click()

        # Open cart popup
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Wait for popup to become visible
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active")))

        # Click "View Cart" on popup
        view_cart_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_btn.click()

        # Proceed to Checkout
        proceed_to_checkout_btn = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_btn.click()

        # Fill out the billing form
        company_input = wait.until(EC.element_to_be_clickable((By.NAME, "company")))
        company_input.send_keys("Comp1")

        address_input = driver.find_element(By.NAME, "address")
        address_input.send_keys("Street1")

        city_input = driver.find_element(By.NAME, "city")
        city_input.send_keys("Quebec")

        state_dropdown = driver.find_element(By.CSS_SELECTOR, ".billing-select select")
        state_dropdown.click()
        driver.find_element(By.XPATH, "//option[text()='Quebec']").click()

        postal_code_input = driver.find_element(By.NAME, "postalCode")
        postal_code_input.send_keys("1234")

        phone_input = driver.find_element(By.NAME, "phone")
        phone_input.send_keys("1234567891")

        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        terms_checkbox.click()

        # Verify if the form is filled
        self.assertTrue(company_input.get_attribute("value"), msg="Company input is empty")
        self.assertTrue(address_input.get_attribute("value"), msg="Address input is empty")
        self.assertTrue(city_input.get_attribute("value"), msg="City input is empty")
        self.assertTrue(postal_code_input.get_attribute("value"), msg="Postal code input is empty")
        self.assertTrue(phone_input.get_attribute("value"), msg="Phone input is empty")
        self.assertTrue(terms_checkbox.is_selected(), msg="Terms checkbox is not selected")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()