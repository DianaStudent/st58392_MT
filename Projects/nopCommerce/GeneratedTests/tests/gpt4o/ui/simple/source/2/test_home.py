import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestHomePageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/")

    def test_ui_elements(self):
        driver = self.driver

        # Wait for header elements
        try:
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "header"))
            )
        except Exception as e:
            self.fail(f"Header is not visible: {e}")

        # Check if register link is present and visible
        try:
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-register"))
            )
            self.assertTrue(register_link.is_displayed(), "Register link is not visible.")
        except Exception as e:
            self.fail(f"Register link is missing or not visible: {e}")

        # Check if login link is present and visible
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".ico-login"))
            )
            self.assertTrue(login_link.is_displayed(), "Log in link is not visible.")
        except Exception as e:
            self.fail(f"Login link is missing or not visible: {e}")

        # Check if search box is present and visible
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-search-box-form"))
            )
            self.assertTrue(search_box.is_displayed(), "Search box is not visible.")
        except Exception as e:
            self.fail(f"Search box is missing or not visible: {e}")

        # Check if shopping cart link is present and visible
        try:
            cart_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "topcartlink"))
            )
            self.assertTrue(cart_link.is_displayed(), "Shopping cart link is not visible.")
        except Exception as e:
            self.fail(f"Shopping cart link is missing or not visible: {e}")

        # Check if menu items are visible
        menu_items = [
            (By.LINK_TEXT, "Home page"),
            (By.LINK_TEXT, "New products"),
            (By.LINK_TEXT, "Search"),
            (By.LINK_TEXT, "My account"),
            (By.LINK_TEXT, "Blog"),
            (By.LINK_TEXT, "Contact us")
        ]

        for locator in menu_items:
            try:
                menu_item = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located(locator)
                )
                self.assertTrue(menu_item.is_displayed(), f"{locator[1]} is not visible.")
            except Exception as e:
                self.fail(f"Menu item '{locator[1]}' is missing or not visible: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()