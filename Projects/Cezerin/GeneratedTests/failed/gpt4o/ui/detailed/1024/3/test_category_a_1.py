from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        try:
            # Check header is present and visible
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
            
            # Check footer is present and visible
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
            
            # Check navigation links in the header
            nav_links = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.primary-nav ul.nav-level-0 li')))
            self.assertTrue(len(nav_links) >= 3, "Not all navigation links are present.")

            # Check search input field is present and visible
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))

            # Check sort dropdown is present and visible
            sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))

            # Check the existence of the cart button
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))

            # Check the section title and breadcrumb
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'breadcrumb')))
            category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))

            # Interact with UI elements to confirm visual reaction
            cart_button.click()

            # Verify cart is empty message is displayed
            cart_empty_text = wait.until(EC.visibility_of_element_located((By.XPATH, "//p[text()='Your cart is empty']")))

        except Exception as e:
            self.fail(f"Required element is missing or interaction failed: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()