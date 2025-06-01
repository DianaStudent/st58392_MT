import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        try:
            # Wait for elements to be visible
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "js-product-list"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "search_widget"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "block-categories"))
            )
            WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "footer"))
            )
        except Exception as e:
            self.fail(f"Required UI component is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()