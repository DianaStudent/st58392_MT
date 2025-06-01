import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIStructure(unittest.TestCase):

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver

        # Check visibility of structural elements
        try:
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )
        except:
            self.fail("Header is missing or not visible")

        try:
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "footer"))
            )
        except:
            self.fail("Footer is missing or not visible")

        # Check presence and visibility of input fields, buttons, labels, and sections
        try:
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.ID, "small-searchterms"))
            )
        except:
            self.fail("Search input field is missing or not visible")

        try:
            search_button = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "button.button-1.search-box-button"))
            )
        except:
            self.fail("Search button is missing or not visible")
        
        try:
            label_search_keyword = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.XPATH, "//label[@for='q']"))
            )
        except:
            self.fail("Search keyword label is missing or not visible")

        # Check interaction with key UI elements (e.g., click buttons)
        search_box.send_keys("book")
        search_button.click()

        # Confirm that the UI reacts visually
        try:
            search_result = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-results"))
            )
        except:
            self.fail("Search results are missing or not visible after performing search")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()