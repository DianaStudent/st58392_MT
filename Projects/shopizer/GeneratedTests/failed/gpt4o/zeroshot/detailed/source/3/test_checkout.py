from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://localhost/"
        self.credentials = {"email": "test22@user.com", "password": "test**11"}

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Step 1: Open the home page
        driver.get(self.base_url)
        self.accept_cookies()

        # Step 2: Log in using credentials
        self.login()

        # Step 3: Navigate back to the home page
        driver.get(self.base_url)

        # Step 4: Hover over the first product and click "Add to cart"
        product = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2")))
        add_to_cart_btn = product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
        driver.execute_script("arguments[0].scrollIntoView();", product)
        add_to_cart_btn.click()

        # Step 5: Click the cart icon to open the popup cart
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart")))
        cart_icon.click()

        # Step 6: Wait for the popup to become visible and click "View cart"
        view_cart_btn = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[contains(text(),'View Cart')]")))
        view_cart_btn.click()

        # Step 7: On the cart page, click the "Proceed to Checkout" button
        proceed_to_checkout_btn = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".grand-totall a")))
        proceed_to_checkout_btn.click()

        # Step 8: Fill out the billing form
        self.fill_billing_form()

        # Assert if the form is filled and no warnings popup
        self.confirm_form_filled()

    def login(self):
        driver = self.driver
        wait = self.wait

        login_link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        login_link.click()

        email_input = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
        email_input.send_keys(self.credentials["email"])

        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys(self.credentials["password"])

        login_button = driver.find_element(By.XPATH, "//button[.//span[text()='Login']]")
        login_button.click()

    def accept_cookies(self):
        try:
            accept_button = self.wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            accept_button.click()
        except Exception:
            pass

    def fill_billing_form(self):
        driver = self.driver
        wait = self.wait

        wait.until(EC.element_to_be_clickable((By.NAME, "company"))).send_keys("Comp1")
        driver.find_element(By.NAME, "address").send_keys("Street1")
        driver.find_element(By.NAME, "city").send_keys("Quebec")

        state_select = driver.find_element(By.XPATH, "//label[text()='State']/following-sibling::select")
        state_select.find_element(By.XPATH, ".//option[text()='Quebec']").click()

        driver.find_element(By.NAME, "postalCode").send_keys("1234")
        driver.find_element(By.NAME, "phone").send_keys("1234567891")
        
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

    def confirm_form_filled(self):
        driver = self.driver
        wait = self.wait
        try:
            order_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//button[.//span[text()='Place your order']]")))
            self.assertTrue(order_button.is_displayed(), "Order button is not displayed.")
        except Exception as e:
            self.fail(f"Form filling failed or map popup detected: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()