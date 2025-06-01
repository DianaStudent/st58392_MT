import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.actions import Actions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestArtCategory(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_art_category_filter(self):
        self.driver.get("http://localhost:8080")

        # Click on the "Art" category in the top menu
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@data-name='Art']"))).click()

        # Wait for the category page to load
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".section-header")))

        # Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_filter = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//label[text()='Composition']/preceding-sibling::input[@type='checkbox']")))
        composition_filter.click()

        # Wait for the filter to apply
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".filter-applied")))

        # Assert that the number of product tiles is reduced from 7 to 3
        original_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']"))
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']")), 3)

        # Locate and click the "Clear all" button to remove filters
        clear_all_button = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@data-name='Clear all']")))
        clear_all_button.click()

        # Wait for the filter to be cleared
        self.driver.implicitly_wait(10)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".filter-applied")))

        # Assert that the number of products returns to the original count - 7
        new_count = len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']"))
        self.assertEqual(new_count, original_count)


if __name__ == '__main__':
    unittest.main()