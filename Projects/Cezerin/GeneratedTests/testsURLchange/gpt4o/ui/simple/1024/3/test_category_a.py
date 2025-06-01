import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCategoryAPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_ui_elements_presence(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header elements
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "header .logo-image")))

            # Check category navigation
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category A")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category B")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Category C")))

            # Check subcategory navigation
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 1")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 2")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 3")))

            # Check search box
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".search-input")))

            # Check cart icon
            wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".cart-button")))

            # Check filter section
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='attribute-title' and text()='Brand']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='attribute-title' and text()='Size']")))
            wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='attribute-title' and text()='Price']")))

            # Check product listing
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product A")))
            wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Product B")))

            # Check footer elements
            wait.until(EC.visibility_of_element_located((By.XPATH, "//footer")))

        except Exception as e:
            self.fail(f"An expected element is missing or not visible: {e}")

if __name__ == '__main__':
    unittest.main()