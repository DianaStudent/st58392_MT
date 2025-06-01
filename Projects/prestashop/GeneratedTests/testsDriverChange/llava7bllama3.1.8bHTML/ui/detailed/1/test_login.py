import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestPageStructure(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_page_structure(self):
        # Test header and footer are visible
        header_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'header'))
        )
        self.assertTrue(header_element.is_displayed())

        footer_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'footer'))
        )
        self.assertTrue(footer_element.is_displayed())

        # Test navigation is present and visible
        nav_element = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'nav'))
        )
        self.assertTrue(nav_element.is_displayed())

        # Test input fields are present and visible
        search_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'search_query_top'))
        )
        self.assertTrue(search_input.is_displayed())

        # Test buttons are present and visible
        login_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[text()='Login']"))
        )
        self.assertTrue(login_button.is_displayed())

        # Interact with key UI elements (e.g., click button)
        login_button.click()

    def test_login_page(self):
        self.driver.get("http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

        # Test input fields are present and visible
        username_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'email'))
        )
        self.assertTrue(username_input.is_displayed())

        password_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'passwd'))
        )
        self.assertTrue(password_input.is_displayed())

    def test_register_page(self):
        self.driver.get("http://localhost:8080/en/registration")

        # Test input fields are present and visible
        username_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.ID, 'email'))
        )
        self.assertTrue(username_input.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()