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

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver

        # Check if header is present and visible
        header = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "header.header-area"))
        )

        # Check if footer is present and visible
        footer = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "footer.footer-area"))
        )

        # Check if navigation is present and visible
        nav = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".main-menu nav"))
        )

        # Check presence of main buttons and links

        # Home link
        home_link = driver.find_element(By.CSS_SELECTOR, ".main-menu a[href='/']")
        if not home_link.is_displayed():
            self.fail("Home link is not visible")

        # Tables link
        tables_link = driver.find_element(By.CSS_SELECTOR, ".main-menu a[href='/category/tables']")
        if not tables_link.is_displayed():
            self.fail("Tables link is not visible")

        # Chairs link
        chairs_link = driver.find_element(By.CSS_SELECTOR, ".main-menu a[href='/category/chairs']")
        if not chairs_link.is_displayed():
            self.fail("Chairs link is not visible")

        # Login link
        login_link = driver.find_element(By.CSS_SELECTOR, ".account-dropdown a[href='/login']")
        if not login_link.is_displayed():
            self.fail("Login link is not visible")

        # Register link
        register_link = driver.find_element(By.CSS_SELECTOR, ".account-dropdown a[href='/register']")
        if not register_link.is_displayed():
            self.fail("Register link is not visible")

        # Subscribe button in footer
        subscribe_button = driver.find_element(By.CSS_SELECTOR, "footer .button")
        if not subscribe_button.is_displayed():
            self.fail("Subscribe button is not visible")

        # Interact with key UI elements
        # Click the cookie consent button if it exists
        try:
            consent_button = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.ID, "rcc-confirm-button"))
            )
            consent_button.click()
        except:
            self.fail("Consent button not clickable or missing")

if __name__ == "__main__":
    unittest.main()