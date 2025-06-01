import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestSearchPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Header
        self.assertTrue(self.is_element_visible(By.CLASS_NAME, "header"), "Header is not visible")

        # Footer
        self.assertTrue(self.is_element_visible(By.CLASS_NAME, "footer"), "Footer is not visible")

        # Search Input
        self.assertTrue(self.is_element_visible(By.ID, "small-searchterms"), "Search input is not visible")

        # Search Button
        self.assertTrue(self.is_element_visible(By.CLASS_NAME, "search-box-button"), "Search button is not visible")

        # Product Grid
        self.assertTrue(self.is_element_visible(By.CLASS_NAME, "product-grid"), "Product grid is not visible")

        # Interactions
        search_input = driver.find_element(By.ID, "small-searchterms")
        search_input.send_keys("book")

        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Assert results
        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-grid")))
        self.assertTrue(self.is_element_visible(By.CLASS_NAME, "product-item"), "Products are not visible")

    def is_element_visible(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            return element.is_displayed()
        except:
            return False

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()