import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestPageLoad(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def test_page_load(self):
        # Open the page.
        url = "http://localhost:8080/en/"
        self.driver.get(url)

        # Confirm the presence of key interface elements.
        self.assertIn("Navigation links", self.driver.page_source)
        self.assertIn("Inputs", self.driver.page_source)
        self.assertIn("Buttons", self.driver.page_source)
        self.assertIn("Banners", self.driver.page_source)

        # Interact with one or two elements — e.g., click a button and check that the UI updates visually.
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#ui-id-1"))
        )
        button.click()

        # Verify that interactive elements do not cause errors in the UI.
        self.assertEqual(self.driver.title, "Title of the page")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()