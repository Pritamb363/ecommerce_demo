from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
import os
from selenium.webdriver.chrome.options import Options

class BaseTest:
    def setup_method(self, method, browser='chrome'):
        # Specify the path to your ChromeDriver
        # Get the current script's directory
        current_dir = os.path.dirname(os.path.abspath(__file__))  
        
        # Navigate to the driver directory located in the parent directory
        chrome_driver_path = os.path.join(current_dir, '..', 'driver', 'chromedriver.exe')
        chrome_options = Options()

        # Initialize the WebDriver based on the browser choice
        if browser == 'chrome':
            self.driver = webdriver.Chrome(chrome_options, service=ChromeService(executable_path=chrome_driver_path))
        # Maximize the window after initializing the driver
        self.driver.maximize_window()
        self.driver.set_page_load_timeout(10)
        self.driver.get("https://www.amazon.in")



    def teardown_method(self, method):
        if self.driver:
            self.driver.quit()

