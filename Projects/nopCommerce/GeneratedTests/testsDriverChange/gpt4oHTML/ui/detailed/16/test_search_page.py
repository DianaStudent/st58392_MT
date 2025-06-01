import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestStoreUI(unittest.TestCase):

    def setUp(self):
        # Set up ChromeDriver using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.base_url = "http://max/"
        self.driver.get(self.base_url + "search")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # 1. Check for the presence of structural elements
        header = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header")))
        footer = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "footer")))
        navigation = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-menu")))

        # Assert that the main elements are visible
        self.assertTrue(header.is_displayed(), "Header is not visible")
        self.assertTrue(footer.is_displayed(), "Footer is not visible")
        self.assertTrue(navigation.is_displayed(), "Navigation is not visible")

        # 2. Check the presence and visibility of input fields, buttons, labels, and sections
        search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
        search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))
        price_filter_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "filter-title")))

        self.assertTrue(search_input.is_displayed(), "Search input field is not visible")
        self.assertTrue(search_button.is_displayed(), "Search button is not visible")
        self.assertTrue(price_filter_title.is_displayed(), "Price filter title is not visible")

        # 3. Interact with key UI elements
        search_input.clear()
        search_input.send_keys("book")
        search_button.click()

        # 4. Confirm that the UI reacts visually
        results = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-results")))
        self.assertTrue(results.is_displayed(), "Search results are not displayed")

        # 5. Assert the elements are visible
        product_titles = driver.find_elements(By.CLASS_NAME, "product-title")
        if not product_titles:
            self.fail("No product titles found in search results.")
        for title in product_titles:
            self.assertTrue(title.is_displayed(), "A product title is not visible")
        
        # Check cart and wishlist
        cart_quantity = driver.find_element(By.CLASS_NAME, "cart-qty")
        wishlist_quantity = driver.find_element(By.CLASS_NAME, "wishlist-qty")
        self.assertTrue(cart_quantity.is_displayed(), "Cart quantity is not visible")
        self.assertTrue(wishlist_quantity.is_displayed(), "Wishlist quantity is not visible")

    def tearDown(self):
        # Quit the browser window
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()