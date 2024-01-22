import unittest, time, os
from builtins import id

from appium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from appium.options.android import UiAutomator2Options
from Data import TestData
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime

from funcoes import Funcoes

class AndroidBudget(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=capabilities_options)


    #Adiciona BUDGET
    def test_app_budget_add(self):
        Funcoes.adicionarBudget(self)

        self.assertEqual(TestData.budget_type, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'supermarket')]").get_attribute(
            'text'))
        

    #Adiciona TRANSACTIONS
    def test_app_transactions_add(self):
        Funcoes.adicionarTransactions(self)

        self.assertEqual(TestData.super, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'Super2')]").get_attribute(
            'text'))


    #Edita Transactions
    def test_app_transactions_edit(self):
        Funcoes.adicionarTransactions(self)

        # clicar em editar

        itemCadast = self.driver.find_element(By.ID, 'protect.budgetwatch:id/name')
        itemCadast.click()
        self.driver.implicitly_wait(30)

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_edit')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.clear()
        name.send_keys("NaoSuper2")

        budgetSpin = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetSpinner')
        budgetSpin.clear()
        budgetSpin.click()
        escolherBudgat = self.driver.find_element(By.XPATH,
                                                  '//android.widget.TextView[@resource-id="protect.budgetwatch:id/text" and @text="supermarket"]')
        escolherBudgat.click()

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.clear()
        account.send_keys("5000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.clear()
        value.send_keys("1")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.clear()
        note.send_keys("testandoEditar")

        calendar = self.driver.find_element(By.ID, 'protect.budgetwatch:id/dateEdit')
        calendar.clear()
        calendar.click()
        dataCalendar = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="06 December 2023"]')
        dataCalendar.click()
        ok = self.driver.find_element(By.ID, 'android:id/button1')
        ok.click()

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()


        self.assertEqual(TestData.nsuper, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'NaoSuper2')]").get_attribute(
            'text'))


    #Exclui Transactions
    def test_app_transactions_delet(self):
        Funcoes.adicionarTransactions(self)

        # clicar em editar
        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/name')
        add.click()
        self.driver.implicitly_wait(30)

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_edit')
        add.click()

        #processo para deletar
        pontinhos = self.driver.find_element(By.XPATH,
                                          "//android.widget.ImageView[@content-desc='More options']")
        pontinhos.click()
        

        excluir = self.driver.find_element(By.ID, 'protect.budgetwatch:id/title')
        excluir.click()

        confirmar = self.driver.find_element(By.ID, 'android:id/button1')
        confirmar.click()


        try:
            elemento_apos_exclusao = self.driver.find_element(By.ID, 'protect.budgetwatch:id/name')
            texto_elemento_apos_exclusao = elemento_apos_exclusao.get_attribute('text')
            self.assertEquals("", texto_elemento_apos_exclusao, "O elemento não foi deletado corretamente.")
        except NoSuchElementException:
            print("\nO elemento foi deletado e não está mais disponível")

    
    #Campo VALOR vazio
    def test_app_valorVazio(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Texto do campo
        try:
            elementVazio = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@resource-id, 'protect.budgetwatch:id/snackbar_text')]")
            elementVazio2 = elementVazio.get_attribute('text')
            self.assertEqual(TestData.valorVazio, elementVazio2, "O campo VALUE está vazio. Não pode salvar. Preencha corretamente")
        except NoSuchElementException:
            pass


    #Campo NOME vazio
    def test_app_NomeVazio(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("123")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        
        # Verificando se permanece na mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionViewActivity"

        self.assertEqual(pag_esperada, pag_atual, "CAMPO NOME ESTÁ VAZIO. Não deveria ter salvado!!!") 


    #Campo NOME e VALOR vazios
    def test_app_NomeValorVazio(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Texto do campo
        elementVazio = self.driver.find_element(By.XPATH,
                                        "//android.widget.TextView[contains(@resource-id, 'protect.budgetwatch:id/snackbar_text')]")
        elementVazio2 = elementVazio.get_attribute('text')
        self.assertEqual(TestData.nomeValorVazio, elementVazio2, "O campo nome e valor estão vazios. Não pode salvar. Preencha corretamente")


    #Nome menor que 2 caracteres
    def test_app_nomeMenorQueDoisCaracteres(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("S")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionViewActivity"

        self.assertEqual(pag_esperada, pag_atual, "Nome menor que 2 caracteres. Não deveria ter salvado!!") 


    #Nome maior que 20 caracteres
    def test_app_nomeMaiorQueVinteCaracteres(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("SuperMarioSuperMarioB")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionViewActivity"

        self.assertEqual(pag_esperada, pag_atual, "Nome maior que 20 caracteres. Não deveria ter salvado!!") 


    #Account menor que 3 caracteres
    def test_app_accountMenorQueTresCaracteres(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("20")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionViewActivity"

        self.assertEqual(pag_esperada, pag_atual, "Campo account menor que 3 caracteres. Não deveria ter salvado!!") 


    #Account maior que 8 caracteres
    def test_app_accountMaiorQueOitoCaracteres(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("200020002")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionViewActivity"

        self.assertEqual(pag_esperada, pag_atual, "Campo ACCOUNT maior que 8 caracteres. Não deveria ter salvado!!") 


    #Account invalido
    def test_app_accountInvalido(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys('[!@#$%^&*(),.?"":{}|<>]')

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionViewActivity"

        self.assertEqual(pag_esperada, pag_atual, "O campo account contem caracteres especiais. Nao deve salvar!") 


    #Account permite caracter '-'
    def test_app_accountSimboloValido(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys('2000-')

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionActivity"

        self.assertEqual(pag_esperada, pag_atual, "O campo account deve permitir a utilização do caracter '-!") 


    #Campo VALUE com numero inteiro
    def test_app_valueComNumeroInteiro(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys('2000')

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionActivity"

        self.assertEqual(pag_esperada, pag_atual, "Tem algo errado pois deve aceitar numero inteiro!!") 

    
    #Campo VALUE com numero decimal até 2 casas decimais
    def test_app_valueComNumeroAteDuasCasasDecimais(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys('2000')

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("10.000000000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se o VALUE salvo tem até 2 casas decimais
        valorElement = self.driver.find_element(By.ID, "protect.budgetwatch:id/value").get_attribute('text')
        valorParse = float(valorElement)
        valorFormatado = "{:.2f}".format(valorParse)

        self.assertEqual(len(valorFormatado), 5, f"O valor {valorElement} tem mais de duas casas decimais.")

        
    #Campo VALUE com string
    def test_app_valueComString(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys('2000')

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("Tudo bem")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Texto do campo
        try:
            elementVazio = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@resource-id, 'protect.budgetwatch:id/snackbar_text')]")
            elementVazio2 = elementVazio.get_attribute('text')
            self.assertEqual(TestData.valorInvalido, elementVazio2, "O campo VALUE está vazio. Não pode salvar. Preencha corretamente")
        except NoSuchElementException:
            pass


    #Campo value com caracter
    def test_app_valueComCaracter(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys('2000')

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("[!@#$%^&*(),.?"":{}|<>-]")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Texto do campo
        try:
            elementVazio = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@resource-id, 'protect.budgetwatch:id/snackbar_text')]")
            elementVazio2 = elementVazio.get_attribute('text')
            self.assertEqual(TestData.valorInvalido, elementVazio2, "O campo VALUE está vazio. Não pode salvar. Preencha corretamente")
        except NoSuchElementException:
            pass

    
    #Campo value com numero negativo
    def test_app_valueNegativo(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em Transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys('2000')

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("-1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Texto do campo
        try:
            elementVazio = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@resource-id, 'protect.budgetwatch:id/snackbar_text')]")
            elementVazio2 = elementVazio.get_attribute('text')
            self.assertEqual(TestData.valorInvalido, elementVazio2, "O campo VALUE está vazio. Não pode salvar. Preencha corretamente")
        except NoSuchElementException:
            self.fail("O campo VALUE nao pode ser numero negativo. Não pode salvar. Deveria ter snackbar_text com 'Value invalid'")


    #Campo note maior que 20 caracteres
    def test_app_noteMaiorQueVinteCaracteres(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0testando0123")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # Verifica se permanece a mesma activity ou se mudou
        pag_atual = self.driver.current_activity
        pag_esperada = ".TransactionViewActivity"

        self.assertEqual(pag_esperada, pag_atual, "Campo NOTE maior que 20 caracteres. Não deveria ter salvado!!") 


    #DATA
    #Este teste verifica tanto formato de data válido quanto data futura. Se o formato tiver certo, ele prossegue com o teste
    #Para visualização do formato inválido, resolvi dividir em 2 testes. A unica mudança foi colocar uma data com formato inválido
    def test_app_naoPodeAceitarDataFutura(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        
        calendar = self.driver.find_element(By.ID, 'protect.budgetwatch:id/dateEdit')
        calendar.click()
        dataCalendar = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="20 December 2023"]')
        dataCompleta =  dataCalendar.get_attribute('content-desc')
        dataCalendar.click()
        ok = self.driver.find_element(By.ID, 'android:id/button1')
        ok.click()

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()


        # Verificar se a data selecionada é data com formato inválido e se é data futura
        data = dataCompleta

        try:
            data_selecionada = datetime.strptime(data, "%d %B %Y") 
            data_atual = datetime.now()

            self.assertTrue(data_selecionada <= data_atual, "A data selecionada é uma data futura. Não deve permitir data futura!!")
        except ValueError:
            self.fail("O teste falhou devido a um formato de data inválido.")


    def test_app_formatoDeData(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em transactions
        trans = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        trans.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        
        calendar = self.driver.find_element(By.ID, 'protect.budgetwatch:id/dateEdit')
        calendar.click()
        dataCalendar = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="20 December 2023"]')
        dataCompleta =  dataCalendar.get_attribute('content-desc')
        dataCalendar.click()
        ok = self.driver.find_element(By.ID, 'android:id/button1')
        ok.click()

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()


        # Verificar se a data selecionada é data com formato inválido e se é data futura
        #data = dataCompleta
        data = "09/12/2023"

        try:
            data_selecionada = datetime.strptime(data, "%d %B %Y") 
            print(data_selecionada)
            data_atual = datetime.now()
            print(data_atual)

 
            self.assertTrue(data_selecionada <= data_atual, "A data selecionada é uma data futura. Não deve permitir data futura!!")
        except ValueError:
            self.fail("O teste falhou devido a um formato de data inválido.")




    def tearDown(self):
        self.driver.quit()





if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)