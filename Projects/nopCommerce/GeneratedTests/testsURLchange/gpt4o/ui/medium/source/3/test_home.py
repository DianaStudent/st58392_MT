import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class HomePageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://max/")
        self.wait = WebDriverWait(self.driver, 20)
    
    def test_home_page_elements(self):
        driver = self.driver

        try:
            # Check header links
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-register")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "ico-login")))
            
            # Check search bar
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))

            # Check navigation menu
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))

            # Check swiper banner
            self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "swiper-slide")))

            # Interact with search bar
            search_box.send_keys("Test")
            search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
            search_button.click()

            # Check the presence of result or no error UI
            self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "master-wrapper-content")))

        except Exception as e:
            self.fail(f"UI elements are missing or interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()