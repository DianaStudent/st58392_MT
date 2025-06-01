from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_page_structure(self):
        self.driver.get("http://max/")

        # Check the presence of key interface elements:
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#nav li"))
        )
        self.assertEqual(len(nav_links), 5)

        inputs = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']"))
        )
        self.assertEqual(len(inputs), 2)

        buttons = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[type='submit']"))
        )
        self.assertEqual(len(buttons), 1)

        banners = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".banner"))
        )
        self.assertEqual(len(banners), 2)

        # Interact with one or two elements:
        login_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        login_button.click()

        # Verify that interactive elements do not cause errors in the UI.
        self.assertEqual(len(nav_links), 5)

    def test_search_page_structure(self):
        self.driver.get("http://max/search")

        # Check the presence of key interface elements:
        search_input = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        self.assertEqual(search_input.get_attribute('placeholder'), 'Search')

        search_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        self.assertEqual(search_button.get_attribute('type'), 'submit')

if __name__ == "__main__":
    unittest.main()