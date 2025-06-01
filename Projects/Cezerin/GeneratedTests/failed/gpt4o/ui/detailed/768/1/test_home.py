from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        # Set up the WebDriver
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not visible")

        # Check footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer is not visible")

        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        except:
            self.fail("Logo is not visible")

        # Check search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-input')))
        except:
            self.fail("Search input is not visible")

        # Check category links
        try:
            category_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav a')))
        except:
            self.fail("Category links are not visible")

        # Check best sellers section
        try:
            best_sellers = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.title.is-4')))
        except:
            self.fail("Best sellers section is not visible")

        # Interact with UI elements
        try:
            category_a_link = driver.find_element(By.LINK_TEXT, 'Category A')
            category_a_link.click()
            wait.until(EC.url_contains("category-a"))
        except:
            self.fail("Cannot navigate to Category A")

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()