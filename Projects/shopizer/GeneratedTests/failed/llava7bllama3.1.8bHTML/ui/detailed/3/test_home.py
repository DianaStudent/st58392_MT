from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

class TestUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_ui_elements(self):
        # Load the page
        self.driver.get("http://localhost/")

        # Check that structural elements are visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "header")))
        self.assertIsNotNone(header)

        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.TAG_NAME, "footer")))
        self.assertIsNotNone(footer)

        # Check the presence and visibility of input fields, buttons, labels, and sections
        navigation_links = self.driver.find_elements(By.XPATH, "//nav/ul/li/a")
        for link in navigation_links:
            self.assertTrue(link.is_displayed())

        login_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        self.assertIsNotNone(login_link)

        register_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Register")))
        self.assertIsNotNone(register_link)

        # Interact with key UI elements
        login_link.click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "username")))

        # Assert that no required UI element is missing
        self.assertIsNotNone(header)
        self.assertIsNotNone(footer)
        self.assertTrue(login_link.is_displayed())
        self.assertTrue(register_link.is_displayed())

if __name__ == "__main__":
    unittest.main()