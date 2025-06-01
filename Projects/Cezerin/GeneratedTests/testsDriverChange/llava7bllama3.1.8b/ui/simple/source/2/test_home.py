import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000")

    def test_main_ui_components(self):
        # Check that the main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='logo']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[@id='mainNav']")))

        # Check that navigation bar is present and visible
        nav_bar = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//nav[@id='mainNav']")))
        self.assertEqual(nav_bar.is_displayed(), True)

        # Check that search bar is present and visible
        search_bar = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Search']")))
        self.assertEqual(search_bar.is_displayed(), True)

        # Check that featured product image is present and visible
        featured_product_image = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//img[@class='featured-product-image']")))
        self.assertEqual(featured_product_image.is_displayed(), True)

        # Check that product card is present and visible
        product_card = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='product-card']")))
        self.assertEqual(product_card.is_displayed(), True)

    def test_category_a_ui_components(self):
        self.driver.get("http://localhost:3000/category-a")

        # Check that main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='logo']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[@id='mainNav']")))

        # Check that category A title is present and visible
        category_a_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='category-title']")))
        self.assertEqual(category_a_title.is_displayed(), True)

    def test_category_a_1_ui_components(self):
        self.driver.get("http://localhost:3000/category-a-1")

        # Check that main UI components are present
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='logo']")))
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//nav[@id='mainNav']")))

        # Check that category A-1 title is present and visible
        category_a_1_title = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//h1[@class='category-title']")))
        self.assertEqual(category_a_1_title.is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()