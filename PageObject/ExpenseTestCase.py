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

    
    ############### EXPENSE #######################
    def test_addExpense(self):
        main = MainPage(self.driver)
        self.driver.implicitly_wait(30)
        add = AddExpensePage(self.driver).addExpense()

        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)

        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(30)

        self.assertEqual(TestData.titleExpense, self.driver.find_element(By.XPATH,
                                                                  "//android.widget.TextView[contains(@text, 'Conserto telhado')]").get_attribute(
            'text'))


    def test_categoryComNumeros(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoryComNumeros)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = TestData.activityExpensive
        pag_atual2 = self.driver.current_activity

        self.assertEqual(pag_esperada, pag_atual2, "Campo CATEGORY com numeros, só pode string. Não deveria ter salvado!!")


    def test_categoryMaiorQueTrintaCaracteres(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoryMaiorTrinta)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = TestData.activityExpensive
        pag_atual2 = self.driver.current_activity

        self.assertEqual(pag_esperada, pag_atual2, "Campo CATEGORY maior que 30 caracteres. Não deveria ter salvado!!")


    def test_categoryVazio(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.campoVazio)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_esperada = TestData.activityExpensive
        pag_atual2 = self.driver.current_activity

        self.assertEqual(pag_esperada, pag_atual2, "Campo CATEGORY está vazio. Não deveria ter salvado!!")


    def test_dataPassada(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        calendar = RecordsPage(self.driver).get_CalendarDate()
        dataCalendar = AddExpensePage(self.driver).click_dataEscolhidaPassada()
        dataCompleta = AddExpensePage(self.driver).get_dataPassada()
        ok = RecordsPage(self.driver).click_okData()
        save = AddExpensePage(self.driver).click_save()

        week = RecordsPage(self.driver)
        week.click_weef()
        allTime = RecordsPage(self.driver)
        allTime.click_allTime()
        self.driver.implicitly_wait(90)

        dataSelecionada = dataCompleta
        dataSalva = self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, '7 December 2023')]").get_attribute('text')
        if (dataSalva < "10 December 2023"):
            dataSalva = "0"+dataSalva
            print(dataSalva)
        else:
            return dataSalva
      
        try:
            self.assertEqual(dataSelecionada, dataSalva)
        except AssertionError:
            self.fail("Elemento não foi salvo pois não aparece na tela Records! Ele deve permitir datas passadas.")


    def test_editarExpense(self):
        main = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        #adicionar
        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(30)

        #editar
        add = AddExpensePage(self.driver).click_localizado()
        price = AddExpensePage(self.driver).type_price(TestData.new_priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.new_titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.new_categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(30)

        self.assertEqual(TestData.new_titleExpense, self.driver.find_element(By.XPATH,
                                                                   "//android.widget.TextView[contains(@text, 'Conserto calha')]").get_attribute('text'))


    def test_excluirExpense(self):
        main = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        #adicionar
        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(30)

        #seleciona expense salvo
        add = AddExpensePage(self.driver).click_localizado()

        excluir = AddExpensePage(self.driver).click_delete()
        self.driver.implicitly_wait(30)

        try:
            elementoParaExcluir = AddExpensePage(self.driver).get_localizaExpense()
            self.assertEquals("", elementoParaExcluir, "O elemento não foi deletado corretamente.")
        except NoSuchElementException:
            print("\nO elemento foi deletado e não está mais disponível")


    def test_naoPodeAceitarDataFutura(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        calendar = RecordsPage(self.driver).get_CalendarDate()
        dataCalendar = AddExpensePage(self.driver).click_dataEscolhidaFutura()
        dataCompleta = AddExpensePage(self.driver).get_dataFutura()
        ok = RecordsPage(self.driver).click_okData()
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Data selecionada
        data = dataCompleta     
        # Data salva
        dataSalva = AddExpensePage(self.driver).get_dataSalva()

        self.assertNotEqual(data, dataSalva, "A data selecionada é uma data futura. Não deve permitir salvar com data futura!!")


    def test_priceMaiorQueTrezeCaracteres(self):
        main = MainPage(self.driver)       
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceMaiorTreze)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(60)

        # Verifica se permanece a mesma activity ou se mudou
        pagAtual = self.driver.current_activity
        pagEsperada = TestData.activityExpensive 

        self.assertEqual(pagEsperada, pagAtual, "Campo PRICE maior que 13 caracteres. Não deveria ter salvado!!")


    def test_priceNegativo(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceNegativo)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".activity.record.AddRecordActivity"
        pag_atual2 = self.driver.current_activity

        self.assertEqual(pag_esperada, pag_atual2, "Campo PRICE tem numero negativo. Não deveria ter salvado!!")


    def test_priceString(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceString)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(60)

        # Texto do campo
        try:
            textoErro = AddExpensePage(self.driver).get_erroPrice()
            self.assertEqual(TestData.campoPriceErro, textoErro,
                             "O campo PRICE nao pode ser string. Não pode salvar. Preencha corretamente")
        except NoSuchElementException:
            self.fail("O campo PRICE nao pode ser string. Não pode salvar.")


    def test_priceVazio(self):
        main = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.campoVazio)
        title = AddExpensePage(self.driver).type_title(TestData.titleExpense)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(60)

        # Verifica se permanece a mesma activity ou se mudou
        pagAtual = self.driver.current_activity
        pagEsperada = TestData.activityExpensive

        self.assertEqual(pagEsperada, pagAtual, "Campo PRICE está vazio. Não deveria ter salvado!!")


    def test_titleComNumeros(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleComNumeros)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = TestData.activityExpensive
        pag_atual2 = self.driver.current_activity

        self.assertEqual(pag_esperada, pag_atual2, "Campo TITLE com numeros, só pode string. Não deveria ter salvado!!")


    def test_titleMaiorQueVinteCaracteres(self):
        intro_page = MainPage(self.driver)
        self.driver.implicitly_wait(30)

        add = AddExpensePage(self.driver).addExpense()
        price = AddExpensePage(self.driver).type_price(TestData.priceExpensive)
        title = AddExpensePage(self.driver).type_title(TestData.titleMaiorVinte)
        categoria = AddExpensePage(self.driver).type_categoria(TestData.categoriaExpense)
        save = AddExpensePage(self.driver).click_save()
        self.driver.implicitly_wait(90)

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".activity.record.AddRecordActivity"
        pag_atual2 = self.driver.current_activity

        self.assertEqual(pag_esperada, pag_atual2, "Campo TITLE com mais de 20 caracteres. Não deveria ter salvado!!")


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




