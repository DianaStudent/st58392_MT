import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestECommerceSite(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_main_page_elements(self):
        # Verify presence of key interface elements
        navigation_links = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'nav > ul li'))
        )
        self.assertEqual(len(navigation_links), 5)

        headers = WebDriverWait(self.driver, 20).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'h1'))
        )
        self.assertEqual(len(headers), 4)

        # Verify presence of banners
        banner = WebDriverWait(self.driver, 20).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.banner'))
        )

        # Interact with one or two elements (e.g., click a button)
        product_link = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.LINK_TEXT, 'Clothes'))
        )
        product_link.click()

        self.assertEqual(self.driver.current_url, "http://localhost:8080/en/3-clothes")

    def test_interactive_elements(self):
        # Click a button and check that the UI updates visually
        cart_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'a.ico-cart'))
        )
        cart_button.click()

        self.assertEqual(self.driver.current_url, "http://localhost:8080/en/checkout")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()