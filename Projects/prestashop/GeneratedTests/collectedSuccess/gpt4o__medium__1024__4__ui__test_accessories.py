import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccessoriesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_accessories_page_ui_elements(self):
        driver = self.driver

        # Verify the presence of main UI components
        try:
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "header")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "footer")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.ID, "category-description")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.NAME, "s")))  # Search input
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'en/3-clothes')]")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'en/9-art')]")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'en/login')]")))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//a[contains(@href,'en/registration')]")))

            # Interact with the search input
            search_box = driver.find_element(By.NAME, "s")
            search_box.send_keys("Mug")
            search_box.submit()

            # Wait for the search results to load
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Search results')]")))

        except Exception as e:
            self.fail(f"Test failed due to missing elements: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()