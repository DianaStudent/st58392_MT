import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost/")

    def test_home_page_components(self):
        # Wait for the main header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1")))

        # Check that the main UI components are present
        self.assertUIComponentsPresent()

    def assertUIComponentsPresent(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, 'h1')))
        self.assertIsNotNone(header.text, "Header text is None")

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".btn")))
        self.assertGreater(len(buttons), 0, "No buttons found")

        # Links
        links = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "a")))
        self.assertGreater(len(links), 0, "No links found")

        # Form fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'input')))
        self.assertGreater(len(form_fields), 0, "No form fields found")

    def test_tables_link_exists(self):
        tables_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'tables')))
        self.assertIsNotNone(tables_link, "Tables link not found")
        tables_link.click()

        # Check that the correct page is loaded
        current_url = self.driver.current_url
        self.assertEqual(current_url, "http://localhost/category/tables", "Incorrect URL")

    def test_chairs_link_exists(self):
        chairs_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'chairs')))
        self.assertIsNotNone(chairs_link, "Chairs link not found")
        chairs_link.click()

        # Check that the correct page is loaded
        current_url = self.driver.current_url
        self.assertEqual(current_url, "http://localhost/category/chairs", "Incorrect URL")

    def test_login_link_exists(self):
        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'login')))
        self.assertIsNotNone(login_link, "Login link not found")
        login_link.click()

        # Check that the correct page is loaded
        current_url = self.driver.current_url
        self.assertEqual(current_url, "http://localhost/login", "Incorrect URL")

    def test_register_link_exists(self):
        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'register')))
        self.assertIsNotNone(register_link, "Register link not found")
        register_link.click()

        # Check that the correct page is loaded
        current_url = self.driver.current_url
        self.assertEqual(current_url, "http://localhost/register", "Incorrect URL")

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()