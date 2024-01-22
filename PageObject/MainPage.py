from appium.webdriver.common.appiumby import By
from BasePage import BasePage


class MainPage(BasePage):
    income_locator = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[contains(@text, 'ADD INCOME')]")
    expense_location = (By.XPATH, "//androidx.recyclerview.widget.RecyclerView[contains(@text, 'ADD EXPENSE')]")
    shortSummary_location = (By.XPATH, "//android.widget.TextView[@text='Short summary']")

    def click_income(self):
        income = self.driver.find_element(*MainPage.income_locator)
        income.click()

    def click_expense(self):
        expense = self.driver.find_element(*MainPage.expense_location)
        expense.click()
    
    def click_budget(self):
        shortSummary = self.driver.find_element(*MainPage.shortSummary_location)
        shortSummary.click()

