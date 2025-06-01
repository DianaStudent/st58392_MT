import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestClothesPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/3-clothes")

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Verify header is present
        try:
            header = wait.until(EC.visibility_of_element_located((By.ID, 'header')))
        except:
            self.fail("Header not found or not visible")

        # Verify main category 'Clothes' is visible
        try:
            clothes_category = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Clothes'))
            )
        except:
            self.fail("Main category 'Clothes' link is not visible")

        # Verify subcategory links 'Men' and 'Women' are visible
        try:
            men_subcategory = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Men'))
            )
            women_subcategory = wait.until(
                EC.visibility_of_element_located((By.LINK_TEXT, 'Women'))
            )
        except:
            self.fail("Subcategory links 'Men' or 'Women' are not visible")

        # Verify search bar is present
        try:
            search_bar = wait.until(
                EC.visibility_of_element_located((By.NAME, 's'))
            )
        except:
            self.fail("Search bar not found or not visible")

        # Verify cart link is visible
        try:
            cart = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'shopping-cart'))
            )
        except:
            self.fail("Cart link not visible")

        # Verify product elements are present and visible
        try:
            product_elements = wait.until(
                EC.visibility_of_element_located((By.CLASS_NAME, 'js-product'))
            )
        except:
            self.fail("Product elements not found or not visible")

        # Verify footer is present
        try:
            footer = wait.until(
                EC.visibility_of_element_located((By.ID, 'footer'))
            )
        except:
            self.fail("Footer not found or not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()