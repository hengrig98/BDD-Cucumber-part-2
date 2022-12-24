from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

@given(u'Login Page is displayed.')
def launch_login_page(context):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    context.driver.implicitly_wait(10)
# BACKGROUND step^^^

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
    context.driver.quit()
   
# Positive test scenario that covers feature file...
@when(u'User clicks login button.')
def click_login(context):
    context.driver.find_element(By.CSS_SELECTOR, ".oxd-button").click()
    sleep(5)


@then(u'New page will display.')
def homepage(context):
    assert context.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").is_displayed()
    context.driver.quit()
    