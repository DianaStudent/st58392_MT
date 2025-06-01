from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_navigation_links(self):
        navigation_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul li a")))
        self.assertGreater(len(navigation_links), 0)

    def test_inputs_and_buttons(self):
        inputs_and_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#header_inner form input, #header_inner form button")))
        self.assertGreater(len(inputs_and_buttons), 0)
        for element in inputs_and_buttons:
            element.click()

    def test_banners(self):
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#banner")))
        self.assertIsNotNone(banner)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()