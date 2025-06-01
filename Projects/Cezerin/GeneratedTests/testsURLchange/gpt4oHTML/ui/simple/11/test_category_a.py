import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryPageUI(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://example.com/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        driver = self.driver

        try:
            # Check header presence
            header = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "header"))
            )

            # Check navbar links
            category_a_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Category A"))
            )
            category_b_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Category B"))
            )
            category_c_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Category C"))
            )

            # Check category title
            category_title = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "category-title"))
            )

            # Check for subcategory links
            subcategory_1_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 1"))
            )
            subcategory_2_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 2"))
            )
            subcategory_3_link = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.LINK_TEXT, "Subcategory 3"))
            )

            # Check for search box
            search_box = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "search-input"))
            )

            # Check for products list
            products_list = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "product-caption"))
            )

            # Check for footer presence
            footer = WebDriverWait(driver, 20).until(
                EC.visibility_of_element_located((By.TAG_NAME, "footer"))
            )

        except Exception as e:
            self.fail(f"UI component test failed: {str(e)}")

if __name__ == "__main__":
    unittest.main()