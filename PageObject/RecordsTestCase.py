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
from Records import RecordsPage



class AndroidExpenseReport(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] =  'emulator-5554'           #'RX8T602267D'           #'emulator-5554'
        desired_caps['appPackage'] = 'com.blogspot.e_kanivets.moneytracker'
        desired_caps['appActivity'] = 'com.blogspot.e_kanivets.moneytracker.activity.record.MainActivity'
        desired_caps['autoGrantPermissions'] = True

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        self.driver = webdriver.Remote('http://127.0.0.1:4724/wd/hub', options=capabilities_options)



    def test_todosIncomesExpensesSalvosNaTelaRecords(self):
        intro_page = MainPage(self.driver)  
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver)
        add.addExpense()
        price = AddExpensePage(self.driver)
        price.type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver)
        title.type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver)
        categoria.type_categoria(TestData.categoriaExpense)
        calendar = RecordsPage(self.driver).get_CalendarDate()
        dataCalendar = RecordsPage(self.driver).click_dataEscolhida()
        dataCompleta = RecordsPage(self.driver).get_dataEscolhida()
        ok = RecordsPage(self.driver).click_okData()
        save = AddExpensePage(self.driver)
        save.click_save()

        week = RecordsPage(self.driver)
        week.click_weef()
        allTime = RecordsPage(self.driver)
        allTime.click_allTime()

        # 
        self.assertEqual(TestData.titleExpense, self.driver.find_element(By.XPATH,
                                                                  "//android.widget.TextView[contains(@text, 'Conserto telhado')]").get_attribute(
            'text'))


    def test_shortSummary(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        
        save = AddExpensePage(self.driver).click_save()

        sumary = RecordsPage(self.driver)
        sumary.click_shortSummary()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = TestData.activityReport

        self.assertEqual(pag_esperada, pag_atual, "ERRO! Não foi para a página SHORT SUMMARY!")
        

    def test_duplicidade(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        #Expense1
        add = AddExpensePage(self.driver)
        add.addExpense()
        price = AddExpensePage(self.driver)
        price.type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver)
        title.type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver)
        categoria.type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver)
        save.click_save()

        #Expense2
        add = AddExpensePage(self.driver)
        add.addExpense()
        price = AddExpensePage(self.driver)
        price.type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver)
        title.type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver)
        categoria.type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver)
        save.click_save()

        #Colocando cada elemento dos expenses em uma lista para comparação
        elemTitle1 = RecordsPage(self.driver).get_title1()
        elemTitle2 = RecordsPage(self.driver).get_title2()
        elemCategory1 = RecordsPage(self.driver).get_category1()
        elemCategory2 = RecordsPage(self.driver).get_category2()
        elemPrice1 = RecordsPage(self.driver).get_price1()
        elemprice2 = RecordsPage(self.driver).get_price2()
        elementoData = RecordsPage(self.driver).get_data()
        self.driver.implicitly_wait(30)

        lista1 = [elemTitle1, elemCategory1, elemPrice1, elementoData]
        lista2 = [elemTitle2, elemCategory2, elemprice2, elementoData]   

        try:
            self.assertNotEqual(lista1, lista2, "Eles são iguais")
        except AssertionError:
            self.fail("Elementos salvos em duplicidade!! Ele não deve permitir salvar")


    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidExpenseReport)
    unittest.TextTestRunner(verbosity=2).run(suite)
