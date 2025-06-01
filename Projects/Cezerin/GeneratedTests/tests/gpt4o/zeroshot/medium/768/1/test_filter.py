import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

class ProductFilterTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        self.driver.get("http://localhost:3000/category-a")

    def tearDown(self):
        self.driver.quit()

    def test_brand_a_filter(self):
        driver = self.driver

        # Verify the page loads with product cards
        product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a")
        if not product_cards or len(product_cards) == 0:
            self.fail("No product cards found on initial page load.")
        original_count = len(product_cards)

        # Locate and apply the "Brand A" checkbox filter
        brand_a_checkbox = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Brand A')]/input"))
        )
        brand_a_checkbox.click()

        # Wait for the UI to update
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a"))
        )
        
        # Verify the product count changes
        product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a")
        self.assertNotEqual(len(product_cards), original_count, "Product count did not change after applying 'Brand A' filter.")

        # Uncheck the "Brand A" filter
        brand_a_checkbox.click()

        # Verify the product count restores
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a"))
        )
        product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a")
        self.assertEqual(len(product_cards), original_count, "Product count did not restore after removing 'Brand A' filter.")

    def test_price_filter(self):
        driver = self.driver

        # Verify the page loads with product cards
        product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a")
        if not product_cards or len(product_cards) == 0:
            self.fail("No product cards found on initial page load.")
        original_count = len(product_cards)

        # Locate the price slider component
        price_slider = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//div[@class='price-filter']"))
        )
        self.assertIsNotNone(price_slider, "Price slider not found.")

        # Move one of the slider handles to change the price range
        slider = driver.find_element(By.XPATH, "//div[@class='price-filter']")
        action = ActionChains(driver)
        action.click_and_hold(slider).move_by_offset(-20, 0).release().perform()

        # Verify the product count changes after adjusting the price slider
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a"))
        )
        product_cards = driver.find_elements(By.XPATH, "//div[@class='column is-6-mobile is-4-tablet is-3-desktop is-3-widescreen is-3-fullhd available']/a")
        self.assertNotEqual(len(product_cards), original_count, "Product count did not change after adjusting price filter.")

if __name__ == "__main__":
    unittest.main()