import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_max_website(self):
        driver = self.driver
        driver.get("http://max/")

        # Wait for main UI components to be visible
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#header"))
        )
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#footer"))
        )

        # Check presence and visibility of input fields, buttons, labels, and sections
        self.assertEqual(self.driver.find_elements(By.CSS_SELECTOR, "#header nav li").__len__, 3)
        self.assertTrue(EC.element_to_be_clickable((By.CSS_SELECTOR, "#header nav li:first-child a")).click())
        self.assertTrue(EC.element_to_be_clickable((By.CSS_SELECTOR, "#search-field")).is_enabled())

        # Interact with key UI elements
        driver.find_element(By.CSS_SELECTOR, "#login-link").click()
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#login-form"))
        )

        # Confirm that the UI reacts visually
        self.assertTrue(EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-button")).is_enabled())
        driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()