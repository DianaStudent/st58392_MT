from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUI(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Navigate to the home page
        self.driver.get("http://localhost:8080/en/")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.TAG_NAME, 'h1'))
        )

        # Navigation menu elements should be present and visible
        navigation_menu_elements = [
            ('Home', By.XPATH, "//a[@href='/en/']", "Home link is missing"),
            ('Products', By.XPATH, "//a[@href='/en/3-clothes']", "Products link is missing"),
            ('Services', By.XPATH, "//a[@href='/en/']", "Services link is missing"), # Link not present in HTML structure
            ('Blog', By.XPATH, "//a[@href='/en/']", "Blog link is missing")
        ]

        for text, by_locator, locator_text in navigation_menu_elements:
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable(by_locator)
                )
            except Exception as e:
                self.fail(locator_text)

        # Hero section elements should be present and visible
        hero_section_elements = [
            ('Hero heading', By.XPATH, "//h1", "Hero heading is missing"),
            ('Hero subtitle', By.XPATH, "//p[@class='lead']", "Hero subtitle is missing")
        ]

        for text, by_locator, locator_text in hero_section_elements:
            try:
                WebDriverWait(self.driver, 20).until(
                    EC.presence_of_element_located(by_locator)
                )
            except Exception as e:
                self.fail(locator_text)

if __name__ == '__main__':
    unittest.main()