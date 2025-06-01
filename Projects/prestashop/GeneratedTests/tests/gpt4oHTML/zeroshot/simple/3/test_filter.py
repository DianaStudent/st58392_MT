import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestFilterFunctionality(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get('http://localhost:8080/en/9-art')

    def tearDown(self):
        self.driver.quit()

    def test_filter_composition_matt_paper(self):
        driver = self.driver
        wait = WebDriverWait(driver, 20)

        # Wait for the filter sidebar to be present
        try:
            filter_sidebar = wait.until(
                EC.presence_of_element_located((By.ID, 'search_filters'))
            )
        except Exception as e:
            self.fail('Filter sidebar not present')

        # Select the 'Composition - Matt paper' filter by its label text
        try:
            composition_label = filter_sidebar.find_element(By.XPATH, "//section[contains(., 'Composition')]//label[contains(., 'Matt paper')]")
            composition_checkbox = composition_label.find_element(By.TAG_NAME, "input")
            driver.execute_script("arguments[0].click();", composition_checkbox)
        except Exception as e:
            self.fail('Could not find or click the Matt paper filter checkbox: ' + str(e))

        # Verify that the number of visible product items changes
        initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, ".js-product")) != initial_product_count
        )
        filtered_count = len(driver.find_elements(By.CSS_SELECTOR, ".js-product"))

        self.assertNotEqual(initial_product_count, filtered_count, "Product count did not change after applying filter")

        # Clear the 'Composition - Matt paper' filter by clicking the checkbox again
        try:
            driver.execute_script("arguments[0].click();", composition_checkbox)
        except Exception as e:
            self.fail('Could not unselect the Matt paper filter checkbox: ' + str(e))

        # Verify that the number of visible product items reverts back
        WebDriverWait(driver, 10).until(
            lambda d: len(d.find_elements(By.CSS_SELECTOR, ".js-product")) == initial_product_count
        )

if __name__ == "__main__":
    unittest.main()