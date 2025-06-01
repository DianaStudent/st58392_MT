from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestEcommerceUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:3000/category-a")

    def test_interface_elements(self):
        # Confirm the presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//nav//a"))
        )
        self.assertGreater(len(navigation_links), 1)

        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
        )
        self.assertIsNotNone(search_input)

        button_add_new = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[text()='Add New']"))
        )
        self.assertIsNotNone(button_add_new)

    def test_interactive_elements(self):
        # Interact with one or two elements
        search_input = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Search']"))
        )

        # Type something in the search input
        search_input.send_keys("test")

        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()