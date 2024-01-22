from appium.webdriver.common.appiumby import By
from BasePage import BasePage
from datetime import datetime


class AddExpensePage(BasePage):
    addExpense_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/btnAddExpense')
    localizaExpense = (By.XPATH, f"//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvTitle']")
    objeto = (By.XPATH, "//android.widget.TextView[contains(@text, 'Conserto telhado')]")
    expense_price_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etPrice')
    expense_title_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etTitle')
    expense_category_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/etCategory')
    expense_save_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/fabDone')
    deleta = (By.XPATH, "//android.widget.TextView[@content-desc='Delete']")
    textoErro = (By.XPATH, "//android.widget.TextView[contains(@resource-id, 'com.blogspot.e_kanivets.moneytracker:id/textinput_error')]")
    dataFutura = (By.XPATH, "//android.view.View[@content-desc='31 December 2023']")
    dataPassada = (By.XPATH, "//android.view.View[@content-desc='07 December 2023']")
    dataSalva = (By.XPATH, "//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvDate']")

    def type_price(self, text):
        price = self.driver.find_element(*AddExpensePage.expense_price_locator)
        price.send_keys(text)

    def type_title(self, text):
        title = self.driver.find_element(*AddExpensePage.expense_title_locator)
        title.send_keys(text)

    def type_categoria(self, text):
        categoria = self.driver.find_element(*AddExpensePage.expense_category_locator)
        categoria.send_keys(text)

    def click_save(self):
        title = self.driver.find_element(*AddExpensePage.expense_save_locator)
        title.click()

    def addExpense(self):
        add = self.driver.find_element(*AddExpensePage.addExpense_locator)
        add.click()

    def get_localizaExpense(self):
        localiza = self.driver.find_element(*AddExpensePage.objeto)
        return localiza.get_attribute('text')
    
    def click_localizado(self):
        localizado = self.driver.find_element(*AddExpensePage.localizaExpense)
        localizado.click()

    def click_delete(self):
        deleta = self.driver.find_element(*AddExpensePage.deleta)
        deleta.click()
    
    def get_erroPrice(self):
        textoErro = self.driver.find_element(*AddExpensePage.textoErro)
        return textoErro.get_attribute('text')
    
    def get_dataFutura(self):
        data = self.driver.find_element(*AddExpensePage.dataFutura)
        return data.get_attribute('content-desc')
    
    def get_dataPassada(self):
        data = self.driver.find_element(*AddExpensePage.dataPassada)
        return data.get_attribute('content-desc')
    
    def click_dataEscolhidaFutura(self):
        data = self.driver.find_element(*AddExpensePage.dataFutura)
        data.click()
    
    def click_dataEscolhidaPassada(self):
        data = self.driver.find_element(*AddExpensePage.dataPassada)
        data.click()

    def get_dataAtual(self):
        data_atual = datetime.now()
        data_formatada = data_atual.strftime("%d %B %Y")
        return data_formatada
    
    def get_dataSalva(self):
        dataAtual = self.get_dataAtual()
        data = self.driver.find_element(By.XPATH, f"//android.widget.TextView[contains(@text, '{dataAtual}')]")
        return data.get_attribute('text')
