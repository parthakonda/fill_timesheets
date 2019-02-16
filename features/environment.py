import json
import os

from selenium import webdriver


def before_all(context):
    """
    Before execution all
    """
    # Set browser
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()

    # User configuration data
    context.config = json.loads(open("./features/config.json").read())

    REPLICON_COMPANY = os.getenv('REPLICON_COMPANY', None)
    REPLICON_USERNAME = os.getenv('REPLICON_USERNAME', None)
    REPLICON_PASSWORD = os.getenv('REPLICON_PASSWORD', None)

    if REPLICON_COMPANY:
        context.config['REPLICON_COMPANY'] = REPLICON_COMPANY
    if REPLICON_USERNAME:
        context.config['REPLICON_USERNAME'] = REPLICON_USERNAME
    if REPLICON_PASSWORD:
        context.config['REPLICON_PASSWORD'] = REPLICON_PASSWORD


def before_feature(context, feature):
    """
    Before execution of behave
    """
    print("before_feature()")


def after_scenario(context, scenario):
    """
    Execution of scenario
    """
    print("after_scenario()")


def after_feature(context, feature):
    """
    Execute after feature
    """
    print("after_feature()")


def after_all(context):
    """
    Execute after all at end
    """
    context.browser.quit()
    print("after_all()")
