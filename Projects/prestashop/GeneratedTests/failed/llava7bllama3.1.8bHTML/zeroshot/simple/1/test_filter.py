from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFiltering(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_filtering(self):
        # Wait for the filter sidebar
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".filter-sidebar")))

        # Select a checkbox filter by its label text
        checkbox_label = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Checkbox Label']")))
        checkbox_input = checkbox_label.find_element(By.XPATH, "..//input")
        checkbox_input.click()

        # Wait for the product list to change
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.find_elements_by_css_selector(".product-item")) != 7)

        # Verify that the number of visible product items changes
        self.assertLess(len(self.driver.find_elements_by_css_selector(".product-item")), 7)

        # Select another checkbox filter by its label text
        checkbox_label = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//label[text()='Another Checkbox Label']")))
        checkbox_input = checkbox_label.find_element(By.XPATH, "..//input")
        checkbox_input.click()

        # Wait for the product list to change again
        WebDriverWait(self.driver, 20).until(lambda x: len(self.driver.find_elements_by_css_selector(".product-item")) != len(self.driver.find_elements_by_css_selector(".product-item")))

        # Verify that the number of visible product items changes again
        self.assertLess(len(self.driver.find_elements_by_css_selector(".product-item")), len(self.driver.find_elements_by_css_selector(".product-item")))

if __name__ == "__main__":
    unittest.main()