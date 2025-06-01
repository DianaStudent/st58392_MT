import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestMax(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/")

    def tearDown(self):
        self.driver.quit()

    def test_max_page_structure(self):
        # Check if header is present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "header"))
        )
        
        # Check if footer is present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "footer"))
        )
        
        # Check if navigation is present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav"))
        )

        # Check if input fields, buttons and labels are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#newsletter-subscribe-button"))
        )

    def test_max_page_interaction(self):
        # Click the newsletter subscribe button
        WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#newsletter-subscribe-button"))
        ).click()
        
        # Wait for a few seconds to see if UI reacts visually
        self.driver.implicitly_wait(5)

    def test_max_page_elements_are_not_missing(self):
        elements = ["header", "footer", "input", "button"]
        for element in elements:
            WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, element))
            )

if __name__ == "__main__":
    unittest.main()