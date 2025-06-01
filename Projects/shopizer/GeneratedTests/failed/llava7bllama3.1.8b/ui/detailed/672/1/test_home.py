from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestShopWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost/")

    def test_ui_elements_present(self):
        # Structural elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Navigation links
        navigation_links = self.driver.find_elements(By.TAG_NAME, "nav")
        for link in navigation_links:
            self.assertTrue(link.is_displayed())

        # Main content elements
        main_content = self.driver.find_element(By.CSS_SELECTOR, ".main-content")
        self.assertTrue(main_content.is_displayed())

    def test_input_fields_visible(self):
        # Input fields (example taken from the html_data)
        input_fields = self.driver.find_elements(By.CSS_SELECTOR, "input[type='text']")
        for field in input_fields:
            self.assertTrue(field.is_enabled() and field.is_displayed())

    def test_button_click(self):
        # Button to click
        button_to_click = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn")))
        button_to_click.click()

        # Check UI reacts visually after clicking the button
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".react-toast-notifications__container")))

    def test_required_elements_not_missing(self):
        # Required elements (example taken from the html_data)
        required_elements = ["header", "footer", "nav", "main-content"]
        for element in required_elements:
            self.assertTrue(len(self.driver.find_elements(By.TAG_NAME, element)) > 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()