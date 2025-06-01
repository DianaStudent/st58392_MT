import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_home_page(self):
        # Open the page
        self.driver.get('https://example.com')  # Replace with your website URL

        # Confirm the presence of key interface elements
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[@class='main-nav']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "header")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-input")))

        # Interact with one or two elements
        button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='btn-primary']")))
        button.click()

        # Verify that interactive elements do not cause errors in the UI
        self.assertTrue(button.is_enabled())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()