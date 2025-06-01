from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomepageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_homepage_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check header visibility
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header is not visible.")

        # Check navigation links
        nav_links = ['Category A', 'Category B', 'Category C']
        for link_text in nav_links:
            nav_element = wait.until(EC.visibility_of_element_located((By.LINK_TEXT, link_text)))
            self.assertTrue(nav_element.is_displayed(), f"Navigation link {link_text} is not visible.")

        # Check main image slider
        slider_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.image-gallery-image img')))
        self.assertTrue(slider_image.is_displayed(), "Slider image is not visible.")

        # Check search box
        search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_box.is_displayed(), "Search box is not visible.")
        
        # Check best sellers section
        best_sellers_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'title')))
        self.assertTrue(best_sellers_title.is_displayed(), "Best sellers title is not visible.")

        # Check product links and prices
        products = driver.find_elements(By.CLASS_NAME, 'content')
        self.assertGreater(len(products), 0, "No products found on the page.")
        for product in products:
            product_name = product.find_element(By.CLASS_NAME, 'product-name')
            product_price = product.find_element(By.CLASS_NAME, 'product-price')
            self.assertTrue(product_name.is_displayed(), "Product name is not visible.")
            self.assertTrue(product_price.is_displayed(), "Product price is not visible.")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer is not visible.")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()