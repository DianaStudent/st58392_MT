from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 20)
        self.base_url = "http://localhost/"

    def test_ui_elements(self):
        driver = self.driver
        driver.get(self.base_url)

        # Check navigation links
        navigation_links = [
            (By.LINK_TEXT, "Home"),
            (By.LINK_TEXT, "Tables"),
            (By.LINK_TEXT, "Chairs")
        ]

        for by, value in navigation_links:
            link = self.wait.until(EC.visibility_of_element_located((by, value)))
            self.assertTrue(link.is_displayed(), f"{value} link is not visible")

        # Check login and register links in account dropdown
        account_dropdown_button = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".account-setting-active")))
        self.assertTrue(account_dropdown_button.is_displayed(), "Account dropdown button is not visible")
        account_dropdown_button.click()

        login_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
        self.assertTrue(login_link.is_displayed(), "Login link is not visible")

        register_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
        self.assertTrue(register_link.is_displayed(), "Register link is not visible")

        # Check presence of cart button
        cart_button = self.wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".icon-cart"))
        )
        self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

        # Check that Accept cookies button is present
        accept_cookies_button = self.wait.until(EC.visibility_of_element_located(
            (By.ID, "rcc-confirm-button"))
        )
        self.assertTrue(accept_cookies_button.is_displayed(), "Accept cookies button is not visible")

        # Interact with the cookies button
        accept_cookies_button.click()
        self.assertTrue(accept_cookies_button.is_enabled(), "Accept Cookies button interaction failed")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()