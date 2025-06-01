import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class NopCommerceTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()

    def test_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Load the home page
        driver.get("http://max/")
        
        # 2. Ensure structural elements (header, footer, navigation) are visible
        try:
            header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
            footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))
        except Exception as e:
            self.fail(f"Structural element missing or not visible: {str(e)}")

        # 3. Check input fields, buttons, labels, and sections
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        except Exception as e:
            self.fail(f"Input field or button missing or not visible: {str(e)}")

        # 4. Interact with key UI elements (e.g., click buttons)
        search_box.send_keys("book")
        search_button.click()

        # 5. Confirm that the UI reacts visually
        try:
            products_container = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "products-container")))
        except Exception as e:
            self.fail(f"UI did not react visually: {str(e)}")

        # 6. Assert that no required UI element is missing
        key_elements = [
            (By.CLASS_NAME, "header"),
            (By.CLASS_NAME, "footer"),
            (By.CLASS_NAME, "header-menu"),
            (By.CLASS_NAME, "search-box"),
            (By.CLASS_NAME, "search-box-button"),
            (By.CLASS_NAME, "products-container"),
            (By.CLASS_NAME, "master-wrapper-content")
        ]

        for by, value in key_elements:
            try:
                wait.until(EC.visibility_of_element_located((by, value)))
            except Exception as e:
                self.fail(f"Required UI element is missing or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()