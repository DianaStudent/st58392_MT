import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import ActionChains

class TestFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://example.com")  # replace with actual URL
        self.driver.find_element(By.XPATH, "//a[@data-name='Art']").click()

    def wait_for_filter_sidebar(self):
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='filter-sidebar']"))
        )

    def apply_filter(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(), 'Matt paper')]//input"))
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='filter-sidebar']"))
        )

    def clear_filters(self):
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Clear all')]"))
        ).click()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='filter-sidebar']"))
        )

    def test_filter(self):
        self.wait_for_filter_sidebar()
        self.apply_filter()
        original_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']"))
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-tile']")))
        filtered_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']"))
        self.assertEqual(filtered_count, original_count - 4)
        self.clear_filters()
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='product-tile']")))
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='filter-sidebar']")))
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']")), original_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()