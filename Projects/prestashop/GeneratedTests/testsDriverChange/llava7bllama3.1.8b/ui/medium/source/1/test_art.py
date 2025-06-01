import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_ui_elements_present(self):
        # Wait for the UI to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@href='/en/home']")))

        # Check for navigation links
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//a[@href='/en/home']"))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//a[@href='/en/pages']"))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//a[@href='/en/products']"))

        # Check for form fields
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//input[@type='text']"))
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//textarea"))

        # Check for buttons
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']"))

    def test_ui_interact(self):
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@class='btn btn-primary']")))
        button = self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
        button.click()

        # Check that the UI updates visually
        self.assertIsNotNone(self.driver.find_element(By.XPATH, "//p[@id='message']"))

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()