from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class UITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")
        self.driver.maximize_window()

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
        self.assertIsNotNone(header, "Header is not present or not visible.")

        # Check footer visibility
        footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
        self.assertIsNotNone(footer, "Footer is not present or not visible.")

        # Check presence of navigation links
        home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/']")))
        self.assertIsNotNone(home_link, "Home link is not present or not visible.")

        tables_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/tables']")))
        self.assertIsNotNone(tables_link, "Tables link is not present or not visible.")
        
        chairs_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category/chairs']")))
        self.assertIsNotNone(chairs_link, "Chairs link is not present or not visible.")

        # Check presence of login and register links
        login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/login']")))
        self.assertIsNotNone(login_link, "Login link is not present or not visible.")

        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/register']")))
        self.assertIsNotNone(register_link, "Register link is not present or not visible.")

        # Check presence of Cookie Consent button and click
        cookie_button = wait.until(EC.visibility_of_element_located((By.ID, 'rcc-confirm-button')))
        self.assertIsNotNone(cookie_button, "Cookie Consent button is not present or not visible.")
        cookie_button.click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()