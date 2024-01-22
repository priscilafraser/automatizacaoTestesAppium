import unittest, time, os
from builtins import id

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep
from appium.options.android import UiAutomator2Options
from AddExpense import AddExpensePage
from Data import TestData
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

from BasePage import BasePage
from MainPage import MainPage




class AndroidExpense(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] =  'emulator-5554'           #'RX8T602267D'           #'emulator-5554'
        desired_caps['appPackage'] = 'com.blogspot.e_kanivets.moneytracker'
        desired_caps['appActivity'] = 'com.blogspot.e_kanivets.moneytracker.activity.record.MainActivity'
        desired_caps['autoGrantPermissions'] = True

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        self.driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', options=capabilities_options)


    def test_titleVazio(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.campoVazio)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = TestData.activityExpensive
        pag_atual2 = self.driver.current_activity

        self.assertEqual(pag_esperada, pag_atual2, "Campo TITLE vazio. Não deveria ter salvado!!")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidExpense)
    unittest.TextTestRunner(verbosity=2).run(suite)