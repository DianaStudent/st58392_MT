from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.service import Service as ChromeService

class TestFilter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_filter(self):
        # Apply the "Brand A" filter
        brand_a_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Brand A')]"))
        )
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(lambda x: x.title != self.driver.title)
        self.assertEqual(len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-card")))), 1)

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()
        WebDriverWait(self.driver, 2).until(lambda x: x.title != self.driver.title)
        self.assertEqual(len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-card")))), 2)

        # Use the interactive price slider component to change price filtering
        slider = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='range']")))
        slider.send_keys("50")
        WebDriverWait(self.driver, 2).until(lambda x: x.title != self.driver.title)
        self.assertEqual(len(WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, ".product-card")))), 1)

if __name__ == '__main__':
    unittest.main()