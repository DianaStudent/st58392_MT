import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Check presence of navigation links
        try:
            home_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/']")))
            clothes_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/3-clothes']")))
            accessories_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/6-accessories']")))
            art_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/9-art']")))
        except:
            self.fail("Navigation links not found or are not visible.")

        # Check presence of login link
        try:
            login_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F9-art']")))
        except:
            self.fail("Login link not found or is not visible.")

        # Check presence of registration link
        try:
            register_link = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[href='http://localhost:8080/en/registration']")))
        except:
            self.fail("Registration link not found or is not visible.")

        # Check presence of search input
        try:
            search_input = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='s']")))
        except:
            self.fail("Search input not found or is not visible.")

        # Check presence of banner
        try:
            banner = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.banner")))
        except:
            self.fail("Banner not found or is not visible.")

        # Interact with element: click on the 'Art' menu link
        try:
            art_link.click()
            WebDriverWait(driver, 20).until(EC.url_contains("9-art"))
        except:
            self.fail("Failed to click on Art link or page did not load correctly.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()