from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestECommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_homepage_elements(self):
        # Check that structural elements are visible
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "footer")))

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(self.driver.find_element(By.ID, "searchbar").is_displayed())
        self.assertTrue(self.driver.find_element(By.ID, "login_button").is_displayed())

        # Interact with key UI elements (e.g., click buttons)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.ID, "login_button"))).click()

        # Confirm that the UI reacts visually
        self.assertTrue(self.driver.find_element(By.XPATH, "//h1[text()='Login']").is_displayed())

    def test_required_elements_present(self):
        required_elements = [
            (By.TAG_NAME, "header"),
            (By.TAG_NAME, "footer"),
            (By.ID, "searchbar"),
            (By.ID, "login_button"),
            (By.XPATH, "//h1[text()='Login']"),
        ]

        for element in required_elements:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(element))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()