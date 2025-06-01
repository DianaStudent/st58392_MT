from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class TestEcommerceWebsite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_main_ui_components(self):
        # Header elements
        header_logo = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@class='logo']")))
        self.assertEqual(header_logo.is_displayed(), True)

        navigation_menu_items = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='nav']//li/a")))
        self.assertGreater(len(navigation_menu_items), 3)

        # Main hero section elements
        hero_section_image = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//img[@class='hero-section-image']")))
        self.assertEqual(hero_section_image.is_displayed(), True)

        hero_section_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//button[(@data-icon='handbag' or @data-icon='home')]")))
        self.assertGreater(len(hero_section_buttons), 1)

        # Featured products section elements
        featured_products_section = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='featured-products-section']")))
        self.assertEqual(featured_products_section.is_displayed(), True)

        featured_product_cards = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='product-listing']//li//img")))
        self.assertGreater(len(featured_product_cards), 3)

        # Footer elements
        footer_section = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//footer[@class='site-footer']")))
        self.assertEqual(footer_section.is_displayed(), True)

        footer_buttons = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//button[(@data-icon='coupon' or @data-icon='home')]")))
        self.assertGreater(len(footer_buttons), 1)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()