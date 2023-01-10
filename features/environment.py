from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
from time import sleep
from configs import config
from logs.logger import logger

def before_all(context):
    context.timeout = 10
    context.logger = logger
    print("##### before all #####")


def before_scenario(context, scenario):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.logger.info(f"Successfully launched {context.driver.name}")
    context.driver.get(config.URL)
    context.logger.info(f"Successfully navigated to {config.URL}")
    context.driver.implicitly_wait(context.timeout)
    

    print(f"###### {scenario.name} ######")

    if 'login' not in scenario.name.lower():
        context.driver.find_element(By.NAME, "username").send_keys(config.USERNAME)
        context.driver.find_element(By.NAME, "password").send_keys(config.PASSWORD)
        context.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
        context.logger.info(f"Successfully landed on Homepage")
    

def after_scenario(context, scenario):
    timestamp = datetime.now().strftime('%m%d%y_%H%M%S')
    context.driver.save_screenshot(fr".\evidence\{scenario.name}_{timestamp}.png")
    context.driver.quit()
    print(f"##### {scenario.name} Passed #####")
    context.logger.info("Successfully closed browser.")
