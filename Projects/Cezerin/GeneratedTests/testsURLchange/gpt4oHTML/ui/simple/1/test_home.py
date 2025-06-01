import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("data:text/html;charset=utf-8,{html_data}".format(html_data=html_data["html"]))
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header not found or not visible")

        # Check main navigation links
        try:
            category_a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        except:
            self.fail("Category A link not found or not visible")

        # Check specific subcategory link under Category A
        try:
            category_a_1_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']")))
        except:
            self.fail("Category A Subcategory 1 link not found or not visible")

        # Check the existence of search box and input
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.search-box > input.search-input')))
        except:
            self.fail("Search input not found or not visible")

        # Check buttons related to image gallery
        try:
            gallery_bullets = wait.until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, 'button.image-gallery-bullet')))
            if len(gallery_bullets) < 3:
                self.fail("Not all gallery navigation bullets are found or visible")
        except:
            self.fail("Gallery navigation bullets not found or not visible")

        # Check presence of a product section
        try:
            best_sellers_section = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(), 'BEST SELLERS')]")))
        except:
            self.fail("Best sellers section not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(argv=[''], exit=False)