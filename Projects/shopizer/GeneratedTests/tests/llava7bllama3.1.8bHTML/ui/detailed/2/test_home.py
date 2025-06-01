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

    def test_home_page_structure(self):
        # Check structural elements are visible
        header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "header"))
        )
        self.assertTrue(header.is_displayed())

        footer = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, "footer"))
        )
        self.assertTrue(footer.is_displayed())

    def test_home_page_elements(self):
        # Check presence and visibility of input fields, buttons, labels, sections
        home_title = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#home > h1"))
        )
        self.assertTrue(home_title.is_displayed())

        tables_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "tables"))
        )
        self.assertTrue(tables_link.is_displayed())

    def test_tables_page_elements(self):
        # Interact with key UI elements (e.g., click buttons)
        tables_link.click()
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tables > h1"))
        )

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()