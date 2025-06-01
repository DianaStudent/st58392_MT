from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://example.com")  # Use the actual URL for the test
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Ensure structural elements are visible
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))

            # Ensure input fields, buttons, labels, and sections are visible
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-icon-search')))
            cart_icon = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))

            # Ensure image gallery and bullets are visible
            image_gallery = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'home-slider')))
            bullets = wait.until(EC.visibility_of_all_elements_located((By.CLASS_NAME, 'image-gallery-bullet')))

            # Interact with key UI elements
            category_a_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Category A')))
            category_a_link.click()

            # Check if navigated to correct page
            subcategory_1_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, 'Subcategory 1')))
            self.assertIsNotNone(subcategory_1_link, "Subcategory 1 link not visible or does not exist")

            # Assert that no required UI element is missing
            for ele in [header, footer, nav, search_input, search_button, cart_icon, best_sellers_title, image_gallery]:
                self.assertIsNotNone(ele, f"{ele} is missing from the UI or not visible")

        except Exception as e:
            self.fail(f"UI elements missing or not functioning properly: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()