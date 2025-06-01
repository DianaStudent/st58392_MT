import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost/')
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check for header
        header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'header.header-area')))
        self.assertIsNotNone(header, "Header is not present or not visible.")

        # Check for home link
        home_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        self.assertIsNotNone(home_link, "Home link is not present or not visible.")

        # Check for tables link
        tables_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        self.assertIsNotNone(tables_link, "Tables link is not present or not visible.")

        # Check for chairs link
        chairs_link = self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        self.assertIsNotNone(chairs_link, "Chairs link is not present or not visible.")

        # Check for account settings button
        account_button = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button.account-setting-active')))
        self.assertIsNotNone(account_button, "Account setting button is not present or not visible.")

        # Check the login link
        driver.get('http://localhost/login')
        login_header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
        self.assertIsNotNone(login_header, "Login page is not present or not visible.")

        # Check the register link
        driver.get('http://localhost/register')
        register_header = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3')))
        self.assertIsNotNone(register_header, "Register page is not present or not visible.")

        # Return to home
        driver.get('http://localhost/')

        # Check for footer
        footer = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'footer.footer-area')))
        self.assertIsNotNone(footer, "Footer is not present or not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()