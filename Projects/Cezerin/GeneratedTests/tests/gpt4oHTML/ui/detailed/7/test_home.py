import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class UITest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8,{0}".format(html_data["html"]))
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)  # Timeout of 20 seconds
    
    def test_ui_elements(self):
        driver = self.driver

        # 1. Load the page and ensure that structural elements (e.g., header, footer, navigation) are visible.
        header = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        footer = self.wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        navigation = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'primary-nav')))
        
        # 2. Check the presence and visibility of input fields, buttons, labels, and sections.
        search_input = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        search_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-icon-search')))
        cart_button = self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))

        # 3. Interact with key UI elements (e.g., click buttons).
        search_input.click()
        search_input.send_keys("test")
        search_button.click()

        # 4. Confirm that the UI reacts visually.
        search_value = search_input.get_attribute("value")
        self.assertEqual(search_value, "test")

        # 5. Assert that no required UI element is missing.
        # Check presence of elements on home category_a category_a_1
        logo = driver.find_element(By.CLASS_NAME, 'logo-image')
        primary_nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav a')
        subcategory_links = driver.find_elements(By.CSS_SELECTOR, '.nav-level-1 a')

        self.assertTrue(logo.is_displayed(), "Logo is not displayed.")
        self.assertGreater(len(primary_nav_links), 0, "Primary navigation links are missing.")
        self.assertGreater(len(subcategory_links), 0, "Subcategory links are missing.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()