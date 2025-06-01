import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestScenario(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def tearDown(self):
        self.driver.quit()

    def test_main_elements_present(self):
        # Check presence and visibility of header, footer, navigation
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
        self.assertTrue(header.is_displayed())
        
        # Check presence and visibility of buttons, links, form fields
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/login']")))

    def test_login_link_href(self):
        # Get the href attribute value of the login link
        login_link_href = self.driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/login']").get_attribute('href')
        
        # Compare it with the expected href value
        self.assertEqual(login_link_href, "http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art")

    def test_button_click(self):
        # Click on a button (example: login button)
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/login']")))
        login_button.click()
        
        # Confirm that the UI reacts visually
        self.assertTrue(login_button.is_enabled())

    def test_no_missing_elements(self):
        # Check that no required element is missing
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "header")))
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "footer")))
        login_button = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[@href='http://localhost:8080/en/login']")))

if __name__ == "__main__":
    unittest.main()