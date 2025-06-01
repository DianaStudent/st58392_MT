import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Navigation links
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav > ul > li"))
        )
        self.assertGreater(len(nav_links), 0)

        # Inputs and buttons
        form_inputs = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, "input"))
        )
        self.assertGreater(len(form_inputs), 0)
        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#search_query_top > button"))
        )

        # Banner
        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".header-container > .heading-text"))
        )
        self.assertIsNotNone(banner.text)

        # Interact with elements
        search_button.click()
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#search_query_top")))

    def test_ui_integrity(self):
        # Check interactive elements don't cause errors in UI
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav > ul > li"))
        )
        for link in nav_links:
            link.click()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".page-content")))

if __name__ == "__main__":
    unittest.main()