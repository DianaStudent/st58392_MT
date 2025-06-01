from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestMax(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_login_page_elements(self):
        # Open the login page
        self.driver.get("http://max/login?returnUrl=%2F")

        # Wait for 20 seconds to ensure elements are loaded
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1")))

        # Check presence of key interface elements
        self.assertIn("Login", self.driver.find_element(By.XPATH, "//h1").text)
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "input")), 2)  # Email and Password inputs
        self.assertEqual(len(self.driver.find_elements(By.TAG_NAME, "button")), 1)  # Login button

    def test_login_button_click(self):
        # Open the login page
        self.driver.get("http://max/login?returnUrl=%2F")

        # Wait for 20 seconds to ensure elements are loaded
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))

        # Click the login button
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

        # Wait for 10 seconds to ensure page has updated visually
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//p[@class='error-message']")))

        # Check that the error message is present
        self.assertIn("Invalid email or password", self.driver.find_element(By.XPATH, "//p[@class='error-message']").text)

if __name__ == "__main__":
    unittest.main()