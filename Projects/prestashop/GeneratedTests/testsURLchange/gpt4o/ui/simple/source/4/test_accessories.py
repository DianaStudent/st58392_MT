import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestAccessoriesPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_ui_elements_present_and_visible(self):
        driver = self.driver

        # Define elements to check by their CSS selector
        elements_to_check = {
            'header': 'header#header',
            'language_selector': 'div.language-selector',
            'sign_in_link': 'a[title="Log in to your customer account"]',
            'cart_link': 'div#_desktop_cart a',
            'category_menu': 'div.menu',
            'search_widget': '#search_widget input[name="s"]',
            'breadcrumb': 'nav.breadcrumb',
            'main_category_title': 'div.block-category h1.h1',
            'subcategory_list': 'ul.subcategories-list',
            'product_list': 'div.products',
            'footer': 'footer#footer'
        }

        # Wait for elements to be present and visible
        for element_name, selector in elements_to_check.items():
            try:
                element = WebDriverWait(driver, 20).until(
                    EC.visibility_of_element_located((By.CSS_SELECTOR, selector))
                )
            except:
                self.fail(f"{element_name} not found or not visible on the page.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()