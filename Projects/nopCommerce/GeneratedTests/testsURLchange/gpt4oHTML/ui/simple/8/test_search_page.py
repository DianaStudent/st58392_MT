import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class NopCommerceTest(unittest.TestCase):

    def setUp(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.get("http://max/")
        self.driver.maximize_window()
    
    def test_ui_components(self):
        driver = self.driver
        
        try:
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "header")))
            self.assertTrue(driver.find_element(By.CLASS_NAME, "header").is_displayed(), "Header is not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "search-box")))
            self.assertTrue(driver.find_element(By.CLASS_NAME, "search-box").is_displayed(), "Search box is not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.search-box-button")))
            self.assertTrue(driver.find_element(By.CSS_SELECTOR, "button.search-box-button").is_displayed(), "Search button is not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "top-menu")))
            self.assertTrue(driver.find_element(By.CLASS_NAME, "top-menu").is_displayed(), "Top menu is not visible")

            WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME, "footer")))
            self.assertTrue(driver.find_element(By.CLASS_NAME, "footer").is_displayed(), "Footer is not visible")

        except Exception as e:
            self.fail(f"Test failed due to exception: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()