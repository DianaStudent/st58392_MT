from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class AccessoriesPageTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_present(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Verify navigation links
            home_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/']")))
            clothes_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/3-clothes']")))
            art_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='http://localhost:8080/en/9-art']")))

            # Verify page header
            header = wait.until(EC.visibility_of_element_located((By.XPATH, "//header[@id='header']")))

            # Verify main banner presence
            main_banner = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='header-banner']")))

            # Verify sign in button
            sign_in_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@title='Log in to your customer account']")))

            # Verify category description
            category_description = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='category-description']")))

            # Verify the search input field
            search_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@name='s']")))

            # Interact with a button and validate UI updates
            sign_in_button.click()
            wait.until(EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(), 'Login')]")))

        except Exception as e:
            self.fail(f"UI element is not present or not visible: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()