from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_page_structure(self):
        # Wait for the header to be visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//header")))
        
        # Check that structural elements (e.g., header, footer, navigation) are visible
        self.assertTrue(self.driver.find_element(By.XPATH, "//header").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//footer").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//nav").is_displayed())

        # Check the presence and visibility of input fields, buttons, labels, and sections
        self.assertTrue(self.driver.find_element(By.XPATH, "//input[@name='search']").is_enabled() and self.driver.find_element(By.XPATH, "//input[@name='search']").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//button[text()='Login']").is_enabled() and self.driver.find_element(By.XPATH, "//button[text()='Login']").is_displayed())

    def test_interact_with_ui_elements(self):
        # Interact with key UI elements (e.g., click buttons)
        self.driver.find_element(By.XPATH, "//button[text()='Login']").click()

        # Confirm that the UI reacts visually
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='alert alert-success']")))

    def test_assert_no_required_ui_elements_missing(self):
        # Assert that no required UI element is missing
        self.assertTrue(self.driver.find_element(By.XPATH, "//header").is_displayed())
        self.assertTrue(self.driver.find_element(By.XPATH, "//nav").is_displayed())

if __name__ == "__main__":
    unittest.main()