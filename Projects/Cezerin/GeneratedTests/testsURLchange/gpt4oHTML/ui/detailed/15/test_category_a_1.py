import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class UITest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8," + html_data['html'])

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Step 1: Load the page and ensure that structural elements are visible.
        try:
            header = wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )
            footer = wait.until(
                EC.visibility_of_element_located((By.TAG_NAME, "footer"))
            )
            nav = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "primary-nav"))
            )
        except:
            self.fail("Basic structural elements (header, footer, navigation) not visible.")

        # Step 2: Check the presence and visibility of input fields, buttons, labels, and sections.
        try:
            search_input = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-input"))
            )
            price_filter = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "price-filter"))
            )
        except:
            self.fail("Input fields or sections are missing or not visible.")

        # Step 3: Interact with key UI elements and check the reaction.
        try:
            search_button = driver.find_element(By.CLASS_NAME, "search-icon-search")
            search_button.click()

            sort_dropdown = driver.find_element(By.XPATH, "//select")
            sort_dropdown.click()
        except:
            self.fail("Unable to interact with UI elements.")

        # Additional step: Validate that buttons are present and visible
        try:
            cart_button = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, "cart-button"))
            )
            filter_button = wait.until(
                EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Filter products')]"))
            )
        except:
            self.fail("Required buttons are missing or not visible.")

    def tearDown(self):
        # Clean up and close the browser.
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()