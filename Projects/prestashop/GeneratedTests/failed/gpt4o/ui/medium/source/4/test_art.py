from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class ArtPageTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/9-art")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        
        # Verify presence of the header logo
        try:
            logo = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#_desktop_logo img")))
        except:
            self.fail("Logo is not present or visible.")

        # Verify presence of navigation links
        try:
            home_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/en/"]')))
            clothes_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/en/3-clothes"]')))
            accessories_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/en/6-accessories"]')))
            art_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/en/9-art"]')))
            login_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href^="/en/login"]')))
            register_link = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/en/registration"]')))
        except:
            self.fail("One or more navigation links are not present or visible.")

        # Verify presence of the search input
        try:
            search_input = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#search_widget input[name="s"]')))
        except:
            self.fail("Search input is not present or visible.")

        # Verify presence of the main banner
        try:
            banner = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.category-cover img')))
        except:
            self.fail("Main banner is not present or visible.")

        # Verify presence of a product and interact with it
        try:
            first_product = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.js-product')))
            quick_view_button = first_product.find_element(By.CSS_SELECTOR, '.quick-view')
            quick_view_button.click()

            # Wait for the quick view or another UI update action
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.modal-content')))
        except:
            self.fail("Product quick view interaction failed or did not result in UI update.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()