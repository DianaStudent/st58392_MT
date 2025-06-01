import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def test_home_page_elements(self):
        # Navigate to the home page
        self.driver.get("http://localhost/")

        # Verify navigation links are present and visible
        nav_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav a')))
        self.assertTrue(len(nav_links) > 0)

        # Verify banners are present and visible
        banners = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.banner')))
        self.assertTrue(len(banners) > 0)

        # Click the login link
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'Login')))
        login_link.click()

        # Verify that the page has changed and check if "Register" button is present
        register_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, 'register-button')))
        self.assertTrue(register_button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()