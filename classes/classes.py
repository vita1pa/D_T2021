from selenium.webdriver.common.by import By
from selenium import webdriver

class BasePage(object):

    def __init__(self):
        self.driver = webdriver.Chrome('driver\\chromedriver.exe')

        self.driver.get('https://opensource-demo.orangehrmlive.com/')


class MainPage(BasePage):


    def __init__(self):
        super(MainPage, self).__init__()
        self.login_line = (By.ID, 'txtUsername')
        self.password_line = (By.ID, 'txtPassword')
        self.enter_button = (By.ID, 'btnLogin')

    def authorize(self):
        element = self.driver.find_element(*self.login_line).send_keys('Admin')
        element = self.driver.find_element(*self.password_line).send_keys('admin123')
        element = self.driver.find_element(*self.enter_button)
        element.click()
        return self.driver

    def login(self):
        element = self.driver.find_element(*self.login_line).send_keys('Admin')

    def password(self):
        element = self.driver.find_element(*self.password_line).send_keys('admin123')

    def enter_button_click(self):
        element = self.driver.find_element(*self.enter_button)
        element.click()
        return self.driver


class JobTitlePage():

    def __init__(self, page):
        self._page = page

        self.job_title_args = (By.ID, 'jobTitle_jobTitle')
        self.job_description_args = (By.ID, 'jobTitle_jobDescription')
        self.note_args = (By.ID, 'jobTitle_note')

        self.job_title = None

    def press_edit(self):
        edit = self._page.find_element(By.ID, "btnSave")
        edit.click()

    def set_job_title(self, value):
        element = self._page.find_element(*self.job_title_args).send_keys(value)
        self.job_title = value
        # print(value)
        # print(self.job_title)

    def set_job_description(self, value):
        element = self._page.find_element(*self.job_description_args).send_keys(value)

    def modify_job_description(self, value):
        element = self._page.find_element(*self.job_description_args).clear()
        self.set_job_description(value)

    def set_note(self, value):
        element = self._page.find_element(*self.note_args).send_keys(value)

    def get_job_title(self):
        # print(self.job_title)
        return self.job_title

    # def get_job_description(self):
    #     return self.job_description

    def enter_button_click(self):
        element = self._page.find_element(By.ID, "btnSave")
        element.click()


class GridPage():

    def __init__(self, page):
        self._page = page

    def press_add(self):
        add_button = self._page.find_elements_by_xpath("//input[@name='btnAdd' and @value='Add']")[0]
        add_button.click()

    def delete(self):
        delete_button = self._page.find_elements_by_xpath("//input[@id='btnDelete' and @value='Delete']")[0]
        delete_button.click()

        OK_button = self._page.find_elements_by_id('dialogDeleteBtn')[0]
        # print(len(OK_button))
        OK_button.click()

    def check(self, job_title):

        table_id = self._page.find_element(By.ID, "resultTable")
        rows = table_id.find_elements(By.TAG_NAME, "tr")

        for i, row in enumerate(rows):
            col = list(map(lambda val: val.text, row.find_elements(By.TAG_NAME, "td")))
            if i!=0:
                if col[1] == job_title:
                    print("Record", [col[1], col[2]],"was successfully added on", i, "position")
                    return 0
        print("Record", job_title, "is not found") 
    
    def get_link(self, job_title):

        table_id = self._page.find_element(By.ID, "resultTable")
        rows = table_id.find_elements(By.TAG_NAME, "tr")

        for i, row in enumerate(rows):
            col = list(map(lambda val: val.text, row.find_elements(By.TAG_NAME, "td")))
            if i!=0:
                if col[1] == job_title:
                    link = list(map(lambda val: val.get_attribute('href'), 
                                row.find_elements(By.XPATH, "//td[@class='left']/a")))[i-1]

                    return link

    def click_box(self, job_title):

        table_id = self._page.find_element(By.ID, "resultTable")
        rows = table_id.find_elements(By.TAG_NAME, "tr")

        for i, row in enumerate(rows):
            col = list(map(lambda val: val.text, row.find_elements(By.TAG_NAME, "td")))
            if i!=0:
                if col[1] == job_title:
                    # link = list(map(lambda val: val.get_attribute('id'), 
                    #             row.find_elements(By.XPATH, "//td[@input='checkbox']/a")))
                    element = row.find_elements_by_css_selector("input[name='chkSelectRow[]'][type='checkbox']")[0]
                    element.click()
                  

    def edit(self, link):
        self._page.get(link)