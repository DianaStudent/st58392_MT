import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestUIProcess(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("data:text/html," + "{html_data}")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check that the header is present and visible
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header should be visible.")

        # Check that the footer is present and visible
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer should be visible.")

        # Check that navigation elements are present and visible
        nav_links = driver.find_elements(By.CSS_SELECTOR, 'ul.nav-level-0 > li > div.cat-parent > a')
        self.assertTrue(all(link.is_displayed() for link in nav_links), "Navigation links should be visible")
        self.assertEqual(len(nav_links), 3, "There should be 3 main navigation links")

        # Check that input fields are present and visible
        search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_input.is_displayed(), "Search input should be visible.")

        # Check that buttons are present and visible
        cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        self.assertTrue(cart_button.is_displayed(), "Cart button should be visible.")

        # Check for Image Gallery and Bullets
        image_gallery = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'image-gallery')))
        self.assertTrue(image_gallery.is_displayed(), "Image gallery should be visible.")
        
        gallery_bullets = driver.find_elements(By.CSS_SELECTOR, '.image-gallery-bullet')
        self.assertTrue(all(bullet.is_displayed() for bullet in gallery_bullets), "All gallery bullets should be visible.")
        
        # Interact with UI Elements
        nav_links[0].click()  # Click on 'Category A'
        self.assertEqual(driver.current_url, '/category-a', "URL should change to the 'Category A' page.")

        subcategory_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a-1"]')))
        subcategory_link.click()  # Click on 'Subcategory 1'
        self.assertEqual(driver.current_url, '/category-a-1', "URL should change to the 'Subcategory 1' page.")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()