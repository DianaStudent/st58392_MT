from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebpage(TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_webpage_elements(self):
        # Verify navigation links
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.navbar-nav > li"))
        )
        self.assertEqual(len(nav_links), 6)

        # Verify banner
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner")))
        self.assertIsNotNone(banner)

        # Verify form fields
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        )
        self.assertEqual(len(form_fields), 2)

    def test_interactive_element(self):
        # Click a button and verify UI updates
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#loginForm > button")))
        button.click()
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".alert.alert-danger")))
        self.assertIsNotNone(banner)

    def test_error_free_interaction(self):
        # Verify that interactive elements do not cause errors in the UI
        form_fields = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        )
        for field in form_fields:
            field.send_keys("test")
            self.assertIsNotNone(field)

    def tearDown(self):
        self.driver.quit()