import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestCMS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://localhost:3000')

    def test_main_components(self):
        # Check that the main UI components are present: headers, buttons, links, form fields, etc.
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'nav#menu')))

            menu = self.driver.find_element(By.CSS_SELECTOR, 'nav#menu')
            self.assertTrue(menu.is_displayed(), "Menu is not displayed")

            logout_button = self.driver.find_element(By.LINK_TEXT, 'LOGOUT')
            self.assertTrue(logout_button.is_enabled(), "Logout button is not enabled")
        except Exception as e:
            self.fail(f"Failed to find main components: {str(e)}")

    def test_category_a_page(self):
        try:
            category_a_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CATEGORIES')))
            category_a_link.click()

            category_a_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.title')))
            self.assertTrue(category_a_title.is_displayed(), "Category A title is not displayed")

            categories_list = self.driver.find_elements(By.CSS_SELECTOR, '.category-list li')
            self.assertGreater(len(categories_list), 0, "Categories list is empty")
        except Exception as e:
            self.fail(f"Failed to navigate to category page: {str(e)}")

    def test_category_a_1_page(self):
        try:
            category_a_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CATEGORIES')))
            category_a_link.click()

            category_a_1_link = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.LINK_TEXT, 'CATEGORY-A-1')))
            category_a_1_link.click()

            category_a_1_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.title')))
            self.assertTrue(category_a_1_title.is_displayed(), "Category A 1 title is not displayed")

            products_list = self.driver.find_elements(By.CSS_SELECTOR, '.product-list li')
            self.assertGreater(len(products_list), 0, "Products list is empty")
        except Exception as e:
            self.fail(f"Failed to navigate to category page: {str(e)}")

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()