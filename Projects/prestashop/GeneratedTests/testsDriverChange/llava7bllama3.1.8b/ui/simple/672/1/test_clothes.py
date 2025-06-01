import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

class TestECommerceWebsite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")

    def test_main_ui_components(self):
        # Check header exists and is visible
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='logo']")))
        self.assertIsNotNone(header)
        self.assertTrue(header.is_displayed())

        # Check navigation menu options exist and are clickable
        nav_menu_options = ["Home", "Shop", "About Us", "Contact Us"]
        for option in nav_menu_options:
            link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{option}']")))
            self.assertIsNotNone(link)
            self.assertTrue(link.is_displayed())
            link.click()

        # Check cart icon exists and is clickable
        cart_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//i[@class='cart-icon']")))
        self.assertIsNotNone(cart_icon)
        self.assertTrue(cart_icon.is_displayed())

        # Check product listing area exists
        products_grid = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='products-grid']")))
        self.assertIsNotNone(products_grid)
        self.assertTrue(products_grid.is_displayed())

        # Check banner advertising 'Mega Sale 20% Off' exists and is visible
        banner = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='banner']")))
        self.assertIsNotNone(banner)
        self.assertTrue(banner.is_displayed())

    def test_product_listing_area(self):
        # Check that products are displayed in a grid format
        products_grid = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='products-grid']")))
        self.assertIsNotNone(products_grid)
        self.assertTrue(products_grid.is_displayed())

    def test_footer_links_and_social_media_icons(self):
        # Check that links to 'Privacy', 'Terms', and 'Sitemap' exist and are clickable
        footer_links = ["Privacy", "Terms", "Sitemap"]
        for link in footer_links:
            footer_link = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//a[text()='{link}']")))
            self.assertIsNotNone(footer_link)
            self.assertTrue(footer_link.is_displayed())
            footer_link.click()

        # Check that social media icons (Instagram and Facebook) exist and are clickable
        social_media_icons = ["Instagram", "Facebook"]
        for icon in social_media_icons:
            icon_element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, f"//i[@class='{icon}-icon']")))
            self.assertIsNotNone(icon_element)
            self.assertTrue(icon_element.is_displayed())

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()