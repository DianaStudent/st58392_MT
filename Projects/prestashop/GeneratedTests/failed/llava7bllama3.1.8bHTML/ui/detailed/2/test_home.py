from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestArtPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get('http://localhost:8080/en/9-art')

    def test_main_elements_present(self):
        # Wait for elements to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.header')))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//ul[@class="nav"]')))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, 'main')))

        # Check elements are visible
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, '.header').is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, '//ul[@class="nav"]').is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, 'main').is_displayed())

    def test_input_fields_visible(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'name')))
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, 'email')))

        self.assertTrue(self.driver.find_element(By.NAME, 'name').is_displayed())
        self.assertTrue(self.driver.find_element(By.NAME, 'email').is_displayed())

    def test_button_clickable(self):
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[@type="submit"]')))

        button = self.driver.find_element(By.XPATH, '//button[@type="submit"]')
        self.assertTrue(button.is_enabled())
        button.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()