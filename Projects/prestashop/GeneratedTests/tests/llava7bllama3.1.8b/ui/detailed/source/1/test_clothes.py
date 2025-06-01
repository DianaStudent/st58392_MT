import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceSite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_structural_elements(self):
        # Check header visibility
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#header"))
        )

        # Check footer visibility
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#footer"))
        )

        # Check navigation menu items
        nav_menu_items = self.driver.find_elements(By.CSS_SELECTOR, ".nav-menu-item")
        self.assertEqual(len(nav_menu_items), 6)

    def test_input_fields_buttons_labels(self):
        # Check input fields presence
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.NAME, "input-field"))
        )

        # Check buttons presence
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#submit-button"))
        )

        # Check labels presence
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "label"))
        )

    def test_interaction_with_ui_elements(self):
        # Click submit button and check if page changes
        self.driver.find_element(By.CSS_SELECTOR, "#submit-button").click()
        WebDriverWait(self.driver, 10).until(
            EC.url_changes(self.driver.current_url)
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()