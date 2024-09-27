## E-Commerce Automation Framework Documentation

## Overview
The E-Commerce Automation Framework is designed for automating the testing of e-commerce functionalities such as searching for products, adding items to the cart, updating product quantities, and verifying cart operations. It uses Selenium WebDriver, PyTest, and other utilities to perform the tests and generate comprehensive reports.
## Directory Structure
ecommerce_demo/
|
├──driver/
|   ├──chromedriver.exe       # WebDriver for Chrome browser automation
|
├── tests/
│   ├── test_search_cart.py    # PyTest test cases for search and cart functionalities
|
├── pages/
│   ├── search_page.py         # Page Object Model (POM) class for search page
│   ├── cart_page.py           # POM class for cart page operations
|
├── utils/
│   ├── base_test.py           # Base class for setting up and tearing down WebDriver
│   ├── reporting.py           # Utility for generating test reports
|
├── input.json                 # Test data for search terms and product quantities
├── reports/
│   ├── report.html            # HTML report generated after running tests
|
├── requirements.txt           # Python dependencies needed for the framework
├── pytest.ini                 # Configuration for PyTest
└── README.md                  # Project documentation

## Clone the repository:
To get started, clone the repository using the following command:
   git clone https://github.com/Pritamb363/ecommerce_demo.git

## Install dependencies:
After cloning the repository, navigate to the project directory and install the necessary dependencies listed in the requirements.txt file:
    pip install -r requirements.txt

## ChromeDriver
Make sure that the chromedriver.exe is available in the driver/ directory. If you're using a different version of Chrome, update your chromedriver.

## How to Run the Tests
## Run All Tests
To execute all the test cases in the tests/ directory, use the following PyTest command. This will also generate an HTML report in the reports/ folder.
    pytest tests/ --html=reports/report.html

## View the report:
    Open reports/report.html in a browser.

## Sample Expected Results

Passed	tests/test_search_cart.py::TestECommerce::test_search_and_cart_flow[test_case0]	13.07	
 ------------------------------Captured stdout call------------------------------ 
Test Case: No results found for 'ld345tsxslfer'

Passed	tests/test_search_cart.py::TestECommerce::test_search_and_cart_flow[test_case1]	32.70	
 ------------------------------Captured stdout call------------------------------ 
Test Case: Results found for 'Laptop'
4th Product added to cart
Subtotal: Subtotal (1 item):, Amount:    41,990.00
Updated quantity in the cart
Subtotal: Subtotal (2 items):, Amount:    83,980.00
_________________________________________________________________________

## How the Framework Works
## Test Execution Flow:
- The test cases in test_search_cart.py use the load_test_data() method  to read from input.json.
- Search for products, add items to the cart, update the cart, and remove items are all performed based on the methods in search_page.py and cart_page.py.

## Page Object Model (POM):
- The framework separates logic related to page interaction into search_page.py and cart_page.py. This makes the code modular, reusable, and maintainable.

## Reporting:
- After the test execution, an HTML report is generated using the --html option in PyTest. This report provides a detailed overview of test results, including pass/fail status and error tracebacks (if any).
_________________________________________________________________________

## Test Case: Search and Add Product to Cart
- Search for a product.
- Verify the product appears in the results.
- Add the 4th product from the list to the cart.
- Update the quantity to 2.
- Verify the subtotal reflects the correct quantity and price.
- Remove the product from the cart and verify the cart is empty.
_________________________________________________________________________

## Troubleshooting
- Browser Compatibility Issues:
Ensure chromedriver.exe is up to date and compatible with your installed version of Chrome. If tests fail, consider updating chromedriver from ChromeDriver Download.

- Missing Dependencies:
If the tests fail to execute, verify that all required dependencies are installed by running:
    pip install -r requirements.txt

## Contact
For any issues or contributions, feel free to reach out or submit a pull request on GitHub.
