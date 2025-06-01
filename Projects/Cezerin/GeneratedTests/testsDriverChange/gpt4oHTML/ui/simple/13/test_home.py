import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestUIComponents(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("data:text/html;charset=utf-8," + html_data["html"])

    def test_ui_elements(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Check for the header presence
        try:
            header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        except:
            self.fail("Header is not visible")

        # Check for the category link for 'Category A'
        try:
            category_a_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a']")))
        except:
            self.fail("Link for 'Category A' is not visible")

        # Check for the category link for 'Subcategory 1'
        try:
            subcategory_1_link = wait.until(EC.visibility_of_element_located((By.XPATH, "//a[@href='/category-a-1']")))
        except:
            self.fail("Link for 'Subcategory 1' is not visible")

        # Check for search input presence
        try:
            search_input = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        except:
            self.fail("Search input is not visible")

        # Check for cart button presence
        try:
            cart_button = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'cart-button')))
        except:
            self.fail("Cart button is not visible")

        # Check for slider image presence
        try:
            slider_image = wait.until(EC.visibility_of_element_located((By.XPATH, "//img[@alt='THE FRESH FOAM CRUZ']")))
        except:
            self.fail("Slider image is not visible")

        # Check for 'BEST SELLERS' present
        try:
            best_sellers_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[contains(text(),'BEST SELLERS')]")))
        except:
            self.fail("'BEST SELLERS' title is not visible")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()