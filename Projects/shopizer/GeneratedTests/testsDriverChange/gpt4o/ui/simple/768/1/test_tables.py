import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ShopizerUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_main_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for header logo
        try:
            header_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".logo a img")))
            self.assertTrue(header_logo.is_displayed(), "Header logo is not visible")
        except:
            self.fail("Header logo element missing.")

        # Check navigation links
        try:
            home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            self.assertTrue(home_link.is_displayed(), "Home link is not visible")
            self.assertTrue(tables_link.is_displayed(), "Tables link is not visible")
            self.assertTrue(chairs_link.is_displayed(), "Chairs link is not visible")
        except:
            self.fail("Navigation links are missing.")

        # Check for login and register links in account dropdown
        try:
            account_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".account-setting-active")))
            account_button.click()

            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

            self.assertTrue(login_link.is_displayed(), "Login link is not visible")
            self.assertTrue(register_link.is_displayed(), "Register link is not visible")
        except:
            self.fail("Account dropdown links are missing.")

        # Check cart icon
        try:
            cart_icon = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".icon-cart")))
            self.assertTrue(cart_icon.is_displayed(), "Cart icon is not visible")
        except:
            self.fail("Cart icon element missing.")

        # Check subscribe form
        try:
            subscribe_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form input[name='email']")))
            subscribe_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-form button")))

            self.assertTrue(subscribe_input.is_displayed(), "Subscribe input is not visible")
            self.assertTrue(subscribe_button.is_displayed(), "Subscribe button is not visible")
        except:
            self.fail("Subscribe form elements are missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()