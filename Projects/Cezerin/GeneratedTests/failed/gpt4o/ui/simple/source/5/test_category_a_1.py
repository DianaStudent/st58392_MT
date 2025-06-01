from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestCategoryPage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")

    def test_UI_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "a.logo-image")))
        except:
            self.fail("Logo is not visible")

        # Verify breadcrumb navigation
        try:
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "nav.breadcrumb")))
        except:
            self.fail("Breadcrumb navigation is not visible")

        # Verify category title
        try:
            category_title = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "h1.category-title")))
            self.assertEqual(category_title.text, "Subcategory 1")
        except:
            self.fail("Category title is not visible or incorrect")

        # Verify search box field
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input.search-input")))
        except:
            self.fail("Search box is not visible")

        # Verify cart button
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.cart-button")))
        except:
            self.fail("Cart button is not visible")

        # Verify footer
        try:
            footer = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "section.section-footer")))
        except:
            self.fail("Footer is not visible")

        # Verify category links
        categories = ["Category A", "Category B", "Category C"]
        for category in categories:
            try:
                category_link = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, category)))
            except:
                self.fail(f"{category} link is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()