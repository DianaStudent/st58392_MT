import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestHomeCategory1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        os.environ["webdriver.chrome.driver"] = "/usr/bin/chromedriver"
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.get("http://example.com")  # Replace with your URL

    def test_navigation_links(self):
        navigation_links = self.driver.find_elements(By.XPATH, "//nav/ul/li/a")
        self.assertEqual(len(navigation_links), 5)
        for link in navigation_links:
            self.assertIsNotNone(link.text)

    def test_header_and_title(self):
        header = self.driver.find_element(By.XPATH, "//h1")
        title = self.driver.title
        self.assertIn("Category A", header.text)
        self.assertIn("Category A | Example", title)

    def test_form_fields(self):
        form_fields = self.driver.find_elements(By.TAG_NAME, "input")
        self.assertEqual(len(form_fields), 5)
        for field in form_fields:
            self.assertIsNotNone(field.get_attribute("placeholder"))

    def test_banners_and_buttons(self):
        banners = self.driver.find_elements(By.XPATH, "//div[@class='banner']")
        buttons = self.driver.find_elements(By.TAG_NAME, "button")
        self.assertEqual(len(banners), 3)
        self.assertEqual(len(buttons), 2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()