from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_max_website(self):
        # Navigate to the website
        self.driver.get("http://max/")

        # Check that the main UI components are present and visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header")))
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, "Login")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-query")))

        # Check that the login page link works
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        WebDriverWait(self.driver, 20).until(EC.url_contains("login"))
        self.assertEqual(self.driver.current_url, "http://max/login?returnUrl=%2F")

        # Check that the register page link works
        self.driver.get("http://max/register?returnUrl=%2F")
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "register-email")))

        # Check that the search form is present and visible
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.ID, "search-form")))
        self.assertEqual(self.driver.current_url, "http://max/search")

if __name__ == "__main__":
    unittest.main()