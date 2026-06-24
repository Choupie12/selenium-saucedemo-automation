# Selenium SauceDemo Automation Project

## Project Overview

This project demonstrates UI test automation using Selenium WebDriver and Python on the SauceDemo e-commerce application.

The objective is to validate key user journeys such as login, cart management, checkout process, and negative authentication scenarios through automated functional testing.
 
---

## Tools & Technologies

* Python 3.13
* Selenium WebDriver
* Google Chrome
* ChromeDriver
* Git & GitHub

---

## Application Under Test

Website: https://www.saucedemo.com

---

## Automated Test Scenarios

### TC_UI_001 – Successful Login

* Login with valid credentials
* Verify redirection to Products page

### TC_UI_002 – Invalid Login

* Login with invalid credentials
* Verify error message is displayed

### TC_UI_003 – Add Product to Cart

* Add Sauce Labs Backpack to cart
* Verify cart badge is updated

### TC_UI_004 – Logout

* Logout from application
* Verify redirection to Login page

### TC_UI_005 – Remove Product from Cart

* Add product to cart
* Remove product from cart
* Verify cart badge disappears

### TC_UI_006 – Complete Checkout Process

* Add product to cart
* Complete checkout workflow
* Verify order confirmation message

### TC_UI_007 – Login with Locked User

* Login with locked user credentials
* Verify access is denied
* Verify error message is displayed

---

## Project Structure

```text
Selenium-SauceDemo-Project
│
├── tests
│   ├── test_login.py
│   ├── test_invalid_login.py
│   ├── test_add_to_cart.py
│   ├── test_logout.py
│   ├── test_remove_from_cart.py
│   ├── test_checkout.py
│   └── test_locked_user.py
│
├── test_cases
│   └── SauceDemo_Test_Cases.xlsx
│
├── screenshots
│
├── requirements.txt
└── README.md
```

---

## How to Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run a test:

```bash
py tests/test_login.py
```

Example:

```bash
py tests/test_checkout.py
```

---

## Test Design Approach

The project covers:

* Functional Testing
* UI Testing
* Positive Testing
* Negative Testing
* End-to-End Testing
* Basic Test Automation Framework Structure

---

## Author

Felicienne Miezan

QA Automation Portfolio Project
