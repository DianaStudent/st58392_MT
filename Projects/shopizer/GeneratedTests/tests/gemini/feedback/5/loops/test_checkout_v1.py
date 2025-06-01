import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

class CheckoutTest(unittest.TestCase):

    def setUp(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.base_url = "http://localhost/"

    def tearDown(self):
        self.driver.quit()

    def test_checkout_process(self):
        driver = self.driver
        driver.get(self.base_url)

        # 1. Accept cookies
        try:
            accept_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.ID, "rcc-confirm-button"))
            )
            accept_button.click()
        except:
            pass

        # 2. Log in
        login_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/login']"))
        )
        login_link.click()

        username_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, "loginPassword"))
        )
        login_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(.,'Login')]"))
        )

        username_field.send_keys("test22@user.com")
        password_field.send_keys("test**11")
        login_button.click()

        # 3. Navigate back to the home page
        home_link = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/']"))
        )
        home_link.click()

       # 4. Hover over the first product and add to cart
        product_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']"))
        )
        actions = ActionChains(driver)
        actions.move_to_element(product_element).perform()

        add_to_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='col-xl-3 col-md-6 col-lg-4 col-sm-6'][1]//div[@class='product-wrap-2 mb-25']//button[@title='Add to cart']"))
        )
        add_to_cart_button.click()

        # 5. Click the cart icon to open the popup cart
        cart_icon = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//button[@class='icon-cart']"))
        )
        cart_icon.click()

        # 6. Wait for the popup to become visible
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.CLASS_NAME, "shopping-cart-content.active"))
        )

        # 7. Click "View Cart" button inside the popup
        view_cart_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/cart' and contains(text(),'View Cart')]"))
        )
        view_cart_button.click()

        # 8. On the cart page, click the "Proceed to Checkout" button
        proceed_to_checkout_button = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[@href='/checkout' and contains(text(),'Proceed to Checkout')]"))
        )
        proceed_to_checkout_button.click()

        # 9. Fill out the billing form
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
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'State')]/following-sibling::select"))
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

        # Select Quebec from the state dropdown
        for option in state_dropdown.find_elements(By.TAG_NAME, 'option'):
            if option.text == 'Quebec':
                option.click()
                break

        postal_code_field.send_keys("1234")
        phone_field.send_keys("1234567891")

        # Accept terms checkbox
        terms_checkbox.click()

        # Verify that the billing form is filled
        self.assertEqual(company_field.get_attribute("value"), "Comp1")
        self.assertEqual(address_field.get_attribute("value"), "Street1")
        self.assertEqual(city_field.get_attribute("value"), "Quebec")
        self.assertEqual(postal_code_field.get_attribute("value"), "1234")
        self.assertEqual(phone_field.get_attribute("value"), "1234567891")
        self.assertTrue(terms_checkbox.is_selected())


if __name__ == "__main__":
    unittest.main()