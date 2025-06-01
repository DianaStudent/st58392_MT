import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIElements(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a-1")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        try:
            # Check the header/logo
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image > img[alt="logo"]')))
            self.assertTrue(logo.is_displayed(), "Logo is not visible")

            # Check the search bar
            search_input = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input.search-input')))
            self.assertTrue(search_input.is_displayed(), "Search input is not visible")

            # Check the cart button
            cart_button = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'span.cart-button > img[alt="cart"]')))
            self.assertTrue(cart_button.is_displayed(), "Cart button is not visible")

            # Check the navigation links
            category_a_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]')))
            self.assertTrue(category_a_link.is_displayed(), "Category A link is not visible")

            subcategory_1_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a-1"].is-active')))
            self.assertTrue(subcategory_1_link.is_displayed(), "Subcategory 1 link is not visible")
            
            # Check the breadcrumb navigation
            breadcrumb = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav.breadcrumb[aria-label="breadcrumbs"]')))
            self.assertTrue(breadcrumb.is_displayed(), "Breadcrumb navigation is not visible")

            # Check the footer
            footer_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.footer-logo > img[alt="logo"]')))
            self.assertTrue(footer_logo.is_displayed(), "Footer logo is not visible")

        except Exception as e:
            self.fail(f"Test failed due to missing element: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()