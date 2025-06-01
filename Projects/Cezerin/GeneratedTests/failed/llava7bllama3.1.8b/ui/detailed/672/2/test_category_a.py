from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def test_category_a_page(self):
        # Wait for the page to load and then find the header element
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'header')))

        # Find and verify the presence of key UI elements
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'header')), 0)
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'main')), 0)
        self.assertGreater(len(self.driver.find_elements(By.TAG_NAME, 'footer')), 0)

        # Click on the Save button and verify that it's clickable
        save_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        save_button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()