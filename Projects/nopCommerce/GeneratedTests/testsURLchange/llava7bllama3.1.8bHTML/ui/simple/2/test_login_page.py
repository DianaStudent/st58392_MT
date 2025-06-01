import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestMaxWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/")

    def test_ui_components(self):
        # Check that the header is present and visible
        header = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//header"))
        )
        self.assertEqual(header.is_displayed(), True)

        # Check that the search input field is present and visible
        search_input = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@name='search']"))
        )
        self.assertEqual(search_input.is_displayed(), True)

        # Check that the search button is present and visible
        search_button = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@type='submit']"))
        )
        self.assertEqual(search_button.is_displayed(), True)

        # Check that the login link is present and visible
        login_link = WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
        )
        self.assertEqual(login_link.is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()