import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='home-header']")))
        self.assertEqual(header.text, "Home Page")

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".home-buttons button")))
        self.assertEqual(len(buttons), 2)

        # Links
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".home-links a")))
        self.assertEqual(len(links), 3)
        for link in links:
            self.assertIn(link.text, ["Tables", "Chairs", "Login"])

        # Form Fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".home-form input")))
        self.assertEqual(len(form_fields), 2)

    def test_tables_ui_components(self):
        self.driver.get("http://localhost/category/tables")
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='category-header']")))
        self.assertEqual(header.text, "Tables")

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".category-buttons button")))
        self.assertEqual(len(buttons), 2)

        # Links
        links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".category-links a")))
        self.assertEqual(len(links), 3)
        for link in links:
            self.assertIn(link.text, ["Chairs", "Login", "Register"])

    def test_chairs_ui_components(self):
        self.driver.get("http://localhost/category/chairs")
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='category-header']")))
        self.assertEqual(header.text, "Chairs")

    def test_login_ui_components(self):
        self.driver.get("http://localhost/login")
        # Form Fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".login-form input")))
        self.assertEqual(len(form_fields), 2)

    def test_register_ui_components(self):
        self.driver.get("http://localhost/register")
        # Form Fields
        form_fields = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".register-form input")))
        self.assertEqual(len(form_fields), 3)


if __name__ == '__main__':
    unittest.main()