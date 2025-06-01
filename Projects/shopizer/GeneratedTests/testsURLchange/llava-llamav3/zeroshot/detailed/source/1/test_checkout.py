from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.assertions import Assert
from selenium.webdriver.support.ui import WebDriverWait

class TestSeleniumTask(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_task(self):
        # Open the home page.
        self.driver.get('http://localhost/')

        # Log in using credentials.
        email_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@name='email']"
        )
        email_field.send_keys("test22@user.com")
        password_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@name='password']"
        )
        password_field.send_keys("test**11")
        self.driver.find_element_by_name('login').click()

        # Navigate back to the home page.
        self.driver.find_element_by_name('backToHome').click()

        # Hover over the first product.
        product_hover = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//div[@class='product__container']"
        )
        hover_product = self.driver.move_to_element(product_hover)

        # Click the revealed "Add to cart" button.
        add_to_cart_button = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//button[@class='add-to-cart-button']"
        )
        add_to_cart_button.click()

        # Click the cart icon to open the popup cart.
        cart_icon = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//a[@title='View Cart']"
        )
        cart_icon.click()

        # Wait for the popup to become visible.
        WebDriverWait(self.driver, 20)

        # Click "View cart" or similar button inside the popup.
        view_cart_button = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//button[@class='view-cart-button']"
        )
        view_cart_button.click()

        # On the cart page, click the "Proceed to Checkout" button.
        proceed_to_checkout_button = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//a[@title='Proceed to Checkout']"
        )
        proceed_to_checkout_button.click()

        # Fill out the billing form:
        company_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@name='company']"
        )
        self.assertEqual(company_field.get_attribute('value'), 'Comp1')

        address_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@name='address']"
        )
        self.assertEqual(address_field.get_attribute('value'), 'Street1')

        city_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//select[@name='city']"
        )
        select_city = Select(city_field)
        select_city.select_by_value('Quebec')

        postal_code_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@name='postalCode']"
        )
        self.assertEqual(postal_code_field.get_attribute('value'), '1234')

        phone_number_field = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@name='phone']"
        )
        self.assertEqual(phone_number_field.get_attribute('value'), '1234567891')

        terms_checkbox = WebDriverWait(self.driver, 20).until(
            By.XPATH,
            "//input[@type='checkbox']"
        )
        self.assertTrue(terms_checkbox.is_selected())

        # Confirm success if form is filled.
        self.assertTrue(postal_code_field.get_attribute('value') != '')

    def test_task(self):
        pass

if __name__ == '__main__':
    unittest.main()