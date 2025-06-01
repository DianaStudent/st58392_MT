from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestEcommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_elements_present(self):
        # Confirm the presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.navbar-nav li a"))
        )
        self.assertGreater(len(navigation_links), 0)

        search_bar = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.ID, "search-bar"))
        )
        self.assertIsNotNone(search_bar)

        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".promotional-banner"))
        )
        self.assertIsNotNone(banner)

    def test_interact_with_button(self):
        # Interact with one or two elements
        button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.ID, "some-button-id"))
        )
        button.click()

        # Check that the UI updates visually
        new_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".new-element"))
        )
        self.assertIsNotNone(new_element)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()