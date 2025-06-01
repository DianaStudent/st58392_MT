import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class CheckoutTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_checkout_process(self):
        driver = self.driver
        wait = self.wait

        # Accept cookies if present
        try:
            accept_cookies = wait.until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            if accept_cookies.is_displayed():
                accept_cookies.click()
        except:
            pass

        # Log in
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_button.click()

        login_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        username_field = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys("test22@user.com")

        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        password_field.send_keys("test**11")

        login_button = wait.until(
            EC.presence_of_element_located((By.XPATH, "//button//span[text()='Login']"))
        )
        login_button.click()

        # Navigate back to home page
        driver.get("http://localhost/")

        # Hover over the first product and add to cart
        first_product = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".product-wrap-2 .product-img")
            )
        )
        actions = ActionChains(driver)
        actions.move_to_element(first_product).perform()

        add_to_cart_button = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@title='Add to cart']")
            )
        )
        add_to_cart_button.click()

        # Open cart popup
        cart_icon = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_icon.click()

        # Wait for the popup to become visible
        wait.until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".shopping-cart-content.active")
            )
        )

        # Click "View cart" button
        view_cart_button = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "View Cart"))
        )
        view_cart_button.click()

        # On the cart page, proceed to checkout
        proceed_button = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))
        )
        proceed_button.click()

        # Fill out the billing form
        company_field = wait.until(
            EC.presence_of_element_located((By.NAME, "company"))
        )
        company_field.send_keys("Comp1")

        address_field = driver.find_element(By.NAME, "address")
        address_field.send_keys("Street1")

        city_field = driver.find_element(By.NAME, "city")
        city_field.send_keys("Quebec")

        # Select region/state
        state_select = driver.find_element(By.XPATH, "//select[@name='stateProvince']")
        state_select.click()
        state_option = state_select.find_element(By.XPATH, "//option[text()='Quebec']")
        state_option.click()

        postal_code_field = driver.find_element(By.NAME, "postalCode")
        postal_code_field.send_keys("1234")

        phone_field = driver.find_element(By.NAME, "phone")
        phone_field.send_keys("1234567891")

        # Accept terms
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        terms_checkbox.click()

        # Confirm the form is filled
        company_value = company_field.get_attribute("value")
        if company_value != "Comp1":
            self.fail("Billing form is not filled correctly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()