from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class TestArtFilter(unittest.TestCase):

    def setUp(self):
        # Setup the driver
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:8080/en/")  # Open the home page

    def test_filter_art_category(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Click on the "Art" category in the top menu
        art_category_link = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='dropdown-item' and contains(@href, '/en/9-art')]"))
        )
        art_category_link.click()

        # Wait for the category page to load
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//main[@id='category']"))
        )

        # Locate the filter section and apply "Matt paper" filter under "Composition"
        toggle_composition = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//section[@class='facet clearfix' and .//p[text()='Composition']]/div"))
        )
        toggle_composition.click()  # This might be required to ensure that the Composition section is expanded

        # Find and click the "Matt paper" checkbox
        matt_paper_checkbox = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//ul[@id='facet_57074']//label[.//span[text()='Matt paper']]//input[@type='checkbox']"))
        )
        matt_paper_checkbox.click()

        # Wait for the filter to apply and the number of products to reduce to 3
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'There are 3 products')]"))
        )
        
        # Assert that there are 3 product tiles
        product_tiles = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='js-product product']")
        self.assertEqual(len(product_tiles), 3, "Product count should reduce to 3 after filter applied.")

        # Locate and click the "Clear all" button to remove filters - assuming it's a reset of filters
        clear_filter_button = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-secondary ok']"))
        )
        clear_filter_button.click()

        # Wait and assert that the number of products returns to the original count - 7
        wait.until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'There are 7 products')]"))
        )
        
        # Assert that the number of product tiles is back to 7 
        product_tiles_after_clearing = driver.find_elements(By.XPATH, "//div[@id='js-product-list']//div[@class='js-product product']")
        self.assertEqual(len(product_tiles_after_clearing), 7, "Product count should return to 7 after clearing filters.")

    def tearDown(self):
        # Tear down the driver
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()