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
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Verify header exists
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'header-area')))
        self.assertIsNotNone(header, "Header is not visible")

        # Verify home link in main menu
        home_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Home')))
        self.assertIsNotNone(home_link, "Home link is not visible")

        # Verify tables link in main menu
        tables_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Tables')))
        self.assertIsNotNone(tables_link, "Tables link is not visible")

        # Verify chairs link in main menu
        chairs_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Chairs')))
        self.assertIsNotNone(chairs_link, "Chairs link is not visible")

        # Verify login link in account menu
        account_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'account-setting-active')))
        account_button.click()  # Assuming a dropdown needs to be clicked to reveal login link
        login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Login')))
        self.assertIsNotNone(login_link, "Login link is not visible")

        # Verify register link in account menu
        register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Register')))
        self.assertIsNotNone(register_link, "Register link is not visible")

        # Verify search form field
        # Assuming there is a search input field to be verified
        # Uncomment the following line if there is a search input field
        # search_field = wait.until(EC.visibility_of_element_located((By.NAME, 'search_query')))
        # self.assertIsNotNone(search_field, "Search field is not visible")

        # Verify footer presence
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'footer-area')))
        self.assertIsNotNone(footer, "Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()