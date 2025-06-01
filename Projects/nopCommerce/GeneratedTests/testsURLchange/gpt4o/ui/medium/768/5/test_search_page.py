import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestWebsiteUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://max/search")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements_present(self):
        driver = self.driver

        # Check for navigation links
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page"))))
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products"))))
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search"))))
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account"))))
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog"))))
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))))

        # Check for search input and button
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms"))))
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button"))))

        # Check for another UI element - for example, a product item
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item"))))

        # Interact with an element (search button) and ensure it functions without error
        search_box = driver.find_element(By.ID, "small-searchterms")
        search_box.send_keys("test")
        search_button = driver.find_element(By.CLASS_NAME, "search-box-button")
        search_button.click()

        # Verify page updates appropriately - example: waiting for search results
        self.assertTrue(self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-results"))))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()