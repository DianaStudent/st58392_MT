import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRegistrationPage(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/register?returnUrl=%2F")

    def test_registration_page_elements(self):
        # Check that the main UI components are present and visible
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='firstName']"))).is_displayed()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='lastName']"))).is_displayed()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='emailAddress']"))).is_displayed()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))).is_displayed()
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//button[text()='Sign Up']"))).is_enabled()
        except Exception as e:
            self.fail(f"Registration page elements are missing: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()