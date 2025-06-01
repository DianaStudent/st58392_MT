from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMainPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_main_page_elements(self):
        # Open the webpage in a new browser session
        self.driver.get("https://example.com")

        # Wait for 20 seconds to ensure all elements are loaded before interacting with them
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located)

        # Verify that headers exist and are visible
        headers = self.driver.find_elements(By.CSS_SELECTOR, "h1")
        self.assertGreater(len(headers), 0)
        for header in headers:
            self.assertTrue(header.is_displayed())

        # Verify that buttons exist and are visible
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        self.assertGreater(len(buttons), 0)
        for button in buttons:
            self.assertTrue(button.is_displayed())

        # Verify that links exist and are visible
        links = self.driver.find_elements(By.TAG_NAME, "a")
        self.assertGreater(len(links), 0)
        for link in links:
            self.assertTrue(link.is_displayed())

        # Verify that form fields exist and are visible
        form_fields = self.driver.find_elements(By.TAG_NAME, "input")
        self.assertGreater(len(form_fields), 0)
        for field in form_fields:
            self.assertTrue(field.is_displayed())

    def test_category_a_links(self):
        # Find all links with text 'Category A'
        category_a_links = self.driver.find_elements(By.XPATH, "//a[text()='Category A']")

        # Wait for the links to be clickable
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Category A']")))

        # Verify that there are at least two category 'A' links present on the page
        self.assertGreater(len(category_a_links), 1)
        for link in category_a_links:
            self.assertTrue(link.is_enabled())

    def test_category_a_1_link(self):
        # Find all links with text 'Category A - 1'
        category_a_1_link = self.driver.find_element(By.XPATH, "//a[text()='Category A - 1']")

        # Verify that the link is present and visible
        self.assertTrue(category_a_1_link.is_displayed())

        # Click on the link
        category_a_1_link.click()

        # Wait for the page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located)

        # Verify that the link has been successfully clicked
        self.assertTrue(category_a_1_link.is_enabled())
        self.assertEqual(category_a_1_link.text, "Category A - 1")

if __name__ == "__main__":
    unittest.main()