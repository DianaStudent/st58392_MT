import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAccessoriesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/6-accessories")

    def tearDown(self):
        self.driver.quit()

    def test_check_ui_elements(self):
        driver = self.driver

        # Wait utility function
        def wait_for_element(by, selector):
            try:
                WebDriverWait(driver, 20).until(EC.visibility_of_element_located((by, selector)))
            except:
                self.fail(f"Element with selector {selector} not found or not visible.")

        # Check header presence
        wait_for_element(By.ID, "header")

        # Check for main navigation links
        wait_for_element(By.LINK_TEXT, "Clothes")
        wait_for_element(By.LINK_TEXT, "Accessories")
        wait_for_element(By.LINK_TEXT, "Art")

        # Check for language selector
        wait_for_element(By.CLASS_NAME, "language-selector")

        # Check for sign in link
        wait_for_element(By.LINK_TEXT, "Sign in")

        # Check for cart link
        wait_for_element(By.CSS_SELECTOR, ".shopping-cart")

        # Check for breadcrumb
        wait_for_element(By.CLASS_NAME, "breadcrumb")

        # Check for product list
        wait_for_element(By.ID, "js-product-list")

        # Check for product quick-view buttons
        quick_view_buttons = driver.find_elements(By.CLASS_NAME, "quick-view")
        self.assertTrue(any(btn.is_displayed() for btn in quick_view_buttons), "Quick view buttons are not visible.")

        # Check for sort by dropdown
        wait_for_element(By.CLASS_NAME, "products-sort-order")

        # Check for footer
        wait_for_element(By.ID, "footer")

if __name__ == '__main__':
    unittest.main()