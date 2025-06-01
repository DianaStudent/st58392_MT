from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost/')
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_UI_elements_present(self):
        driver = self.driver

        # Check visibility of header
        header = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertTrue(header.is_displayed(), "Header is not visible")

        # Check visibility of footer
        footer = driver.find_element(By.CLASS_NAME, 'footer-area')
        self.assertTrue(footer.is_displayed(), "Footer is not visible")

        # Check visibility of main navigation links
        home_link = driver.find_element(By.LINK_TEXT, 'Home')
        tables_link = driver.find_element(By.LINK_TEXT, 'Tables')
        chairs_link = driver.find_element(By.LINK_TEXT, 'Chairs')
        self.assertTrue(home_link.is_displayed(), "Home link is not visible")
        self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")
        self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")

        # Check presence of login and register links
        login_link = driver.find_element(By.LINK_TEXT, 'Login')
        register_link = driver.find_element(By.LINK_TEXT, 'Register')
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Interact with cookie consent button
        cookie_button = self.wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        cookie_button.click()

        # Check cart button presence
        cart_button = driver.find_element(By.CLASS_NAME, 'icon-cart')
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Verify product section is visible
        product_section = driver.find_element(By.CLASS_NAME, 'shop-area')
        self.assertTrue(product_section.is_displayed(), "Product section is not visible")

if __name__ == "__main__":
    unittest.main()