from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
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
        self.driver.get("data:text/html;charset=utf-8," + html_data['html'])

    def test_main_ui_components(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header not found or not visible")

        # Check that logo is present
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'logo-image')))
        except:
            self.fail("Logo not found or not visible")
        
        # Check for search input
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except:
            self.fail("Search input not found or not visible")

        # Check for cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        except:
            self.fail("Cart button not found or not visible")

        # Check navigation links
        categories = ['Category A', 'Category B', 'Category C']
        for category in categories:
            try:
                category_link = wait.until(
                    EC.visibility_of_element_located((By.LINK_TEXT, category))
                )
            except:
                self.fail(f"Link for {category} not found or not visible")

        # Check for footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()