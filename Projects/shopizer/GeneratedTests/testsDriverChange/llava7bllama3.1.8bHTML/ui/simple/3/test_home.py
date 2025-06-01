import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check main header is present
        main_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Main Header']"))
        )
        self.assertIsNotNone(main_header)
        self.assertTrue(main_header.is_displayed())

        # Check buttons are present
        buttons = self.driver.find_elements(By.CSS_SELECTOR, "button")
        for button in buttons:
            self.assertIsNotNone(button)
            self.assertTrue(button.is_displayed())

        # Check links are present
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            self.assertIsNotNone(link)
            self.assertTrue(link.is_displayed())

        # Check form fields are present
        form_fields = self.driver.find_elements(By.NAME, "email")
        for field in form_fields:
            self.assertIsNotNone(field)
            self.assertTrue(field.is_displayed())

    def test_tables_page_ui_components(self):
        self.driver.get("http://localhost/category/tables")
        main_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Tables']"))
        )
        self.assertIsNotNone(main_header)
        self.assertTrue(main_header.is_displayed())

    def test_chairs_page_ui_components(self):
        self.driver.get("http://localhost/category/chairs")
        main_header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//h1[text()='Chairs']"))
        )
        self.assertIsNotNone(main_header)
        self.assertTrue(main_header.is_displayed())

    def test_login_page_ui_components(self):
        self.driver.get("http://localhost/login")
        login_form = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "login-form"))
        )
        self.assertIsNotNone(login_form)
        self.assertTrue(login_form.is_displayed())

    def test_register_page_ui_components(self):
        self.driver.get("http://localhost/register")
        register_form = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "register-form"))
        )
        self.assertIsNotNone(register_form)
        self.assertTrue(register_form.is_displayed())

if __name__ == "__main__":
    unittest.main()