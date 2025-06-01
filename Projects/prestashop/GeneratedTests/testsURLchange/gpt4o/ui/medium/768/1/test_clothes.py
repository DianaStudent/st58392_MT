from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class TestClothingPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_elements(self):
        driver = self.driver

        # Check presence of navigation links
        home_link = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
        clothes_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")
        accessories_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/6-accessories']")
        art_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")

        # Check presence of login link
        login_link = driver.find_element(By.XPATH, "//a[@href='http://localhost:8080/en/login?back=http%3A%2F%2Flocalhost%3A8080%2Fen%2F3-clothes']")

        # Check presence of search input
        search_input = driver.find_element(By.XPATH, "//input[@type='text'][@name='s']")

        # Check presence of filters
        filter_title = driver.find_element(By.XPATH, "//p[contains(text(), 'Filter By')]")

        # Interact with the elements
        home_link.click()
        current_url = driver.current_url
        self.assertEqual(current_url, "http://localhost:8080/en/")

        # Go back to clothes page
        driver.get("http://localhost:8080/en/3-clothes")
        
        # Interact with the search bar
        search_input.send_keys("shirt")
        search_input.submit()

        # Verify that UI updates: Checking if no errors occur by waiting for the search result header
        try:
            search_result = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//p[contains(text(), 'Showing 1-')]")))
        except:
            self.fail("Search result not visible indicating possible error in UI update.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()