from appium.webdriver.common.appiumby import By
from BasePage import BasePage

class RecordsPage(BasePage):
    week_locator = (By.ID, 'com.blogspot.e_kanivets.moneytracker:id/spinner')
    shortSummary_locator = (By.XPATH, "//android.widget.TextView[@text='Short summary']") 
    allTime_locator = (By.XPATH, "//android.widget.TextView[@resource-id='android:id/text1' and @text='All time']")

    calendar_locator = (By.XPATH, "//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvDate']")
    dataEscolhida = (By.XPATH, "//android.view.View[@content-desc='01 December 2023']")
    okdate_locator = (By.ID, 'android:id/button1')

    titleDuplicidade1 = (By.XPATH, "(//android.widget.TextView[contains(@resource-id, 'com.blogspot.e_kanivets.moneytracker:id/tvTitle')])[1]")
    titleDuplicidade2 = (By.XPATH, "(//android.widget.TextView[contains(@resource-id, 'com.blogspot.e_kanivets.moneytracker:id/tvTitle')])[2]")

    categoryDuplicidade1 = (By.XPATH, "(//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvCategory'])[1]")
    categoryDuplicidade2 = (By.XPATH, "(//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvCategory'])[2]")

    priceDuplicidade1 = (By.XPATH, "(//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvPrice'])[1]")
    priceDuplicidade2 = (By.XPATH, "(//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvPrice'])[2]")

    dataDuplicidade = (By.XPATH, "//android.widget.TextView[@resource-id='com.blogspot.e_kanivets.moneytracker:id/tvDate']")

    def click_weef(self):
        title = self.driver.find_element(*RecordsPage.week_locator)
        title.click()

    def click_allTime(self):
        title = self.driver.find_element(*RecordsPage.allTime_locator)
        title.click()

    def click_shortSummary(self):
        title = self.driver.find_element(*RecordsPage.shortSummary_locator)
        title.click()
    
    def get_title1(self):
        text_titulo = self.driver.find_element(*RecordsPage.titleDuplicidade1)
        return text_titulo.get_attribute('text')
    
    def get_title2(self):
        text_titulo = self.driver.find_element(*RecordsPage.titleDuplicidade2)
        return text_titulo.get_attribute('text')
    
    def get_category1(self):
        text_categoria = self.driver.find_element(*RecordsPage.categoryDuplicidade1)
        return text_categoria.get_attribute('text')
    
    def get_category2(self):
        text_categoria = self.driver.find_element(*RecordsPage.categoryDuplicidade2)
        return text_categoria.get_attribute('text')
    
    def get_price1(self):
        text_price = self.driver.find_element(*RecordsPage.priceDuplicidade1)
        return text_price.get_attribute('text')
    
    def get_price2(self):
        text_price = self.driver.find_element(*RecordsPage.priceDuplicidade2)
        return text_price.get_attribute('text')

    def get_data(self):
        text_data = self.driver.find_element(*RecordsPage.dataDuplicidade)
        return text_data.get_attribute('text')

    def get_CalendarDate(self):
        calendar = self.driver.find_element(*RecordsPage.calendar_locator)
        calendar.click()

    def click_dataEscolhida(self):
        data = self.driver.find_element(*RecordsPage.dataEscolhida)
        data.click()
    
    def get_dataEscolhida(self):
        data = self.driver.find_element(*RecordsPage.dataEscolhida)
        return data.get_attribute('content-desc')
    
    def click_okData(self):
        ok = self.driver.find_element(*RecordsPage.okdate_locator)
        ok.click()
   