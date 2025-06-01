import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from webdriver_manager.chrome import ChromeDriverManager

class ClothesPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header logo
        try:
            logo = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".logo")))
        except Exception:
            self.fail("Logo is not visible on the page")

        # Check Contact us link
        try:
            contact_us = wait.until(visibility_of_element_located((By.CSS_SELECTOR, "#contact-link a")))
        except Exception:
            self.fail("Contact us link is not visible on the page")

        # Check Language selector
        try:
            language_selector = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".language-selector")))
        except Exception:
            self.fail("Language selector is not visible on the page")

        # Check Sign in link
        try:
            sign_in = wait.until(visibility_of_element_located((By.CSS_SELECTOR, "a[title='Log in to your customer account']")))
        except Exception:
            self.fail("Sign in link is not visible on the page")

        # Check Cart
        try:
            cart = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".shopping-cart")))
        except Exception:
            self.fail("Cart is not visible on the page")

        # Check breadcrumb navigation
        try:
            breadcrumb = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".breadcrumb")))
        except Exception:
            self.fail("Breadcrumb is not visible on the page")

        # Check main category title
        try:
            category_title = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".block-category h1")))
        except Exception:
            self.fail("Category title is not visible on the page")

        # Check subcategory images
        try:
            subcategory_images = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".subcategory-image")))
        except Exception:
            self.fail("Subcategory images are not visible on the page")

        # Check product list
        try:
            product_list = wait.until(visibility_of_element_located((By.CSS_SELECTOR, ".products")))
        except Exception:
            self.fail("Product list is not visible on the page")

        # Check footer
        try:
            footer = wait.until(visibility_of_element_located((By.ID, "footer")))
        except Exception:
            self.fail("Footer is not visible on the page") 

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()