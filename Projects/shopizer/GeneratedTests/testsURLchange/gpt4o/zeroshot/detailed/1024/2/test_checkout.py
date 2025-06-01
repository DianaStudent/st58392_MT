import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
    
    def test_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        url = "http://localhost/"

        # 1. Open the home page.
        driver.get(url)
        
        # Accept cookies if presented
        try:
            cookie_button = wait.until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # 2. Log in using credentials.
        account_button = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".account-setting-active"))
        )
        account_button.click()

        login_link = wait.until(
            EC.presence_of_element_located((By.LINK_TEXT, "Login"))
        )
        login_link.click()

        email_input = wait.until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        email_input.send_keys("test22@user.com")

        password_input = driver.find_element(By.NAME, "loginPassword")
        password_input.send_keys("test**11")

        login_button = driver.find_element(By.XPATH, "//button[span='Login']")
        login_button.click()

        # 3. Navigate back to the home page.
        logo = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".logo a"))
        )
        logo.click()

        # 3. Hover over the first product.
        first_product = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-wrap-2"))
        )
        driver.execute_script("arguments[0].scrollIntoView();", first_product)

        # 4. Click the revealed "Add to cart" button.
        add_to_cart_button = first_product.find_element(By.CSS_SELECTOR, "button[title='Add to cart']")
        add_to_cart_button.click()

        # 5. Click the cart icon to open the popup cart.
        cart_icon = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".icon-cart"))
        )
        cart_icon.click()

        # 6. Wait for the popup to become visible.
        cart_popup = wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart-content.active"))
        )

        # 7. Click "View Cart" button inside the popup.
        view_cart_button = cart_popup.find_element(By.LINK_TEXT, "View Cart")
        view_cart_button.click()

        # 8. On the cart page, click the "Proceed to Checkout" button.
        proceed_to_checkout_button = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
        )
        proceed_to_checkout_button.click()

        # 7. Fill out the billing form.
        wait.until(EC.presence_of_element_located((By.NAME, "company"))).send_keys("Comp1")
        driver.find_element(By.NAME, "address").send_keys("Street1")
        driver.find_element(By.NAME, "city").send_keys("Quebec")

        # Select region/state from dropdown
        state_dropdown = driver.find_element(By.XPATH, "//label[text()='State']/following-sibling::select")
        state_dropdown.click()
        quebec_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//option[text()='Quebec']"))
        )
        quebec_option.click()

        driver.find_element(By.NAME, "postalCode").send_keys("1234")
        driver.find_element(By.NAME, "phone").send_keys("1234567891")

        # Accept terms checkbox
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        # Confirm success if form is filled.
        self.assertTrue(driver.find_element(By.NAME, "company").get_attribute("value"), msg="Billing form not filled")
    
    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()