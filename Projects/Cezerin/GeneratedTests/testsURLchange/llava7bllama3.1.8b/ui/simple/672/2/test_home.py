import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestEcommercePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000")

    def test_main_ui_components(self):
        # Header Section
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "header")))
        self.assertEqual(header.is_displayed(), True)
        
        logo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//a[@class='logo']")))
        self.assertEqual(logo.is_displayed(), True)

        search_bar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "search-bar")))
        self.assertEqual(search_bar.is_displayed(), True)

        # Main Content Area
        product_image = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@src='slide8.jpg']")))
        self.assertEqual(product_image.is_displayed(), True)
        
        new_arrival_tag = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='new-arrival-tag']")))
        self.assertEqual(new_arrival_tag.is_displayed(), True)

        related_products_area = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='related-products-area']")))
        self.assertEqual(related_products_area.is_displayed(), True)
        
        # Product Information Section
        product_info_section = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='product-info-section']")))
        self.assertEqual(product_info_section.is_displayed(), True)

        # Footer Section
        footer = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.ID, "footer")))
        self.assertEqual(footer.is_displayed(), True)
        
        social_media_links = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//a[@class='social-media-link']")))
        for link in social_media_links:
            self.assertEqual(link.is_displayed(), True)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()