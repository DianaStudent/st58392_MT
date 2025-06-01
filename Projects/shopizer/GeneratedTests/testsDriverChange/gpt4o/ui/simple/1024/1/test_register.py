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
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_ui_elements_visible(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header elements
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-area")))
            self.assertIsNotNone(header, "Header is missing")

            # Check logo
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.logo a img")))
            self.assertIsNotNone(logo, "Logo is missing")

            # Check navigation links
            nav_home = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
            nav_tables = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Tables")))
            nav_chairs = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Chairs")))

            self.assertIsNotNone(nav_home, "Home link is missing")
            self.assertIsNotNone(nav_tables, "Tables link is missing")
            self.assertIsNotNone(nav_chairs, "Chairs link is missing")

            # Check login/register links
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Login")))
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))

            self.assertIsNotNone(login_link, "Login link is missing")
            self.assertIsNotNone(register_link, "Register link is missing")

            # Check search box
            search_box = wait.until(EC.visibility_of_element_located((By.NAME, "email")))
            self.assertIsNotNone(search_box, "Search box is missing")

            # Check Accept cookies button
            accept_cookies_button = wait.until(EC.visibility_of_element_located((By.ID, "rcc-confirm-button")))
            self.assertIsNotNone(accept_cookies_button, "Accept cookies button is missing")

        except Exception as e:
            self.fail(f"UI element test failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()