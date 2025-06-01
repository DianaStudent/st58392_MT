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
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        # 1. Open the home page - already done in setUp

        # 2. Log in using credentials
        self.driver.get("http://localhost/login")
        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.wait.until(EC.presence_of_element_located((By.NAME, "loginPassword")))
        username_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button = self.wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Login')]")))
        login_button.click()

        # 3. Navigate back to the home page
        self.driver.get("http://localhost/")

        # 4. Hover over the first product
        first_product = self.wait.until(EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-img']/a")))
        actions = ActionChains(self.driver)
        actions.move_to_element(first_product).perform()

        # 5. Click the revealed "Add to cart" button
        add_to_cart_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//button[@title='Add to cart']")))
        add_to_cart_button.click()

        # 6. Click the cart icon to open the popup cart
        cart_icon = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "icon-cart")))
        cart_icon.click()

        # 7. Wait for the popup to become visible
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "shopping-cart-content.active")))

        # 8. Click "View Cart" button inside the popup
        view_cart_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # 9. On the cart page, click the "Proceed to Checkout" button
        proceed_to_checkout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout_button.click()

        # 10. Fill out the billing form
        company_input = self.wait.until(EC.presence_of_element_located((By.NAME, "company")))
        address_input = self.wait.until(EC.presence_of_element_located((By.NAME, "address")))
        city_input = self.wait.until(EC.presence_of_element_located((By.NAME, "city")))
        state_select = self.wait.until(EC.presence_of_element_located((By.XPATH, "//label[text()='State']/following-sibling::select")))
        postal_code_input = self.wait.until(EC.presence_of_element_located((By.NAME, "postalCode")))
        phone_input = self.wait.until(EC.presence_of_element_located((By.NAME, "phone")))
        terms_checkbox = self.wait.until(EC.presence_of_element_located((By.NAME, "isAgree")))

        company_input.send_keys("Comp1")
        address_input.send_keys("Street1")
        city_input.send_keys("Quebec")
        select = Select(state_select)
        select.select_by_visible_text("Quebec")
        postal_code_input.send_keys("1234")
        phone_input.send_keys("1234567891")
        terms_checkbox.click()

        # 11. Confirm success if form is filled
        self.assertEqual(company_input.get_attribute("value"), "Comp1")
        self.assertEqual(address_input.get_attribute("value"), "Street1")
        self.assertEqual(city_input.get_attribute("value"), "Quebec")
        self.assertEqual(postal_code_input.get_attribute("value"), "1234")
        self.assertEqual(phone_input.get_attribute("value"), "1234567891")

if __name__ == "__main__":
    unittest.main()