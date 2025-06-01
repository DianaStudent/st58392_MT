import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_main_ui_components(self):
        # Wait for main UI components to be present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#navbarSupportedContent"))
        )

        # Check that header is visible
        self.assertIsNotNone(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//header"))))

        # Check that buttons and links are present and visible
        self.assertIsNotNone(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']"))))
        self.assertIsNotNone(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, "Tables"))))

        # Check that form fields are present and visible
        self.assertIsNotNone(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "username"))))
        self.assertIsNotNone(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "password"))))

    def test_tables_link_present(self):
        # Go to tables page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Tables"))
        ).click()

        # Check that URL has changed to tables page
        self.assertEqual(self.driver.current_url, "http://localhost/category/tables")

    def test_chairs_link_present(self):
        # Go to chairs page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Chairs"))
        ).click()

        # Check that URL has changed to chairs page
        self.assertEqual(self.driver.current_url, "http://localhost/category/chairs")

    def test_login_link_present(self):
        # Go to login page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
        ).click()

        # Check that URL has changed to login page
        self.assertEqual(self.driver.current_url, "http://localhost/login")

    def test_register_link_present(self):
        # Go to register page
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
        ).click()

        # Check that URL has changed to register page
        self.assertEqual(self.driver.current_url, "http://localhost/register")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()