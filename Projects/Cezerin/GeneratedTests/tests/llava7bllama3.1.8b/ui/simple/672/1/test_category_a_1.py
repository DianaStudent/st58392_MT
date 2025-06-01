import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestSimpleUI(unittest.TestCase):

    def setUp(self):
        from webdriver_manager.chrome import ChromeDriverManager
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def tearDown(self):
        self.driver.quit()

    def test_ui_components(self):
        self.driver.get("http://localhost:3000")
        
        # Check Header Section exists and is visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//header")))
        self.assertIsNotNone(header)
        
        # Check Main Content Area exists and is visible
        main_content = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//main[@class='main-content']")))
        self.assertIsNotNone(main_content)
        
        # Check Footer Section exists and is visible
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//footer")))
        self.assertIsNotNone(footer)
        
        # Check Buttons exist and are visible
        subscribe_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='subscribe']")))
        self.assertIsNotNone(subscribe_button)
        get_started_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='get-started']")))
        self.assertIsNotNone(get_started_button)
        
    def test_category_a_ui_components(self):
        self.driver.get("http://localhost:3000/category-a")
        
        # Check Header Section exists and is visible
        header = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//header")))
        self.assertIsNotNone(header)
        
        # Check Main Content Area exists and is visible
        main_content = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//main[@class='main-content']")))
        self.assertIsNotNone(main_content)
        
        # Check Footer Section exists and is visible
        footer = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//footer")))
        self.assertIsNotNone(footer)
        
        # Check Buttons exist and are visible
        subscribe_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='subscribe']")))
        self.assertIsNotNone(subscribe_button)
        get_started_button = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='get-started']")))
        self.assertIsNotNone(get_started_button)

if __name__ == "__main__":
    unittest.main()