import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestMainUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_main_ui_components(self):
        # Navigate to the home page
        self.driver.get('http://localhost:8080/en/')

        # Check that all required UI components are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//h1[@class='page-title']"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='nav nav-pills']"))
        )

        # Check that all links are present and visible
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            self.assertTrue(link.is_displayed())

        # Check that the login and register links are correct
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Login"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Register"))
        )

        # Check that the main buttons are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-default']"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-success']"))
        )

    def test_category_links(self):
        # Navigate to the clothes page
        self.driver.get('http://localhost:8080/en/3-clothes')

        # Check that all category links are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//ul[@class='nav nav-pills']"))
        )
        links = self.driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            self.assertTrue(link.is_displayed())

    def test_login_page(self):
        # Navigate to the login page
        self.driver.get('http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art')

        # Check that all form fields and buttons are present and visible
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password']"))
        )
        WebDriverWait(self.driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='btn btn-default']"))
        )

if __name__ == '__main__':
    unittest.main()