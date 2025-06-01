import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestHomePage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get('http://localhost:3000')
        self.wait = WebDriverWait(self.driver, 20)

    def test_page_elements(self):
        driver = self.driver
        wait = self.wait

        # Check logo
        try:
            logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a.logo-image')))
        except:
            self.fail('Logo is not visible')

        # Check search box
        try:
            search_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.search-box .search-input')))
        except:
            self.fail('Search box is not visible')

        # Check header links
        try:
            category_a_link = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/category-a"]')))
        except:
            self.fail('Category A link is not visible')

        # Check image slider
        try:
            slider_image = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.image-gallery-slide a img')))
        except:
            self.fail('Slider image is not visible')

        # Check best sellers section
        try:
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.XPATH, '//div[text()="BEST SELLERS"]')))
        except:
            self.fail('BEST SELLERS title is not visible')

        # Check footer
        try:
            footer_logo = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.footer-logo img')))
        except:
            self.fail('Footer logo is not visible')

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()