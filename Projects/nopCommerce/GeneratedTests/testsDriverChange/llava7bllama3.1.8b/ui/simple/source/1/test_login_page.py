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

    def test_login_page_elements(self):
        self.driver.get("http://max/login?returnUrl=%2F")

        # Wait for the main elements to be visible
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        wait.until(EC.presence_of_element_located((By.ID, "password")))

        # Check that all required elements exist and are visible
        self.assertEqual(self.driver.find_element(By.ID, "username").is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.ID, "password").is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.XPATH, "//button[@type='submit']").is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.LINK_TEXT, "Forgot Password").is_displayed(), True)

    def test_register_page_elements(self):
        self.driver.get("http://max/register?returnUrl=%2F")

        # Wait for the main elements to be visible
        wait = WebDriverWait(self.driver, 20)
        wait.until(EC.presence_of_element_located((By.ID, "username")))
        wait.until(EC.presence_of_element_located((By.ID, "email")))

        # Check that all required elements exist and are visible
        self.assertEqual(self.driver.find_element(By.ID, "username").is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.ID, "email").is_displayed(), True)
        self.assertEqual(self.driver.find_element(By.XPATH, "//button[@type='submit']").is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()