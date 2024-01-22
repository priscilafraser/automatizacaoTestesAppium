from Data import TestData
from selenium.webdriver.common.by import By

class Funcoes:
    def __init__(self):
        "code"

    def adicionarBudget(self):
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



    def adicionarTransactions(self):
        Funcoes.adicionarBudget(self)

        #Após adicionar budget, voltar para a tela anterior
        if self.driver.find_element(By.XPATH,
                                    "//android.view.ViewGroup[@resource-id='protect.budgetwatch:id/toolbar']"):
            skip = self.driver.find_element(By.XPATH, '//android.widget.ImageButton[@content-desc="Navigate up"]')
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

        budgetSpin = self.driver.find_element(By.ID, 'protect.budgetwatch:id/budgetSpinner')
        budgetSpin.click()
        escolherBudget = self.driver.find_element(By.XPATH,
                                                  '//android.widget.TextView[@resource-id="protect.budgetwatch:id/text" and @text="supermarket"]')
        escolherBudget.click()

        account = self.driver.find_element(By.ID, 'protect.budgetwatch:id/accountEdit')
        account.send_keys("2000")

        value = self.driver.find_element(By.ID, 'protect.budgetwatch:id/valueEdit')
        value.send_keys("1000")

        note = self.driver.find_element(By.ID, 'protect.budgetwatch:id/noteEdit')
        note.send_keys("testando0")

        calendar = self.driver.find_element(By.ID, 'protect.budgetwatch:id/dateEdit')
        calendar.click()
        dataCalendar = self.driver.find_element(By.XPATH, '//android.view.View[@content-desc="06 December 2023"]')
        dataCalendar.click()
        ok = self.driver.find_element(By.ID, 'android:id/button1')
        ok.click()

        save = self.driver.find_element(By.ID, 'protect.budgetwatch:id/action_save')
        save.click()

        