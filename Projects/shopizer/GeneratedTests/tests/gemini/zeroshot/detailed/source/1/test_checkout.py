import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

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
        account_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
        )
        account_button.click()

        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
        )
        login_link.click()

        username_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        login_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Login']"))
        )

        username_input.send_keys(self.email)
        password_input.send_keys(self.password)
        login_button.click()

        # Navigate back to home page
        driver.get(self.url)

        # Add product to cart
        first_product = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]"))
        )
        
        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25'][1]//button[@title='Add to cart']"))
        )
        
        ActionChains(driver).move_to_element(first_product).perform()
        add_to_cart_button.click()

        # Open cart popup
        cart_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "icon-cart"))
        )
        cart_icon.click()

        # View cart
        view_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "View Cart"))
        )
        view_cart_button.click()

        # Proceed to checkout
        checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout"))
        )
        checkout_button.click()

        # Fill billing form
        company_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "company"))
        )
        address_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "address"))
        )
        city_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "city"))
        )
        state_select = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select"))
        )
        postal_code_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "postalCode"))
        )
        phone_input = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "phone"))
        )

        company_input.send_keys("Comp1")
        address_input.send_keys("Street1")
        city_input.send_keys("Quebec")

        select = Select(state_select)
        select.select_by_value("QC")

        postal_code_input.send_keys("1234")
        phone_input.send_keys("1234567891")

        # Accept terms
        terms_checkbox = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "isAgree"))
        )
        terms_checkbox.click()

        # Verify that the billing form is filled
        self.assertEqual(company_input.get_attribute("value"), "Comp1")
        self.assertEqual(address_input.get_attribute("value"), "Street1")
        self.assertEqual(city_input.get_attribute("value"), "Quebec")
        self.assertEqual(postal_code_input.get_attribute("value"), "1234")
        self.assertEqual(phone_input.get_attribute("value"), "1234567891")

if __name__ == "__main__":
    unittest.main()