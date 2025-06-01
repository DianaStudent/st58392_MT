import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.url = "http://max/search"
        self.driver.get(self.url)
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver

        # Verify header elements are visible
        for item in ['login', 'register', 'wishlist', 'cart']:
            try:
                self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, f"ico-{item}")))
            except TimeoutException:
                self.fail(f"{item.capitalize()} is not visible")

        # Verify search box is present and visible
        try:
            search_box = self.wait.until(EC.visibility_of_element_located((By.ID, 'small-searchterms')))
        except TimeoutException:
            self.fail("Search box is not visible")
        
        # Verify search button is present and visible
        try:
            search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-box-button')))
            search_button.click()
        except TimeoutException:
            self.fail("Search button is not visible")

        # Verify footer elements are visible
        for link_title in ['Sitemap', 'Shipping & returns', 'Privacy notice', 'Conditions of Use']:
            try:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_title)))
            except TimeoutException:
                self.fail(f"{link_title} link is not visible in the footer")
        
        # Verify product item elements are visible
        try:
            product_item = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'product-item')))
            ActionChains(driver).move_to_element(product_item).perform()
        except TimeoutException:
            self.fail("Product items are not visible")

        # Verify header menu items are visible
        for page in ['Home page', 'New products', 'Search', 'My account', 'Blog', 'Contact us']:
            try:
                self.wait.until(EC.visibility_of_element_located((By.LINK_TEXT, page)))
            except TimeoutException:
                self.fail(f"Header menu item '{page}' is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()