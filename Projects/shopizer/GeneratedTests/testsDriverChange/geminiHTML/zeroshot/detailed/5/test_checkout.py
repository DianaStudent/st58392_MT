import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # 1. Open the home page.
        try:
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))
        except TimeoutException:
            self.fail("Home page did not load in 20 seconds.")

        # 2. Log in using credentials.
        try:
            account_button = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "account-setting-active"))
            )
            account_button.click()
            login_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
            )
            login_link.click()

            email_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "username"))
            )
            password_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "loginPassword"))
            )
            login_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'Login')]"))
            )

            email_input.send_keys("test22@user.com")
            password_input.send_keys("test**11")
            login_button.click()
        except TimeoutException:
            self.fail("Login elements not found or login failed.")

        # 3. Navigate back to the home page.
        try:
            home_link = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//a[text()='Home']"))
            )
            home_link.click()
        except TimeoutException:
            self.fail("Could not navigate back to home page.")

        # 4. Hover over the first product.
        # 5. Click the revealed "Add to cart" button.
        try:
            product_img = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "(//div[@class='product-img']/a)[1]"))
            )
            actions = ActionChains(self.driver)
            actions.move_to_element(product_img).perform()

            add_to_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.XPATH, "(//button[@title='Add to cart'])[1]"))
            )
            add_to_cart_button.click()
        except TimeoutException:
            self.fail("Could not add product to cart.")

        # 5. Click the cart icon to open the popup cart.
        try:
            cart_icon = self.wait.until(
                EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart"))
            )
            cart_icon.click()
        except TimeoutException:
            self.fail("Could not open cart popup.")

        # 6. Wait for the popup to become visible.
        # 7. Click "View cart" or similar button inside the popup.
        try:
            view_cart_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "View Cart"))
            )
            view_cart_button.click()
        except TimeoutException:
            self.fail("Could not view cart.")

        # 8. On the cart page, click the "Proceed to Checkout" button.
        try:
            checkout_button = self.wait.until(
                EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout"))
            )
            checkout_button.click()
        except TimeoutException:
            self.fail("Could not proceed to checkout.")

        # 7. Fill out the billing form:
        try:
            company_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "company"))
            )
            address_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "address"))
            )
            city_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "city"))
            )
            state_select = self.wait.until(
                EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select"))
            )
            postal_code_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "postalCode"))
            )
            phone_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, "phone"))
            )
            terms_checkbox = self.wait.until(
                EC.presence_of_element_located((By.NAME, "isAgree"))
            )

            company_input.send_keys("Comp1")
            address_input.send_keys("Street1")
            city_input.send_keys("Quebec")
            for option in state_select.find_elements(By.TAG_NAME, 'option'):
                if option.text == 'Quebec':
                    option.click()
                    break

            postal_code_input.send_keys("1234")
            phone_input.send_keys("1234567891")
            terms_checkbox.click()

        except TimeoutException:
            self.fail("Billing form elements not found.")

        # 8. Wait for any maps popups or warnings and close them.
        # (Skipping this step as there's no clear indication of such popups in the HTML)

        # 9. Confirm success if form is filled.
        try:
            self.assertTrue(company_input.get_attribute("value") == "Comp1")
            self.assertTrue(address_input.get_attribute("value") == "Street1")
            self.assertTrue(city_input.get_attribute("value") == "Quebec")
            self.assertTrue(postal_code_input.get_attribute("value") == "1234")
            self.assertTrue(phone_input.get_attribute("value") == "1234567891")
            self.assertTrue(terms_checkbox.is_selected())

        except AssertionError:
            self.fail("Billing form not filled correctly.")

if __name__ == "__main__":
    unittest.main()