from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_main_elements_present(self):
        # Header present and visible
        header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "nav#header"))
        )
        self.assertTrue(header.is_displayed())

        # Navigation links present and visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#columns > div > ul > li"))
        )
        for link in nav_links:
            self.assertTrue(link.is_displayed())

        # Footer present and visible
        footer = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "div#footer"))
        )
        self.assertTrue(footer.is_displayed())

    def test_input_fields_buttons_labels_sections_present(self):
        # Input fields (search bar) present and visible
        search_bar = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_query_top"))
        )
        self.assertTrue(search_bar.is_displayed())

        # Buttons (cart button) present and visible
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a#top.links .btn"));
        )
        self.assertTrue(cart_button.is_displayed())

        # Labels and sections present and visible
        labels_sections = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".category-name"))
        )
        for label_section in labels_sections:
            self.assertTrue(label_section.is_displayed())

    def test_interact_with_ui_elements(self):
        # Click on "Clothes" category link
        clothes_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Clothes']"))
        )
        clothes_link.click()

        # Assert page title changes to "Clothes"
        self.assertEqual("Clothes", self.driver.title)

    def test_visual_reaction(self):
        # Check that the UI reacts visually (e.g., categories change)
        art_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@title='Art']"))
        )
        art_link.click()

        # Assert page title changes to "Art"
        self.assertEqual("Art", self.driver.title)

if __name__ == "__main__":
    unittest.main()