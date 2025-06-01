import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.url = "http://localhost/"
        self.email = "test22@user.com"
        self.password = "test**11"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.url)

        # Accept cookies
        try:
            cookie_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            cookie_button.click()
        except:
            pass

        # Login
        try:
            account_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
        except:
            self.fail("Account button not found")

        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()
        except:
            self.fail("Login link not found")

        try:
            username_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
            )

            username_field.send_keys(self.email)
            password_field.send_keys(self.password)
            login_button.click()

        except:
            self.fail("Login form elements not found")

        # Navigate back to home page
        driver.get(self.url)

        # Add product to cart
        try:
            product = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//h3/a[text()='Olive Table']/ancestor::div[@class='product-content-2']/preceding-sibling::div[@class='product-img']"))
            )

            add_to_cart_button = product.find_element(By.XPATH, ".//div[@class='product-action-2']/button[@title='Add to cart']")

            driver.execute_script("arguments[0].click();", add_to_cart_button)

        except:
            self.fail("Could not add product to cart")

        # Open cart popup
        try:
            cart_icon = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()

            view_cart_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()

        except:
            self.fail("Cart icon or view cart button not found")

        # Proceed to checkout
        try:
            checkout_button = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except:
            self.fail("Checkout button not found")

        # Fill billing form
        try:
            company_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "company"))
            )
            address_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            state_dropdown = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select"))
            )
            postal_code_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_field = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            terms_checkbox = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.NAME, "isAgree"))
            )

            company_field.send_keys("Comp1")
            address_field.send_keys("Street1")
            city_field.send_keys("Quebec")

            for option in state_dropdown.find_elements(By.TAG_NAME, 'option'):
                if option.text == 'Quebec':
                    option.click()
                    break

            postal_code_field.send_keys("1234")
            phone_field.send_keys("1234567891")

            driver.execute_script("arguments[0].click();", terms_checkbox)

        except:
            self.fail("Billing form elements not found")

        # Verify that the billing form is filled
        try:
            self.assertEqual(company_field.get_attribute("value"), "Comp1")
            self.assertEqual(address_field.get_attribute("value"), "Street1")
            self.assertEqual(city_field.get_attribute("value"), "Quebec")
            self.assertEqual(postal_code_field.get_attribute("value"), "1234")
            self.assertEqual(phone_field.get_attribute("value"), "1234567891")
        except:
            self.fail("Billing form was not filled correctly")


if __name__ == "__main__":
    unittest.main()