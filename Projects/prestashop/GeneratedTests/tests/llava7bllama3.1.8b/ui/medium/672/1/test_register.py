import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestPageElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_page_elements(self):
        # Confirm the presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "nav > ul > li"))
        )
        self.assertGreater(len(navigation_links), 0)

        login_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, "Login"))
        )
        self.assertIsNotNone(login_link)

        # Interact with one or two elements
        register_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        register_button.click()

        # Verify that interactive elements do not cause errors in the UI
        banners = self.driver.find_elements(By.XPATH, "//div[@class='banner']")
        self.assertGreater(len(banners), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()