from selenium import webdriver
from selenium.webdriver import ActionChains as ac
from selenium.webdriver.common.keys import Key
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select as s

class TestShop(unittest.TestCase):
def setUp(self):
self.driver = webdriver.Chrome()

# test main UI components
def test_main_ui_components(self):
headers = self.find_by_id("header")
self.assertEqual(len(headers), 0)
buttons = self.find_by_css_selector(".btn.btn-primary")
self.assertEqual(len(buttons), 1)
links = self.find_by_css_selector(".nav-link")
self.assertEqual(len(links), 4)

# test login and register pages
def test_login(self):
login_url = "http://localhost/login"
self.driver.get(login_url)

username_field = self.find_by_name("username")
password_field = self.find_by_name("password")

# wait for the elements to be visible before interacting with them
username_field_wait = WebDriverWait(self.driver, 20).until(
lambda x: self.find_by_name("username")
)
password_field_wait = WebDriverWait(self.driver, 20).until(
lambda x: self.find_by_name("password")
)

# try logging in with a wrong username or password
wrong_username = "incorrect_username"
self.driver.execute_script(f"document.getElementsByName('username').value='{wrong_username}'")

# try logging in with a correct username and password
correct_password = "correct_password"
self.driver.execute_script(f"document.getElementsByName('password').value '{correct_password}'")

def tearDown(self):
self.driver.quit()

if __name__ == "__main__":
unittest.main()