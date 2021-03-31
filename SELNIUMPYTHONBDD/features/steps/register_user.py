#coding=utf-8
import os
import sys
sys.path.append(os.getcwd())
from features.lib.pages.register_page import RegisterPage
from behave import *
# import os
# import sys
# sys.path.append("D:\PycharmProject\SeleniumPythonBDD")


use_step_matcher('re')

@when('I open the register website')
def step_register(context):
    RegisterPage(context).get_url("http://www.5itest.cn/register")

@then('I expect that the title is "([^"]*)"')
def step_register(context,title_name):
    title = RegisterPage(context).get_title()
    assert  title_name in title

@when('I set with usermail "([^"]*)"')
def step_register(context,usermail):
    RegisterPage(context).send_email(usermail)

@when('I set with username "([^"]*)"')
def step_register(context,username):
    RegisterPage(context).send_username(username)

@when('I set with password "([^"]*)"')
def step_register(context,password):
    RegisterPage(context).send_password(password)

@when('I set with code "([^"]*)"')
def step_register(context,code):
    RegisterPage(context).send_code(code)

@when('I click with registerbutton')
def step_register(context):
    RegisterPage(context).click_registerbtn()

@then('I expect that text "([^"]*)"')
def step_register(context,code_text):
    text =RegisterPage(context).register_text()
    assert code_text in text