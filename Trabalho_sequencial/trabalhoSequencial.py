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

class AndroidBudget(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = ''
        desired_caps['appPackage'] = 'protect.budgetwatch'
        desired_caps['appActivity'] = '.MainActivity'

        capabilities_options = UiAutomator2Options().load_capabilities(desired_caps)

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', options=capabilities_options)


    def test_app_accountMenorQueNove(self):
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
        value.send_keys("03111111")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando000000000000")

        # Obter o texto do elemento
        campoAccount = self.driver.find_element(By.ID, "protect.budgetwatch:id/accountEdit").get_attribute('text')


        # Verificar se o comprimento do texto é maior que 10
        self.assertLess(len(campoAccount), 9, f"O comprimento do nome  deve ser menor que ({len(campoAccount)}).")
        #self.assertTrue(any(c.isalnum() or c in '!@#$%^&*()-_+=<>,.?/:;[]{}|' for c in campoAccount),
               # "O campo não contém pelo menos um caractere alfanumérico ou um símbolo.")


               

    def test_app_accountMMaiorQueDois(self):
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
        value.send_keys("203")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando000000000000")

        # Obter o texto do elemento
        campoAccount = self.driver.find_element(By.ID, "protect.budgetwatch:id/accountEdit").get_attribute('text')


        # Verificar se o comprimento do texto é maior que 10
        self.assertGreater(len(campoAccount), 2, f"O comprimento do nome  deve ser maior que ({len(campoAccount)}).")
        #self.assertTrue(any(c.isalnum() or c in '!@#$%^&*()-_+=<>,.?/:;[]{}|' for c in campoAccount),
               # "O campo não contém pelo menos um caractere alfanumérico ou um símbolo.")



    def test_app_valorENomeVazio(self):
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
        value.send_keys("testando000000000000")

        # Obter o texto do elemento
        nomeVazio = self.driver.find_element(By.ID, "protect.budgetwatch:id/nameEdit").get_attribute('text')
        valorVazio = self.driver.find_element(By.ID, "protect.budgetwatch:id/valueEdit").get_attribute('text')


        # Verificar se o comprimento do texto é maior que 10
        self.assertTrue(nomeVazio and valorVazio, "Ambos os campos estão vazios. Não deve ser possível salvar.")


    def test_app_nomeNaoVazio(self):
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
        name.send_keys("Super")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando000000000000")

        # Obter o texto do elemento
        elementVazio = self.driver.find_element(By.ID, "protect.budgetwatch:id/nameEdit").get_attribute('text')

        # Verificar se o comprimento do texto é maior que 10
        self.assertTrue(elementVazio, "O campo está vazio. Não pode salvar. Preencha corretamente")
        
       
    def test_app_valorNaoVazio(self):
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
        value.send_keys("testando000000000000")

        # Obter o texto do elemento
        elementVazio = self.driver.find_element(By.ID, "protect.budgetwatch:id/valueEdit").get_attribute('text')

        # Verificar se o comprimento do texto é maior que 10
        self.assertTrue(elementVazio, "O campo valor está vazio. Não pode salvar. Preencha corretamente")



    def test_app_noteMenorQueVinte(self):
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
        name.send_keys("12345678910111111111")

        #name = self.driver.find_element(By.ID, 'protect.budgetwatch:id/text')
        #name.send_keys("Super2")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        value.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        value.send_keys("testando000000000000")

        # Obter o texto do elemento
        element_text = self.driver.find_element(By.ID, "protect.budgetwatch:id/noteEdit").get_attribute('text')

        # Verificar se o comprimento do texto é maior que 10
        self.assertLess(len(element_text),21, f"O comprimento do campo note deve ser menor que ({len(element_text)}).")

        
    
    def test_app_nomeMenorQueDez(self):
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
        name.send_keys("12345678910111111111")

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
        self.assertLess(len(element_text),21, f"O comprimento do nome  deve ser menor que ({len(element_text)}).")
        
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
        name.send_keys("Super2")

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


    def test_app_transactions_delet(self):
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
        

    def test_app_transactions_edit(self):
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
            'text'))
    


    def test_app_transactions_add(self):
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
            'text'))
        

    def test_app_budget_add(self):
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
            'text'))
        
    
        

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(AndroidBudget)
    unittest.TextTestRunner(verbosity=2).run(suite)