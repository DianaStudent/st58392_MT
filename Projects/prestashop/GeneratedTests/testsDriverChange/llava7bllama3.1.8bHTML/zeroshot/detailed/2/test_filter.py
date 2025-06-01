import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestFilter(unittest.TestCase):
    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")  # replace with your website URL

    def test_filter(self):
        # Click on the "Art" category in the top menu
        art_menu_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@data-name='art']"))
        )
        art_menu_button.click()

        # Wait for the category page to load
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//h1[@class='page-title']")))

        # Locate the filter section and apply the checkbox "Matt paper" under "Composition"
        composition_filter = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[@data-name='composition']/.."))
        )
        composition_filter.click()
        matt_paper_checkbox = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @data-name='matt-paper']"))
        )
        matt_paper_checkbox.click()

        # Wait for the filter to apply
        WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "(//div[@class='product-tile'])[3]")))

        # Assert that the number of product tiles is reduced from 7 to 3
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']")), 3)

        # Locate and click the "Clear all" button to remove filters
        clear_all_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-name='clear-all']"))
        )
        clear_all_button.click()

        # Wait and assert that the number of products returns to the original count - 7
        self.assertEqual(len(self.driver.find_elements(By.XPATH, "//div[@class='product-tile']")), 7)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()