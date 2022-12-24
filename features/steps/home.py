from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


@when(u'User clicks dropdown menu option.')
def click_user_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown").click()


@when(u'User clicks user menu option "{option}".')     
def checking_for_menu_options(context, option):
    context.driver.find_element(By.LINK_TEXT, f'{option}').click()
    # sleep(5)
    # assert "{text}" in context.driver.page_source