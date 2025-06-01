from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCategoryFilter(unittest.TestCase):

    def setUp(self):
        # Setup the ChromeDriver using WebDriver Manager
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")  # Replace with actual URL of the page
        self.wait = WebDriverWait(self.driver, 20)
    
    def tearDown(self):
        self.driver.quit()

    def test_filter_process(self):
        driver = self.driver
        wait = self.wait
        
        # Step 1: Ensure the category page is open by checking for the presence of 'Category A' link
        try:
            category_a_link = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@href='/category-a']")))
            self.assertTrue(category_a_link, "Category A link not found")
        except Exception as e:
            self.fail(f"Category A link not found: {str(e)}")
        
        # Step 2: Check the "Brand A" filter
        try:
            brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[input[@type='checkbox' and following-sibling::text()[contains(.,'Brand A')]]]")))
            brand_a_checkbox.click()
        except Exception as e:
            self.fail(f"Brand A checkbox not clickable: {str(e)}")

        # Wait for UI to update
        time.sleep(2)
        
        # Step 3: Verify the number of displayed products changes (assume initially 2 products)
        try:
            products = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
            self.assertEqual(len(products), 1, "The number of product cards did not change to 1 after filtering by Brand A")
        except Exception as e:
            self.fail(f"Product count after Brand A filter: {str(e)}")

        # Step 4: Uncheck the "Brand A" filter
        try:
            brand_a_checkbox.click()
            time.sleep(2)
        except Exception as e:
            self.fail(f"Unable to uncheck Brand A checkbox: {str(e)}")

        # Verify the original number of products is restored
        try:
            products = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
            self.assertEqual(len(products), 2, "The number of product cards did not restore to 2 after unchecking Brand A")
        except Exception as e:
            self.fail(f"Product count restoration failed: {str(e)}")

        # Step 5: Apply a price range filter using the slider
        try:
            price_range = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "price-filter-values")))
            handles = driver.find_elements(By.CSS_SELECTOR, "input[type='range']")
            if handles and len(handles) >= 1:
                action = ActionChains(driver)
                action.click_and_hold(handles[0]).move_by_offset(-10, 0).release().perform()
                time.sleep(2)
            else:
                self.fail("Price slider handles not found or interactable")
        except Exception as e:
            self.fail(f"Unable to move price slider: {str(e)}")
        
        # Step 6: Verify product count changes after applying price filter
        try:
            products_after_price_filter = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div")
            self.assertLess(len(products_after_price_filter), 2, "The number of product cards should reduce after price filter is applied")
        except Exception as e:
            self.fail(f"Product count after price filter: {str(e)}")

if __name__ == "__main__":
    unittest.main()