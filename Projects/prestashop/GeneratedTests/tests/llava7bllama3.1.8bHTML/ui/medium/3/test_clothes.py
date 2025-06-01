import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_home_page_elements(self):
        # Navigation links
        navigation_links = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".nav-list > li")))
        self.assertGreater(len(navigation_links), 1)

        # Inputs
        inputs = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "input")))
        self.assertGreater(len(inputs), 2)

        # Buttons
        buttons = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.TAG_NAME, "button")))
        self.assertGreater(len(buttons), 1)

        # Banners
        banners = WebDriverWait(self.driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".banner")))
        self.assertGreater(len(banners), 0)

    def test_interactive_element(self):
        # Click a button and check that the UI updates visually
        buttons = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".success-message")))

    def test_no_errors_on_interaction(self):
        # Verify that interactive elements do not cause errors in the UI
        buttons = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        self.assertEqual(len(self.driver.find_elements(By.CSS_SELECTOR, ".error-message")), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()