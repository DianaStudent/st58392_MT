from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class UITestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/")

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check the header
        header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
        self.assertIsNotNone(header, "Header is not visible")

        # Check the menu links
        menu_links = [
            ("clothes", "http://localhost:8080/en/3-clothes"),
            ("accessories", "http://localhost:8080/en/6-accessories"),
            ("art", "http://localhost:8080/en/9-art")
        ]

        for category, url in menu_links:
            element = wait.until(EC.visibility_of_element_located((By.XPATH, f"//a[@href='{url}']")))
            self.assertIsNotNone(element, f"Category link for {category} not visible")

        # Check the login link
        login_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        self.assertIsNotNone(login_link, "Login link is not visible")

        # Check the register link
        register_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/registration']")))
        self.assertIsNotNone(register_link, "Register link is not visible")

        # Check for footer existence
        footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
        self.assertIsNotNone(footer, "Footer is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()