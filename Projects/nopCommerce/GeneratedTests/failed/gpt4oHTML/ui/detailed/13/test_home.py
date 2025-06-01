from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSeleniumUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.driver.maximize_window()

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the presence of the main header and footer
        try:
            header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.header')))
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.footer')))
        except Exception as e:
            self.fail(f"Main UI components are missing: {str(e)}")

        # Check the presence and visibility of navigation links in the header
        navigation_elements = [
            "a.ico-register",
            "a.ico-login",
            "a.ico-wishlist",
            "a.ico-cart",
            "li a[href='/']",
            "li a[href='/newproducts']",
            "li a[href='/search']",
            "li a[href='/customer/info']",
            "li a[href='/blog']",
            "li a[href='/contactus']"
        ]

        for nav_selector in navigation_elements:
            try:
                nav_element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, nav_selector)))
            except Exception as e:
                self.fail(f"Navigation UI element missing: {nav_selector}, Exception: {str(e)}")

        # Check the presence and visibility of the search box form
        try:
            search_form = wait.until(EC.visibility_of_element_located((By.ID, "small-search-box-form")))
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
        except Exception as e:
            self.fail(f"Search UI components are missing: {str(e)}")

        # Check Visibility of Notification and Cart Components
        notification_bar = driver.find_element(By.ID, "bar-notification")
        self.assertTrue(notification_bar.is_displayed(), "Notification bar is not visible.")

        cart_flyout = driver.find_element(By.ID, "flyout-cart")
        self.assertFalse(cart_flyout.is_displayed(), "Flyout cart should not be initially visible.")

        # Interact with the Search Elements
        try:
            search_input.send_keys("Test item")
            search_button.click()
            wait.until(EC.visibility_of_element_located((By.ID, "ui-id-1")))
        except Exception as e:
            self.fail(f"Interacting with the search components failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()