import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://max/search")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check header links
            register_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Register")))
            login_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Log in")))
            wishlist_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Wishlist")))
            cart_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Shopping cart")))

            # Check search box
            search_input = wait.until(EC.visibility_of_element_located((By.ID, "small-searchterms")))
            search_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "search-box-button")))

            # Check menu items
            home_page_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home page")))
            new_products_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "New products")))
            search_page_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Search")))
            my_account_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "My account")))
            contact_us_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Contact us")))

            # Interact with search button
            search_input.send_keys("book")
            search_button.click()
            wait.until(EC.url_contains("search?q=book"))

            # Verify product is loaded
            product_item = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-item")))
            self.assertTrue(product_item.is_displayed())
            
        except Exception as e:
            self.fail(f"UI element verification failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()