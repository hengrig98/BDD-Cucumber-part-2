from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


# Negative test scenario using parametrization...
@when(u'User enters username "{username}".')
def step_impl(context, username):
    if username == 'empty': username = ''
    context.driver.find_element(By.NAME, "username").send_keys(username)


@when(u'User enters password "{password}".')
def step_impl(context, password):
    if password == 'empty': password = ''
    context.driver.find_element(By.NAME, "password").send_keys(password)

@then(u'text "{text}" will display.')
def step_impl(context, text):
    sleep(5)
    assert text.lower() in context.driver.page_source.lower()
    context.logger.info(f"{text} displayed with invalid credentials")
   
# Positive test scenario that covers feature file...

@when(u'User enters username "Admin"')
def step_impl(context):
    context.driver.find_element(By.NAME, "username").send_keys("Admin")
       

@when(u'User enters password "admin123"')
def step_impl(context):
     context.driver.find_element(By.NAME, "password").send_keys("admin123")
       

@when(u'User clicks login button.')
def step_impl(context):
    context.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()


@then(u'Home page should display.')
def step_impl(context):
    sleep(5)
    assert context.driver.find_element(By.CSS_SELECTOR, '.oxd-userdropdown').is_displayed()
    context.logger.info(f"Successfully landed on Homepage")