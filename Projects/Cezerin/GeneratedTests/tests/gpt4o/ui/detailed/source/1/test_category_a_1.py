import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestCategoryPageUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:3000/category-a-1")
        self.wait = WebDriverWait(self.driver, 20)

    def test_ui_elements(self):
        driver = self.driver
        wait = self.wait

        # Check header
        header = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'header')))
        self.assertTrue(header.is_displayed(), "Header not visible")

        # Check footer
        footer = wait.until(EC.visibility_of_element_located((By.TAG_NAME, 'footer')))
        self.assertTrue(footer.is_displayed(), "Footer not visible")

        # Check navigation links
        nav_links = driver.find_elements(By.CSS_SELECTOR, '.primary-nav a')
        self.assertGreater(len(nav_links), 0, "Navigation links are missing")
        for link in nav_links:
            self.assertTrue(link.is_displayed(), "Navigation link not visible")

        # Check search box
        search_box = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'search-input')))
        self.assertTrue(search_box.is_displayed(), "Search box not visible")

        # Check category title
        category_title = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'category-title')))
        self.assertTrue(category_title.is_displayed(), "Category title not visible")

        # Check sort dropdown
        sort_dropdown = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select')))
        self.assertTrue(sort_dropdown.is_displayed(), "Sort dropdown not visible")

        # Check mini-cart
        mini_cart = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, 'mini-cart')))
        self.assertTrue(mini_cart.is_displayed(), "Mini-cart not visible")

        # Interact with elements (e.g., click sort dropdown)
        sort_dropdown.click()
        wait.until(EC.visibility_of_element_located((By.XPATH, "//option[@value='-date_created']"))).click()

        # Confirm UI reaction by checking changed text
        selected_option = driver.find_element(By.XPATH, "//select/option[@selected]")
        self.assertEqual(selected_option.text, "Newest", "Sort option did not update correctly")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()