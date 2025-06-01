from selenium.webdriver.support.expected_conditions import presence_of_element_located, element_to_be_clickable, text_to_be_present_in_element
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TestWebpage(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get("http://localhost:3000/category-a")  # replace with your webpage URL

    def test_filtering(self):
        wait = WebDriverWait(self.driver, 20)

        # Apply "Brand A" filter
        brand_a_checkbox = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[@class='attribute'][contains(text(), 'Brand A')]/input")))
        brand_a_checkbox.click()
        self.driver.implicitly_wait(2)  # wait 2 seconds for the filter to apply

        # Check if number of visible product cards has changed
        initial_product_count = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='column']/a"))))

        # Remove "Brand A" filter
        brand_a_checkbox.click()
        self.driver.implicitly_wait(2)  # wait 2 seconds for the filter to remove

        # Check if number of visible product cards has changed back
        final_product_count = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='column']/a"))))

        # Check success condition: Product count should change after applying and removing the filter
        self.assertNotEqual(initial_product_count, final_product_count)

    def test_price_slider(self):
        wait = WebDriverWait(self.driver, 20)
        initial_product_count = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='column']/a"))))

        # Change price filtering using interactive slider
        price_slider = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='range']")))
        price_slider.send_keys("1000")  # change this value to any valid price

        # Check if number of visible product cards has changed
        final_product_count = len(wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='column']/a"))))

        # Check success condition: Product count should change after changing the filter
        self.assertNotEqual(initial_product_count, final_product_count)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()