import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        self.driver.get("http://localhost:8080/en/6-accessories")

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check visibility of header components
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, "header")))
            self.assertIsNotNone(header, "Header is missing")

            header_nav = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "header-nav")))
            self.assertIsNotNone(header_nav, "Navigation bar is missing in header")
        except Exception as e:
            self.fail(f"Header components test failed: {e}")

        # Check visibility of main content elements
        try:
            main_section = wait.until(EC.visibility_of_element_located((By.ID, "main")))
            self.assertIsNotNone(main_section, "Main section is missing")

            category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".block-category h1")))
            self.assertIsNotNone(category_title, "Category title is missing")

            product_list = wait.until(EC.visibility_of_element_located((By.ID, "js-product-list")))
            self.assertIsNotNone(product_list, "Product list is missing")
        except Exception as e:
            self.fail(f"Main content elements test failed: {e}")

        # Check visibility of search input field
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#search_widget input[type='text']")))
            self.assertIsNotNone(search_input, "Search input field is missing")
        except Exception as e:
            self.fail(f"Search input field test failed: {e}")

        # Check visibility of footer components
        try:
            footer = wait.until(EC.visibility_of_element_located((By.ID, "footer")))
            self.assertIsNotNone(footer, "Footer is missing")

            newsletter = wait.until(EC.visibility_of_element_located((By.ID, "blockEmailSubscription_displayFooterBefore")))
            self.assertIsNotNone(newsletter, "Newsletter section is missing in footer")
        except Exception as e:
            self.fail(f"Footer components test failed: {e}")

        # Interact with UI elements
        try:
            sort_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".products-sort-order .btn-unstyle")))
            sort_button.click()

            # Verify UI reaction
            dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".dropdown-menu")))
            self.assertIsNotNone(dropdown, "Sort dropdown is not visible after clicking sort button")

        except Exception as e:
            self.fail(f"Interaction with key UI elements failed: {e}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()