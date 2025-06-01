from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait
        
        # Click on Accept Cookies
        accept_cookie_btn = wait.until(
            EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
        )
        accept_cookie_btn.click()

        # Log in
        account_btn = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_btn.click()
        login_btn = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_btn.click()

        username_input = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_input.send_keys("test22@user.com")

        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys("test**11")

        login_submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        login_submit_btn.click()

        # Navigate back to home page
        logo = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".logo a"))
        )
        logo.click()

        # Add first product to cart
        product = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        ActionChains(driver).move_to_element(product).perform()

        add_to_cart_btn = product.find_element(By.CSS_SELECTOR, ".fa-shopping-cart").find_element(By.XPATH, "..")
        add_to_cart_btn.click()

        # Open cart popup
        cart_btn = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_btn.click()

        # Wait for popup and click on View Cart
        view_cart_btn = wait.until(
            EC.visibility_of_element_located((By.LINK_TEXT, "View Cart"))
        )
        view_cart_btn.click()

        # On the cart page, click on Proceed to Checkout button
        checkout_btn = wait.until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Proceed to Checkout']"))
        )
        checkout_btn.click()

        # Fill out the billing form
        def fill_input_element(name, value):
            element = wait.until(EC.presence_of_element_located((By.NAME, name)))
            element.send_keys(value)

        fill_input_element("company", "Comp1")
        fill_input_element("address", "Street1")
        fill_input_element("city", "Quebec")
        fill_input_element("postalCode", "1234")
        fill_input_element("phone", "1234567891")

        # Select region/state
        state_select = driver.find_element(By.CSS_SELECTOR, "select[name='state']")
        ActionChains(driver).move_to_element(state_select).click().perform()
        for option in state_select.find_elements(By.TAG_NAME, "option"):
            if option.text == "Quebec":
                option.click()
                break

        # Accept terms
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        terms_checkbox.click()

        # Ensure form is filled
        # (This should confirm with additional checks if needed in real-world usage)
        self.assertTrue(
            all([
                el.get_attribute("value") != "" for el in (
                    driver.find_element(By.NAME, "company"),
                    driver.find_element(By.NAME, "address"),
                    # Continue with all elements
                )
            ]),
            "Billing form is not correctly filled."
        )

        # If any popups, handle them here (pseudo-code)
        # close_popup_if_exists(driver)

if __name__ == "__main__":
    unittest.main()