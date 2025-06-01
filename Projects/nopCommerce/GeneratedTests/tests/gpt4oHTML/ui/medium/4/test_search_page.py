import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class SearchPageUITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://max/search")

    def test_ui_elements_presence_and_interaction(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check presence of main navigation links
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page"))), "Home page link not visible.")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search"))), "Search link not visible.")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account"))), "My account link not visible.")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Blog"))), "Blog link not visible.")
        self.assertTrue(wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us"))), "Contact us link not visible.")

        # Check presence of the search input and button
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        self.assertTrue(search_box, "Search input not visible.")
        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        self.assertTrue(search_button, "Search button not visible.")

        # Interact with the search bar
        search_box.send_keys("book")
        search_button.click()

        # Verify the UI updates visually - e.g., check for product display
        product_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-title a")))
        self.assertTrue(product_title, "Product title not visible after search.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()