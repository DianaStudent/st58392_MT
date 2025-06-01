import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.base_url = "http://max/"

    def test_home_page_elements(self):
        driver = self.driver
        driver.get(self.base_url)

        try:
            # Check key elements are present and visible
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-register")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-login")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.ico-cart")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-box-text")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img.slider-img")))

            # Interact with the search box and perform search
            search_box = driver.find_element(By.ID, "small-searchterms")
            search_box.send_keys("test")
            search_button = driver.find_element(By.CSS_SELECTOR, "button.button-1.search-box-button")
            search_button.click()

            # Wait for the search page to load
            WebDriverWait(driver, 20).until(EC.url_contains("search?q=test"))

            # Verify no UI errors present
            self.assertTrue("No results were found" not in driver.page_source)

        except Exception as e:
            self.fail(f"Test failed due to exception: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()