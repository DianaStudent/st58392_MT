import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_main_ui_components(self):
        driver = self.driver

        # Check header area
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area"))
            )
        except Exception as e:
            self.fail("Header area is not visible: " + str(e))

        # Check navigation links: Home, Tables, Chairs
        try:
            nav_home = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Home"))
            )
            nav_tables = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
            )
            nav_chairs = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
            )
        except Exception as e:
            self.fail("Navigation links are not visible: " + str(e))

        # Check login and register links
        try:
            login_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
            )
            register_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
            )
        except Exception as e:
            self.fail("Login or Register links are not visible: " + str(e))

        # Check for main menu, ensuring at least one operation is clickable
        try:
            menu_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-menu nav ul"))
            )
        except Exception as e:
            self.fail("Main menu is not visible: " + str(e))

        # Check if the Cookie Acceptance Button is present and visible
        try:
            cookie_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "rcc-confirm-button"))
            )
        except Exception as e:
            self.fail("Cookie acceptance button is not visible: " + str(e))

        # Check for products section
        try:
            products_section = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-area"))
            )
        except Exception as e:
            self.fail("Products section is not visible: " + str(e))

        # Check 'Subscribe' button is present and visible
        try:
            subscribe_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".subscribe-area-3 .subscribe-form-3 .button"))
            )
        except Exception as e:
            self.fail("Subscribe button is not visible: " + str(e))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()