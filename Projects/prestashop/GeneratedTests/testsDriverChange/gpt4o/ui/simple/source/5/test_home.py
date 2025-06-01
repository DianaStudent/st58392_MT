import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestDemoWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('http://localhost:8080/en/')

    def test_ui_elements(self):
        driver = self.driver

        try:
            # Check for header
            header = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
            
            # Check for main menu
            top_menu = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "_desktop_top_menu")))
            
            # Check for search widget
            search_widget = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "search_widget")))
            
            # Check for sign in link
            sign_in = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Sign in")))
            
            # Check for categories
            clothes_category = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/3-clothes']")))
            accessories_category = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/6-accessories']")))
            art_category = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a[href='/en/9-art']")))

            # Check for footer
            footer = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))

        except Exception as e:
            self.fail(f"UI element not found: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()