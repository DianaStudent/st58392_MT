from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from unittest import TestCase

class TestShop(TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://localhost:8080/en/")

    def test_main_ui_components(self):
        try:
            # Check if header exists and is visible
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1")))
            
            # Check if buttons exist and are visible
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']")))
            
            # Check if links exist and are visible
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/en/3-clothes']")))
            
            # Check if form fields exist and are visible
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.NAME, "email")))
            
        except (TimeoutException, NoSuchElementException):
            self.fail("Required element is missing")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()