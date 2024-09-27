from selenium.webdriver.common.by import By

class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.clear()
        search_box.send_keys(product_name)
        self.driver.find_element(By.ID, "nav-search-submit-button").click()


    def get_results_message(self):
        try:
                    # Locate the 'No results' message span element by its class
            message_element = self.driver.find_element(By.XPATH, "//span[contains(@class, 'a-size-medium a-color-base') and contains(text(), 'No results for')]")
            return message_element.text  # Return the 'No results for' text if found
        except:
            # If no 'No results' message, assume results are found and return a generic message
            return "Results found"

    def get_product_results(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".s-main-slot .s-title")
