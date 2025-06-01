from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from webdriver_manager.chrome import ChromeDriverManager

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_apply_filters(self):
        driver = self.driver

        # Wait until products and filters are fully loaded
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'products')))
        
        # Locate "Brand A" checkbox filter and click
        brand_a_checkbox = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//label[input[@type='checkbox'] and contains(text(), 'Brand A')]")
        ))
        brand_a_checkbox.click()

        # Confirm it is checked
        input_element = brand_a_checkbox.find_element(By.XPATH, "./input[@type='checkbox']")
        self.assertTrue(input_element.is_selected())

        # Wait 2 seconds
        driver.implicitly_wait(2)

        # Verify product card count is reduced
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        initial_count = len(product_cards)
        self.assertEqual(initial_count, 1, "Expected product card count to be 1")

        # Uncheck "Brand A" filter
        brand_a_checkbox.click()
        driver.implicitly_wait(2)

        # Verify product card count increased
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        restored_count = len(product_cards)
        self.assertEqual(restored_count, 2, "Expected product card count to be 2")

        # Locate price slider and adjust
        slider = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//div[@class='price-filter']/input")
        ))
        actions = ActionChains(driver)
        actions.click_and_hold(slider).move_by_offset(-30, 0).release().perform()

        # Allow for the slider to move
        driver.implicitly_wait(2)

        # Verify product card count is reduced
        product_cards = driver.find_elements(By.CSS_SELECTOR, ".products .available")
        reduced_count = len(product_cards)
        self.assertEqual(reduced_count, 1, "Expected product card count to be 1 after price filtering")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()