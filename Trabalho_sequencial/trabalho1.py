import unittest, time, os
from builtins import id

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep
from appium.options.android import UiAutomator2Options
from Data import TestData
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Data import TestData
from datetime import datetime

from funcoes import Funcoes




class AndroidBudget(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] =  'emulator-5554'   #'RX8T602267D'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=capabilities_options)



    # Campo VALUE com numero inteiro
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




    


    """def test_app_valueComNumeroAteDuasCasasDecimais(self):
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
        valorDuasCasas = "{:.2f}".format(valorParse)

        self.assertEqual(len(valorDuasCasas), 5, f"O valor {valorDuasCasas} tem mais de duas casas decimais.")

        #self.assertEqual(pag_esperada, pag_atual, "Tem algo errado pois deve aceitar numero decimal!!") 

        # Verifique se a URL permanece a mesma ou se mudou
        #pag_atual = self.driver.current_activity
        #print(pag_atual)
        #pag_esperada = ".TransactionViewActivity"

        #self.assertEqual(pag_esperada, pag_atual, "Nao deve salvar pois o campo VALUE só pode ser numeros!") 
"""

        






        #elementVazio = self.driver.find_element(By.XPATH,
           #                             "//android.widget.TextView[contains(@resource-id, 'protect.budgetwatch:id/snackbar_text')]")
        #elementVazio2 = elementVazio.get_attribute('text')
        #self.assertEqual(TestData.nomeValorVazio, elementVazio2, "O campo nome e valor estão vazios. Não pode salvar. Preencha corretamente")
  
        
        
        #self.assertEqual(TestData.nomeValorVazio, elementVazio2, "O campo nome e valor estão vazios. Não pode salvar. Preencha corretamente")

        
        # Verificando se permanece na mesma activity ou se mudou
        #pag_atual = self.driver.current_activity
        #print(pag_atual)
        #pag_esperada = ".TransactionViewActivity"

        #self.assertEqual(pag_esperada, pag_atual, "Não deveria ter salvado com o campo NOME vazio!") 

        
        # Obter o texto do elemento
        #element_text = self.driver.find_element(By.ID, "protect.budgetwatch:id/nameEdit").get_attribute('text')

        # Verificar se o comprimento do texto é maior que 10
        #self.assertGreater(len(element_text), 2, f"O comprimento do nome  deve ser maior que ({len(element_text)}).")
        




    """    
    def test_app_accountMenorQueNove(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.send_keys(TestData.budget_type)

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys(TestData.budget_value)

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        if self.driver.find_element(By.XPATH, "//android.view.ViewGroup[@resource-id='protect.budgetwatch:id/toolbar']"):
            skip = self.driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Navegar para cima"]')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        budgat = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetSpinner')
        budgat.click()
        escolherBudgat = self.driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="protect.budgetwatch:id/text" and @text="supermarket"]')
        escolherBudgat.click()

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("0399www")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando000000000000")

        calendar = self.driver.find_element(By.ID, 'protect.budgetwatch:id/dateEdit')
        calendar.click()
        dataCalendar = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="05 dezembro 2023"]')
        dataCalendar.click()
        ok = self.driver.find_element(By.ID, 'android:id/button1')
        ok.click()

        campoAccount = self.driver.find_element(By.ID, "protect.budgetwatch:id/accountEdit").get_attribute('text')

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        
        #self.driver.execute_script("alert('Este é um alerta de teste!');")

     
        #self.assertLess(len(campoAccount), 9, f"O comprimento do nome  deve ser menor que ({len(campoAccount)}).")
        self.assertEqual(TestData.account, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, '0399www')]").get_attribute(
            'text'))
               

        # Obter o texto do elemento
        campoAccount = self.driver.find_element(By.ID, "protect.budgetwatch:id/accountEdit").get_attribute('text')


        # Verificar se o comprimento do texto é maior que 10
        try:
            alert = WebDriverWait(self.driver, 50).until(EC.alert_is_present())
            alerta = Alert(self.driver)
            texto = "Passou o tamanho"
            alert.accept()  # ou alert.dismiss() ou outras interações
        except NoAlertPresentException:
            # Nenhum alerta presente, faça algo conforme necessário
            print("Nenhum alerta presente na tela.")
                

        self.assertLess(len(campoAccount), 9, f"O comprimento do nome  deve ser menor que ({len(campoAccount)}).")"""
        #self.assertTrue(any(c.isalnum() or c in '!@#$%^&*()-_+=<>,.?/:;[]{}|' for c in campoAccount),
               # "O campo não contém pelo menos um caractere alfanumérico ou um símbolo.")


        

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)


"""def test_app_accountMenorQueNove(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.send_keys(TestData.budget_type)

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys(TestData.budget_value)

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        if self.driver.find_element(By.XPATH, "//android.view.ViewGroup[@resource-id='protect.budgetwatch:id/toolbar']"):
            skip = self.driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Navegar para cima"]')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        budgat = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetSpinner')
        budgat.click()
        escolherBudgat = self.driver.find_element(By.XPATH, '//android.widget.TextView[@resource-id="protect.budgetwatch:id/text" and @text="supermarket"]')
        escolherBudgat.click()

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("0399www")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando000000000000")

        calendar = self.driver.find_element(By.ID, 'protect.budgetwatch:id/dateEdit')
        calendar.click()
        dataCalendar = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="05 dezembro 2023"]')
        dataCalendar.click()
        ok = self.driver.find_element(By.ID, 'android:id/button1')
        ok.click()

        campoAccount = self.driver.find_element(By.ID, "protect.budgetwatch:id/accountEdit").get_attribute('text')

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        
        #self.driver.execute_script("alert('Este é um alerta de teste!');")

     
        self.assertLess(len(campoAccount), 9, f"O comprimento do nome  deve ser menor que ({len(campoAccount)}).")"""

"""
    self.assertLess(len(campoAccount), 9, self.driver.execute_script("alert('Nao vale')"))
def test_app_nomeMaiorQueDois(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando0")

        # Obter o texto do elemento
        element_text = self.driver.find_element(By.ID, "protect.budgetwatch:id/nameEdit").get_attribute('text')

        # Verificar se o comprimento do texto é maior que 10
        self.assertGreater(len(element_text), 2, f"O comprimento do nome  deve ser maior que ({len(element_text)}).")

"""
"""def test_app_transactions_delet(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # clicar em editar

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/name')
        add.click()
        self.driver.implicitly_wait(30)

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_edit')
        add.click()

        #clicar em delete

        pontinhos = self.driver.find_element(By.XPATH,
                                          "//android.widget.ImageView[@content-desc='More options']")
        pontinhos.click()
        

        excluir = self.driver.find_element(By.ID, 'protect.budgetwatch:id/title')
        excluir.click()

        confirmar = self.driver.find_element(By.ID, 'android:id/button1')
        confirmar.click()


        self.assertEqual(TestData.nsuper, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'NaoSuper2')]").get_attribute(
            'text'))
    """


"""def test_app_transactions_edit(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        # clicar em editar

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/name')
        add.click()
        self.driver.implicitly_wait(30)

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_edit')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.clear()
        name.send_keys("NaoSuper2")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetView')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.clear()
        value.send_keys("5000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.clear()
        value.send_keys("1")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.clear()
        value.send_keys("testandoEditar")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()


        self.assertEqual(TestData.nsuper, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'NaoSuper2')]").get_attribute(
            'text'))"""

"""def test_app_transactions_add(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()


        self.assertEqual(TestData.super, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'Super2')]").get_attribute(
            'text'))"""

"""def transactions_add(self):
        def __init__(self):
            self

        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()
    """

"""def test_app_budget_add(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Budgets')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_add')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        name.send_keys(TestData.budget_type)

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys(TestData.budget_value)

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()


        self.assertEqual(TestData.budget_type, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'supermarket')]").get_attribute(
            'text'))"""

"""budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()"""

"""if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)"""

"""def test_app_transactions_delete(self):
        if self.driver.find_element(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_element(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        budget = self.driver.find_element(By.XPATH,
                                          "//android.widget.TextView[contains(@text, 'Transactions')]")
        budget.click()

        add = self.driver.find_element(By.ID, 'protect.budgetwatch:id/title')
        add.click()

        name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/nameEdit')
        name.send_keys("Super2")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando0")

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()


        self.assertEqual(TestData.nsuper, self.driver.find_element(By.XPATH,
                                                                        "//android.widget.TextView[contains(@text, 'NaoSuper2')]").get_attribute(
            'text'))
    """

"""import unittest, time, os
from builtins import id

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from datetime import date
from time import sleep
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AndroidBudget(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'emulator-5554'
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=capabilities_options)

    def test_app_budget_add(self):
        if self.driver.find_elements(By.XPATH, "//android.widget.TextView[contains(@text, 'Welcome to Budget Watch')]"):
            skip = self.driver.find_elements(By.ID, 'protect.budgetwatch:id/skip')
            skip.click()
            self.driver.implicitly_wait(30)

        # clicar em budget
        #budget = self.driver.find_elements(By.XPATH, "//android.widget.TextView[contains(@text, 'Budgets')]")
        #budget.click()
        budget_elements = self.driver.find_elements(By.XPATH, "//android.widget.TextView[contains(@text, 'Budgets')]")
        if budget_elements:
            budget_elements[0].click()

        add = self.driver.find_elements(By.ID, 'protect.budgetwatch:id/action_add')
        if budget_elements:
            budget_elements[0].click()

        name = self.driver.find_elements(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        #name.send_keys("energia")
        if name:
            name[0].send_keys("energia")

        value = self.driver.find_elements(By.ID, 'protect.budgetwatch:id/valueEdit')
        #value.send_keys("500")
        if value:
            value[0].send_keys("500")

        name = self.driver.find_elements(By.ID, 'protect.budgetwatch:id/budgetNameEdit')
        #name.set_text("energia")
        if name:
            name[0].set_text("energia")

        value = self.driver.find_elements(By.ID, 'protect.budgetwatch:id/valueEdit')
        #value.set_text("500")
        if value:
            value[0].clear()  # Limpe o campo antes de inserir o novo valor
            value[0].send_keys("500")

        save = self.driver.find_elements(By.ID, 'protect.budgetwatch:id/action_save')
        #save.click()
        if save:
            save[0].click()

        #self.assertEqual("energia", self.driver.find_elements(By.XPATH, "//android.widget.TextView[contains(@text, 'energia')]").get_attribute('text'))
        # Encontrar todos os elementos correspondentes
        #wait = WebDriverWait(self.driver, 10)
        #text_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//android.widget.TextView[contains(@text, 'energia')]")))
        text_elements = self.driver.find_elements(By.XPATH, "//android.widget.TextView[contains(@text, 'energia')]")

        # Verificar se a lista de elementos não está vazia
        if text_elements:
            # Obter o texto do primeiro elemento na lista
            text_value = text_elements[0].get_attribute('text')

            # Comparar o texto com a string desejada usando o método assertEqual
            self.assertEqual("energia", text_value)
        else:
            # Se a lista estiver vazia, falhar o teste ou realizar outra ação apropriada
            self.fail("Elemento 'energia' não encontrado.")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)
    """