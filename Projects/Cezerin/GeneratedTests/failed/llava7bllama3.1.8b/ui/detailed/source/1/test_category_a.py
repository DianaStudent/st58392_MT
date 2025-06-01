from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUIElements(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_ui_elements(self):
        # Wait for structural elements to be visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Check presence and visibility of main UI components
        self.assertIsNotNone(self.driver.find_element(By.TAG_NAME, "h1"))
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "h1").is_displayed())

        self.assertIsNotNone(self.driver.find_element(By.TAG_NAME, "nav"))
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "nav").is_displayed())

        # Click on category_a link
        self.driver.find_element(By.LINK_TEXT, "Category A").click()

        # Wait for structural elements to be visible in category_a page
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Check presence and visibility of main UI components in category_a page
        self.assertIsNotNone(self.driver.find_element(By.TAG_NAME, "h1"))
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "h1").is_displayed())

        self.assertIsNotNone(self.driver.find_element(By.TAG_NAME, "nav"))
        self.assertTrue(self.driver.find_element(By.TAG_NAME, "nav").is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()