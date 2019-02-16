from behave import *
import time


@given("fill valid time")
def fill_valid_time(context):
    """
    filling all as 8
    """
    time.sleep(10)
    all_days = context.browser.find_elements_by_css_selector(
        'td.day input')
    for idx, day in enumerate(all_days):
        if idx < 5:
            day.send_keys("8.00")
        if idx >= 5:
            day.send_keys("0.00")
    time.sleep(2)


@then("click on submit")
def click_on_submit(context):
    """
    Click on submit for approval
    """
    submit_for_approval = context.browser.find_elements_by_css_selector(
        "input[type='button'][value='Submit for Approval']")
    for item in submit_for_approval:
        item.click()
    time.sleep(10)
