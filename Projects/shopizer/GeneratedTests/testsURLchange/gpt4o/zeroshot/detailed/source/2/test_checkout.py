import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable
from webdriver_manager.chrome import ChromeDriverManager

class CheckoutProcessTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_user_checkout_process(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)
        
        # Click on login
        login_button = wait.until(presence_of_element_located((By.XPATH, "//a[text()='Login']")))
        login_button.click()

        # Enter login credentials
        email_field = wait.until(presence_of_element_located((By.NAME, "username")))
        email_field.send_keys("test22@user.com")
        
        password_field = driver.find_element(By.NAME, "loginPassword")
        password_field.send_keys("test**11")
        
        login_submit = driver.find_element(By.XPATH, "//button/span[text()='Login']")
        login_submit.click()

        # Navigate back to home page
        driver.get("http://localhost/")

        # Hover over the first product and add to cart
        first_product = wait.until(presence_of_element_located((By.XPATH, "//div[@class='product-wrap-2 mb-25']")))
        add_to_cart_button = first_product.find_element(By.XPATH, ".//button[@title='Add to cart']")
        driver.execute_script("arguments[0].scrollIntoView(true);", add_to_cart_button)
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart
        cart_icon = wait.until(presence_of_element_located((By.XPATH, "//button[@class='icon-cart']")))
        cart_icon.click()
        
        # Wait for popup to become visible and click "View Cart"
        view_cart_button = wait.until(presence_of_element_located((By.LINK_TEXT, "View Cart")))
        view_cart_button.click()

        # On the cart page, click "Proceed to Checkout"
        proceed_to_checkout = wait.until(presence_of_element_located((By.LINK_TEXT, "Proceed to Checkout")))
        proceed_to_checkout.click()

        # Fill out the billing form
        company_field = wait.until(presence_of_element_located((By.NAME, "company")))
        company_field.send_keys("Comp1")
        
        address_field = driver.find_element(By.ID, "autocomplete")
        address_field.send_keys("Street1")
        
        city_field = driver.find_element(By.NAME, "city")
        city_field.send_keys("Quebec")
        
        country_dropdown = driver.find_element(By.XPATH, "//select[@placeholder='Country']")
        for option in country_dropdown.find_elements_by_tag_name('option'):
            if option.text == 'Canada':
                option.click()
                break
        
        state_dropdown = driver.find_element(By.XPATH, "//select[@placeholder='State']")
        for option in state_dropdown.find_elements_by_tag_name('option'):
            if option.text == 'Quebec':
                option.click()
                break
        
        postal_code_field = driver.find_element(By.NAME, "postalCode")
        postal_code_field.send_keys("1234")
        
        phone_field = driver.find_element(By.NAME, "phone")
        phone_field.send_keys("1234567891")
        
        terms_checkbox = driver.find_element(By.NAME, "isAgree")
        if not terms_checkbox.is_selected():
            terms_checkbox.click()

        # Check that form is filled successfully
        self.assertEqual(company_field.get_attribute('value'), "Comp1")
        self.assertEqual(address_field.get_attribute('value'), "Street1")
        self.assertEqual(city_field.get_attribute('value'), "Quebec")
        self.assertEqual(state_dropdown.get_attribute('value'), "QC")
        self.assertEqual(postal_code_field.get_attribute('value'), "1234")
        self.assertEqual(phone_field.get_attribute('value'), "1234567891")
        self.assertTrue(terms_checkbox.is_selected(), "Terms checkbox is not selected")

if __name__ == "__main__":
    unittest.main()