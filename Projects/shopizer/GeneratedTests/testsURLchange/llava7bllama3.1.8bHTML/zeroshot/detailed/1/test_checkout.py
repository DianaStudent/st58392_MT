import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        options = Options()
        options.add_argument('--headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    def tearDown(self):
        self.driver.quit()

    def test_checkout(self):
        # 1. Open the home page
        self.driver.get("http://localhost/")

        # 2. Log in using credentials
        login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Login')))
        login_button.click()
        email_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'email')))
        password_input = self.driver.find_element(By.NAME, 'password')
        login_button = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        email_input.send_keys("test22@user.com")
        password_input.send_keys("test**11")
        login_button.click()

        # 3. Navigate back to the home page
        self.driver.back()
        self.driver.refresh()

        # 4. Hover over the first product
        product_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.LINK_TEXT, 'Product')))
        if len(product_links) > 0:
            product_links[0].click()

        # 5. Click the revealed "Add to cart" button.
        add_to_cart_button = self.driver.find_element(By.CSS_SELECTOR, '.add-to-cart')
        add_to_cart_button.click()

        # 6. Click the cart icon to open the popup cart
        cart_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Cart')))
        cart_icon.click()

        # 7. Wait for the popup to become visible
        cart_popup = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='cart-popup']")))

        # 8. Click "View cart" or similar button inside the popup.
        view_cart_button = self.driver.find_element(By.LINK_TEXT, 'View cart')
        view_cart_button.click()

        # 9. On the cart page, click the "Proceed to Checkout" button
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Proceed to checkout')))
        proceed_to_checkout_button.click()

        # 10. Fill out the billing form:
        company_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'company')))
        address_input = self.driver.find_element(By.NAME, 'address')
        city_input = self.driver.find_element(By.NAME, 'city')
        region_input = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LABEL_TEXT, 'State/Province')))
        postal_code_input = self.driver.find_element(By.NAME, 'postal_code')
        phone_number_input = self.driver.find_element(By.NAME, 'phone')

        company_input.send_keys('Comp1')
        address_input.send_keys('Street1')
        city_input.send_keys('Quebec')
        region_input.send_keys('State/Province')  # This value is not specified in the problem
        postal_code_input.send_keys('1234')
        phone_number_input.send_keys('1234567891')

        # Accept terms checkbox
        accept_terms_checkbox = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, 'terms')))
        if accept_terms_checkbox.is_enabled():
            accept_terms_checkbox.click()

        # Wait for any maps popups or warnings and close them.
        WebDriverWait(self.driver, 20).until_not(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.modal')))

        # Confirm success if form is filled
        self.assertTrue(company_input.get_attribute('value') == 'Comp1')
        self.assertTrue(address_input.get_attribute('value') == 'Street1')
        self.assertTrue(city_input.get_attribute('value') == 'Quebec')
        self.assertTrue(region_input.get_attribute('value') == '')
        self.assertTrue(postal_code_input.get_attribute('value') == '1234')
        self.assertTrue(phone_number_input.get_attribute('value') == '1234567891')

if __name__ == "__main__":
    unittest.main()