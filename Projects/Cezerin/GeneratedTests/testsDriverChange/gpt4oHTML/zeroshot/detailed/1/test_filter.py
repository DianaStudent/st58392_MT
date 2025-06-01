import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.chrome.service import Service as ChromeService

class FilterTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a") # The URL should be replaced with the actual category page URL
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_filter_process(self):
        driver = self.driver
        wait = self.wait

        # Step 2: Wait until products and filters are fully loaded
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "section.section-category")))

        # Step 3: Locate and apply the "Brand A" checkbox filter using its associated input
        brand_a_checkbox = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'attribute')]/label[input[@type='checkbox' and following-sibling::text()='Brand A']]")))
        brand_a_checkbox.click()

        # Step 4: Confirm it is checked
        brand_a_checked = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'attribute')]/label[@class='attribute-checked']")))
        assert brand_a_checked is not None, self.fail("Brand A checkbox is not checked.")

        # Step 5: Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 → 1)
        time.sleep(2)
        products_after_filter = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div.available")
        initial_count = len(products_after_filter)
        if initial_count != 1:
            self.fail(f"Product count not reduced to 1 after applying Brand A filter. Current count: {initial_count}")

        # Step 6: Uncheck the filter and confirm product count is restored (e.g., 1 → 2)
        brand_a_checkbox.click()
        wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'attribute')]/label")))

        time.sleep(2)
        products_after_uncheck = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div.available")
        restored_count = len(products_after_uncheck)
        if restored_count != 2:
            self.fail(f"Product count not restored to 2 after unchecking Brand A filter. Current count: {restored_count}")

        # Step 7: Locate the price range slider and adjust it
        price_filter = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.price-filter")))
        slider_handle = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "YOUR_PRICE_SLIDER_HANDLE_SELECTOR")))
        
        actions = ActionChains(driver)
        actions.click_and_hold(slider_handle).move_by_offset(-50, 0).release().perform()

        # Step 9: Wait 2 seconds and verify that the number of product cards is reduced (e.g., 2 → 1)
        time.sleep(2)
        products_after_price_filter = driver.find_elements(By.CSS_SELECTOR, "div.columns.is-multiline.is-mobile.products > div.available")
        price_filtered_count = len(products_after_price_filter)
        if price_filtered_count != 1:
            self.fail(f"Product count not reduced to 1 after applying price filter. Current count: {price_filtered_count}")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()