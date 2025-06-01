import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Check that the main UI components are present
        header = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "header"))
        )
        self.assertIsNotNone(header)
        self.assertTrue(header.is_displayed())

        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button"))
        )
        for button in buttons:
            self.assertIsNotNone(button)
            self.assertTrue(button.is_displayed())

        links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a"))
        )
        for link in links:
            self.assertIsNotNone(link)
            self.assertTrue(link.is_displayed())

        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        )
        for field in form_fields:
            self.assertIsNotNone(field)
            self.assertTrue(field.is_displayed())

    def test_login_button(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        self.assertIsNotNone(login_button)

    def test_register_link(self):
        register_link = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Register"))
        )
        self.assertIsNotNone(register_link)
        self.assertTrue(register_link.is_displayed())

    def test_search_field(self):
        search_field = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        self.assertIsNotNone(search_field)

if __name__ == "__main__":
    unittest.main()