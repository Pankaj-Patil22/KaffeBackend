from time import sleep
import pytest
from pytest_bdd import scenarios, given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

home_page = 'http://127.0.0.1:5500/FrontEnd/templates/home.html'
scenarios('../features/choose_table.feature')

@pytest.fixture
def browser():
  browser = webdriver.Chrome()
  browser.implicitly_wait(50)
  yield browser
  browser.quit()

@given('the account is logged in')
def login(browser):
  browser.get(home_page)

@when('i click tables tab, it should nagivate to tables page')
def moving_to_tables_page(browser):
  browser.find_element(By.XPATH, '//*[@id="collapsibleNavbar"]/div/ul/li[2]/a').click()

@then('i choose the date and time')
def choose_date_time(browser):
  browser.find_element(By.ID, 'datefield').send_keys('28-10-2022')
  browser.find_element(By.ID, 'selectTS').click()
  browser.find_element(By.ID, 'time-12').click()

@then('i choose the table i want to book')
def choose_tables(browser):
  browser.find_element(By.XPATH, '/html/body/div/div[1]/ol/li[2]/ol/li[2]/label').click()
  browser.find_element(By.XPATH, '/html/body/div/div[1]/ol/li[2]/ol/li[3]/label').click()


@then('it should show me that total price')
def check_total(browser):
  total = browser.find_element(By.ID, 'totalPriceInfo')
  assert total.text == "Total Amount: 1000"