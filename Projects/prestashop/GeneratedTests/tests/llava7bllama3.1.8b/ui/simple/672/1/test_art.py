import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class TestUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://localhost:8080/en/")

    def test_main_ui_components(self):
        # Header
        header = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='header']")))
        self.assertIsNotNone(header)

        # Search Bar
        search_bar = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//input[@id='search']")))
        self.assertIsNotNone(search_bar)

        # Menu Items
        menu_items = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='menu']/li/a")))
        self.assertGreater(len(menu_items), 0)

        # User Icon and Notification Bell
        user_icon = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='user-icon']")))
        notification_bell = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='notification-bell']")))
        self.assertIsNotNone(user_icon)
        self.assertIsNotNone(notification_bell)

        # Main Content Area
        main_content_area = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, "//main[@class='main-content']")))
        self.assertIsNotNone(main_content_area)

        # Cards
        cards = WebDriverWait(self.driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='card']")))
        self.assertGreater(len(cards), 0)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()