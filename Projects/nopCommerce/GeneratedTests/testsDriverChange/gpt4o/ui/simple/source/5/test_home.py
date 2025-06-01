import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://max/')

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header links
        try:
            header_links = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-links')))
            self.assertTrue(header_links.is_displayed(), "Header links not visible")
        except:
            self.fail("Header links not found")

        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-logo')))
            self.assertTrue(logo.is_displayed(), "Logo not visible")
        except:
            self.fail("Logo not found")

        # Check search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, 'small-search-box-form')))
            self.assertTrue(search_box.is_displayed(), "Search box not visible")
        except:
            self.fail("Search box not found")

        # Check top menu
        try:
            top_menu = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'top-menu')))
            self.assertTrue(top_menu.is_displayed(), "Top menu not visible")
        except:
            self.fail("Top menu not found")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer')))
            self.assertTrue(footer.is_displayed(), "Footer not visible")
        except:
            self.fail("Footer not found")

        # Check Register button
        try:
            register_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-register')))
            self.assertTrue(register_button.is_displayed(), "Register button not visible")
        except:
            self.fail("Register button not found")

        # Check Login button
        try:
            login_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-login')))
            self.assertTrue(login_button.is_displayed(), "Login button not visible")
        except:
            self.fail("Login button not found")

        # Check Wishlist link
        try:
            wishlist_link = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-wishlist')))
            self.assertTrue(wishlist_link.is_displayed(), "Wishlist link not visible")
        except:
            self.fail("Wishlist link not found")

        # Check Shopping Cart link
        try:
            shopping_cart_link = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'ico-cart')))
            self.assertTrue(shopping_cart_link.is_displayed(), "Shopping cart link not visible")
        except:
            self.fail("Shopping cart link not found")

if __name__ == '__main__':
    unittest.main()