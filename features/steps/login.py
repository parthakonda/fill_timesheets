from behave import *
from selenium import webdriver
from selenium.common.exceptions import (ElementNotInteractableException,
                                        NoSuchElementException)
from selenium.webdriver.common.by import By
import time


@given('Go to login page')
def go_to_login_page(context):
    """
    user is in login page of Replicon
    """
    context.browser.get(context.config['APP_URL'])
    context.browser.implicitly_wait(60)


@when("fill valid credentials")
def fill_valid_credentials(context):
    browser = context.browser
    # Fill company name
    company = browser.find_element(By.ID, 'CompanyNameTextBox')
    company.send_keys(context.config['REPLICON_COMPANY'])
    # Fill username
    username = browser.find_element(By.ID, 'LoginNameTextBox')
    username.send_keys(context.config['REPLICON_USERNAME'])
    # Fill password
    password = browser.find_element(By.ID, 'PasswordTextBox')
    password.send_keys(context.config['REPLICON_PASSWORD'])


@then("click on login")
def click_on_login(context):
    # Click login
    login_button = context.browser.find_element(By.ID, 'LoginButton')
    login_button.click()
    time.sleep(10)
