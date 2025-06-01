import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class TestArtWebsite(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver with ChromeDriver using webdriver-manager
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        # Navigate to the home page
        self.driver.get("http://localhost:8080/en/")

    def test_interface_elements(self):
        # Verify that navigation links exist and are visible
        nav_links = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "#header > div > ul > li"))
        )
        self.assertGreaterEqual(len(nav_links), 5)

        # Verify that inputs, buttons, and banners exist and are visible
        input_field = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "email")))
        submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".home-slider > .slick-track")))

    def test_interactive_elements(self):
        # Click the submit button
        submit_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[@type='submit']")))
        submit_button.click()

        # Verify that the UI updates visually after clicking the button
        self.assertTrue(WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "success"))))

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()