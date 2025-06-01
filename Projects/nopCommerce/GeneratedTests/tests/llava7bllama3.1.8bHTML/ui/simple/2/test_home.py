import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_main_ui_components(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//header"))
        )
        self.assertTrue(header.is_displayed())

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "button"))
        )
        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Links
        links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
        )
        for link in links:
            self.assertTrue(link.is_displayed())

        # Form fields
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.NAME, "newsletter-email"))
        )
        self.assertEqual(len(form_fields), 1)
        self.assertTrue(form_fields[0].is_enabled())

    def test_login_page(self):
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='login?returnUrl=%2F']"))
        )
        login_button.click()

        # Check that the URL is correct
        self.assertEqual(self.driver.current_url, "http://max/login?returnUrl=%2F")

        # Login form fields
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.NAME, "username"))
        )
        self.assertEqual(len(form_fields), 1)
        self.assertTrue(form_fields[0].is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()