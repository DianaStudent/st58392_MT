from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestShopperCategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_shopper_category_page(self):
        driver = self.driver
        driver.get("http://localhost/category/chairs")

        # Wait for the page to load and ensure structural elements are visible
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'h1')))

        # Check presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(driver.find_element(By.TAG_NAME, 'h1').is_displayed())
        self.assertTrue(driver.find_element(By.TAG_NAME, 'button[type="submit"]').is_displayed())

        # Interact with key UI elements (e.g., click buttons)
        driver.find_element(By.TAG_NAME, 'button[type="submit"]').click()

        # Confirm that the UI reacts visually
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'div')))

        # Assert that no required UI element is missing
        self.assertTrue(len(driver.find_elements(By.TAG_NAME, 'h1')) > 0)
        self.assertTrue(len(driver.find_elements(By.TAG_NAME, 'button[type="submit"]')) > 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()