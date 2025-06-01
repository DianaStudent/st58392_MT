from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUITestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_page_structure_and_elements(self):
        # Check structural elements (header, footer, navigation)
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Check presence of input fields, buttons, labels, and sections
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.NAME, "search")))
        self.driver.find_element(By.NAME, "search").is_displayed()

        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
        self.driver.find_element(By.XPATH, "//button[@type='submit']").is_enabled()

        # Check interaction with key UI elements
        self.driver.find_element(By.NAME, "search").send_keys("test")
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "result")))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()