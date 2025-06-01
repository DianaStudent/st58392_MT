import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestProductFilter(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_apply_filter(self):
        driver = self.driver

        try:
            # Wait for the "Brand A" checkbox and click it
            brand_a_checkbox = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, "//label[input[@type='checkbox' and contains(.., 'Brand A')]]"))
            )
            brand_a_checkbox.click()

            # Wait and check that the product count changes to 1
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, ".products .product-caption")) == 1
            )

            # Uncheck the "Brand A" checkbox
            brand_a_checkbox.click()

            # Wait and check that the product count changes back to 2
            WebDriverWait(driver, 20).until(
                lambda d: len(d.find_elements(By.CSS_SELECTOR, ".products .product-caption")) == 2
            )

            # Use price slider: assuming some JavaScript-based interaction for this component
            # Adjust this to match the interaction mechanism for the slider
            # Note: Simplifying as the slider may require JS execution
            # Example:
            # driver.execute_script("document.querySelector('YOUR_SLIDER_SELECTOR').value = 'desired_value'") 
            # WebDriverWait to ensure the change is reflected

        except Exception as e:
            self.fail(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    unittest.main()